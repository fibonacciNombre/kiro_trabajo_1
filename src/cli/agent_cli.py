"""Interfaz de línea de comandos del agente de recomendación musical.

Parsea consultas en lenguaje natural (español) y delega al
``RecommendationEngine`` para generar recomendaciones explicables.
"""

import re
from dataclasses import dataclass, field
from typing import List, Optional

from src.models.data_models import Explanation, Recommendation, SemanticPath
from src.models.enums import NodeType
from src.engine.recommendation_engine import RecommendationEngine


@dataclass
class AgentResponse:
    """Respuesta del agente con recomendaciones y un mensaje para el usuario."""

    recommendations: List[Recommendation] = field(default_factory=list)
    message: str = ""


# ── Patrones de consulta ───────────────────────────────────────────────

# Orden importa: patrones más específicos primero.
_SONG_PATTERNS = [
    re.compile(r"recomi[eé]ndame\s+algo\s+como\s+(.+)", re.IGNORECASE),
    re.compile(r"algo\s+(?:parecido|similar)\s+a\s+(.+)", re.IGNORECASE),
    re.compile(r"canciones?\s+(?:como|similar(?:es)?\s+a)\s+(.+)", re.IGNORECASE),
]

_ARTIST_PATTERNS = [
    re.compile(r"recomi[eé]ndame\s+canciones?\s+de\s+(.+)", re.IGNORECASE),
    re.compile(r"m[uú]sica\s+de\s+(.+)", re.IGNORECASE),
    re.compile(r"canciones?\s+de\s+(.+)", re.IGNORECASE),
]

_MOOD_PATTERNS = [
    re.compile(r"quiero\s+m[uú]sica\s+(.+)", re.IGNORECASE),
    re.compile(r"m[uú]sica\s+(?:para\s+)?(?:sentirme\s+)?(.+)", re.IGNORECASE),
    re.compile(r"algo\s+(.+?)(?:\s+por\s+favor)?$", re.IGNORECASE),
]

_GENRE_PATTERNS = [
    re.compile(r"recomi[eé]ndame\s+(.+)", re.IGNORECASE),
]

_EXIT_KEYWORDS = {"salir", "exit", "quit", "q"}


class AgentCLI:
    """Interfaz CLI para el agente de recomendación musical.

    Acepta consultas en español, las parsea para determinar el tipo
    (canción, artista, género, estado de ánimo) y delega al
    ``RecommendationEngine``.
    """

    def __init__(self, engine: RecommendationEngine) -> None:
        self._engine = engine

    # ── Búsqueda de entidades ──────────────────────────────────────────

    def _find_node_by_name(self, name: str, node_type: NodeType) -> Optional[str]:
        """Busca un nodo por nombre (case-insensitive) y tipo en la red.

        Retorna el ``id`` del nodo o ``None`` si no se encuentra.
        """
        name_lower = name.strip().lower()
        for node in self._engine._inference._network.get_nodes_by_type(node_type):
            if node.name.lower() == name_lower or node.id.lower() == name_lower:
                return node.id
        return None

    def _find_song(self, name: str) -> Optional[str]:
        return self._find_node_by_name(name, NodeType.SONG)

    def _find_artist(self, name: str) -> Optional[str]:
        return self._find_node_by_name(name, NodeType.ARTIST)

    def _find_genre(self, name: str) -> Optional[str]:
        return self._find_node_by_name(name, NodeType.GENRE)

    def _find_mood(self, name: str) -> Optional[str]:
        return self._find_node_by_name(name, NodeType.MOOD)

    # ── Parseo de consultas ────────────────────────────────────────────

    def process_query(self, query: str) -> AgentResponse:
        """Parsea una consulta de texto y delega al motor de recomendación.

        Determina el tipo de consulta (canción, artista, género, estado
        de ánimo) y extrae el nombre de la entidad.  Retorna un
        ``AgentResponse`` con las recomendaciones o un mensaje de error.
        """
        text = query.strip()
        if not text:
            return AgentResponse(message="Por favor, escribe una consulta. Ejemplo: recomiéndame algo como Bohemian Rhapsody")

        # 1. Intentar como canción
        for pattern in _SONG_PATTERNS:
            match = pattern.search(text)
            if match:
                entity = match.group(1).strip()
                return self._handle_song_query(entity)

        # 2. Intentar como artista
        for pattern in _ARTIST_PATTERNS:
            match = pattern.search(text)
            if match:
                entity = match.group(1).strip()
                return self._handle_artist_query(entity)

        # 3. Intentar como estado de ánimo
        for pattern in _MOOD_PATTERNS:
            match = pattern.search(text)
            if match:
                entity = match.group(1).strip()
                result = self._handle_mood_query(entity)
                if result.recommendations:
                    return result

        # 4. Intentar como género (patrón más genérico)
        for pattern in _GENRE_PATTERNS:
            match = pattern.search(text)
            if match:
                entity = match.group(1).strip()
                result = self._handle_genre_query(entity)
                if result.recommendations:
                    return result

        return AgentResponse(
            message=(
                f"No pude entender la consulta \"{text}\".\n"
                "Prueba con:\n"
                "  • recomiéndame algo como <canción>\n"
                "  • recomiéndame canciones de <artista>\n"
                "  • quiero música <estado de ánimo>\n"
                "  • recomiéndame <género>"
            )
        )

    # ── Handlers por tipo de consulta ──────────────────────────────────

    def _handle_song_query(self, entity: str) -> AgentResponse:
        song_id = self._find_song(entity)
        if song_id is None:
            return AgentResponse(
                message=f"No encontré la canción \"{entity}\" en la base de conocimiento."
            )
        recs = self._engine.recommend_by_song(song_id)
        if not recs:
            return AgentResponse(
                message=f"No encontré recomendaciones a partir de \"{entity}\"."
            )
        return AgentResponse(
            recommendations=recs,
            message=f"Recomendaciones basadas en la canción \"{entity}\":",
        )

    def _handle_artist_query(self, entity: str) -> AgentResponse:
        artist_id = self._find_artist(entity)
        if artist_id is None:
            return AgentResponse(
                message=f"No encontré al artista \"{entity}\" en la base de conocimiento."
            )
        recs = self._engine.recommend_by_artist(artist_id)
        if not recs:
            return AgentResponse(
                message=f"No encontré recomendaciones para el artista \"{entity}\"."
            )
        return AgentResponse(
            recommendations=recs,
            message=f"Recomendaciones basadas en el artista \"{entity}\":",
        )

    def _handle_mood_query(self, entity: str) -> AgentResponse:
        mood_id = self._find_mood(entity)
        if mood_id is None:
            return AgentResponse(
                message=f"No encontré el estado de ánimo \"{entity}\" en la base de conocimiento."
            )
        recs = self._engine.recommend_by_mood(entity)
        if not recs:
            return AgentResponse(
                message=f"No encontré recomendaciones para el estado de ánimo \"{entity}\"."
            )
        return AgentResponse(
            recommendations=recs,
            message=f"Recomendaciones para estado de ánimo \"{entity}\":",
        )

    def _handle_genre_query(self, entity: str) -> AgentResponse:
        genre_id = self._find_genre(entity)
        if genre_id is None:
            return AgentResponse(
                message=f"No encontré el género \"{entity}\" en la base de conocimiento."
            )
        recs = self._engine.recommend_by_genre(entity)
        if not recs:
            return AgentResponse(
                message=f"No encontré recomendaciones para el género \"{entity}\"."
            )
        return AgentResponse(
            recommendations=recs,
            message=f"Recomendaciones del género \"{entity}\":",
        )

    # ── Formateo de salida ─────────────────────────────────────────────

    def display_recommendations(self, recommendations: List[Recommendation]) -> str:
        """Formatea una lista de recomendaciones para la terminal.

        Cada recomendación muestra: posición, nombre, tipo, puntuación
        y un resumen de la explicación.
        """
        if not recommendations:
            return "  (sin resultados)"

        lines: List[str] = []
        for i, rec in enumerate(recommendations, start=1):
            node = rec.item
            type_label = node.node_type.value
            lines.append(f"  {i}. {node.name} [{type_label}] (score: {rec.score:.3f})")
            if rec.explanation and rec.explanation.summary:
                lines.append(f"     ↳ {rec.explanation.summary}")
        return "\n".join(lines)

    def display_explanation(self, explanation: Explanation) -> str:
        """Formatea una explicación con caminos semánticos legibles.

        Muestra el resumen, los pasos de razonamiento y los caminos
        semánticos con sus pesos.
        """
        lines: List[str] = []

        if explanation.summary:
            lines.append(f"  Resumen: {explanation.summary}")

        if explanation.reasoning_steps:
            lines.append("  Pasos de razonamiento:")
            for step in explanation.reasoning_steps:
                lines.append(f"    • {step}")

        if explanation.paths:
            lines.append("  Caminos semánticos:")
            for j, path in enumerate(explanation.paths, start=1):
                path_str = self._format_path(path)
                lines.append(f"    [{j}] {path_str} (peso: {path.total_weight:.3f})")

        return "\n".join(lines) if lines else "  (sin explicación disponible)"

    def _format_path(self, path: SemanticPath) -> str:
        """Convierte un ``SemanticPath`` en una cadena legible.

        Ejemplo: ``Bohemian Rhapsody →(interpretada_por)→ Queen →(pertenece_a_genero)→ Rock``
        """
        network = self._engine._inference._network
        parts: List[str] = []
        for i, node_id in enumerate(path.nodes):
            node = network.get_node(node_id)
            name = node.name if node else node_id
            parts.append(name)
            if i < len(path.relations):
                parts.append(f"→({path.relations[i].value})→")
        return " ".join(parts)

    # ── Bucle principal ────────────────────────────────────────────────

    def run(self) -> None:
        """Bucle principal de interacción con el usuario.

        Muestra un mensaje de bienvenida, acepta consultas en español
        y muestra recomendaciones formateadas hasta que el usuario
        escriba ``salir`` o ``exit``.
        """
        print("\n" + "=" * 60)
        print("  🎵 Agente de Recomendación Musical")
        print("  Basado en Redes Semánticas")
        print("=" * 60)
        print()
        print("  Soy un agente inteligente que recomienda música")
        print("  usando una red semántica de conocimiento musical.")
        print("  Puedo encontrar canciones relacionadas por género,")
        print("  artista, estado de ánimo e instrumentos.")
        print()
        print("  Ejemplos de consultas:")
        print("    • recomiéndame algo como Bohemian Rhapsody")
        print("    • recomiéndame canciones de Queen")
        print("    • quiero música relajada")
        print("    • recomiéndame rock")
        print()
        print("  Escribe 'salir' para terminar.")
        print("-" * 60)

        while True:
            try:
                user_input = input("\n🎵 > ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n¡Hasta luego! 🎶")
                break

            if not user_input:
                continue

            if user_input.lower() in _EXIT_KEYWORDS:
                print("¡Hasta luego! 🎶")
                break

            response = self.process_query(user_input)
            print()
            print(response.message)
            if response.recommendations:
                print(self.display_recommendations(response.recommendations))
