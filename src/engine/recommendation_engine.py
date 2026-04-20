"""Motor de recomendación musical basado en inferencia semántica.

Orquesta llamadas al InferenceEngine para generar recomendaciones
filtradas por canción, artista, estado de ánimo, género o preferencias
combinadas del usuario.
"""

from typing import Dict, List

from src.models.enums import NodeType
from src.models.data_models import (
    Recommendation,
    SemanticPath,
    UserPreferences,
)
from src.engine.inference_engine import InferenceEngine


class RecommendationEngine:
    """Genera recomendaciones musicales usando el motor de inferencia semántica.

    Cada método produce una lista de ``Recommendation`` ordenada por
    puntuación descendente, donde cada recomendación incluye el nodo
    recomendado, su puntuación, una explicación en lenguaje natural y
    los caminos semánticos que la justifican.
    """

    def __init__(self, inference: InferenceEngine) -> None:
        self._inference = inference

    # ── Helpers ────────────────────────────────────────────────────────

    def _build_recommendations(
        self,
        source_id: str,
        target_type: NodeType,
        top_k: int,
    ) -> List[Recommendation]:
        """Genera recomendaciones desde *source_id* filtrando por tipo."""
        scored = self._inference.infer_by_similarity(source_id, target_type)
        results: List[Recommendation] = []
        for sn in scored[:top_k]:
            explanation = self._inference.explain_recommendation(source_id, sn.node_id)
            paths = self._inference.find_semantic_paths(source_id, sn.node_id)
            results.append(
                Recommendation(
                    item=sn.node,
                    score=sn.score,
                    explanation=explanation,
                    semantic_paths=paths,
                )
            )
        return results

    def _find_node_id_by_name_and_type(
        self,
        name: str,
        node_type: NodeType,
    ) -> str | None:
        """Busca un nodo por nombre (case-insensitive) y tipo."""
        for node in self._inference._network.get_nodes_by_type(node_type):
            if node.name.lower() == name.lower() or node.id.lower() == name.lower():
                return node.id
        return None

    # ── API pública ────────────────────────────────────────────────────

    def recommend_by_song(
        self,
        song_id: str,
        top_k: int = 5,
    ) -> List[Recommendation]:
        """Recomienda canciones similares a la canción dada.

        Usa ``infer_by_similarity`` para encontrar canciones relacionadas
        semánticamente y construye objetos ``Recommendation`` con
        explicaciones.
        """
        return self._build_recommendations(song_id, NodeType.SONG, top_k)

    def recommend_by_artist(
        self,
        artist_id: str,
        top_k: int = 5,
    ) -> List[Recommendation]:
        """Recomienda canciones relacionadas con un artista.

        Busca canciones conectadas al artista a través de la red
        semántica (interpretaciones, influencias, géneros compartidos).
        """
        return self._build_recommendations(artist_id, NodeType.SONG, top_k)

    def recommend_by_mood(
        self,
        mood: str,
        top_k: int = 5,
    ) -> List[Recommendation]:
        """Recomienda canciones que evocan un estado de ánimo dado.

        Busca el nodo de estado de ánimo por nombre o id y luego
        encuentra canciones conectadas semánticamente.
        """
        mood_id = self._find_node_id_by_name_and_type(mood, NodeType.MOOD)
        if mood_id is None:
            return []
        return self._build_recommendations(mood_id, NodeType.SONG, top_k)

    def recommend_by_genre(
        self,
        genre: str,
        top_k: int = 5,
    ) -> List[Recommendation]:
        """Recomienda canciones de un género dado.

        Busca el nodo de género por nombre o id y luego encuentra
        canciones conectadas semánticamente.
        """
        genre_id = self._find_node_id_by_name_and_type(genre, NodeType.GENRE)
        if genre_id is None:
            return []
        return self._build_recommendations(genre_id, NodeType.SONG, top_k)

    def recommend_composite(
        self,
        preferences: UserPreferences,
        top_k: int = 5,
    ) -> List[Recommendation]:
        """Genera recomendaciones combinando múltiples preferencias.

        Recopila recomendaciones de cada criterio (canciones, artistas,
        estados de ánimo, géneros), fusiona los resultados por nodo y
        promedia las puntuaciones para producir un ranking unificado.
        """
        # Recopilar candidatos de cada fuente de preferencia
        candidates: Dict[str, List[Recommendation]] = {}

        for song_id in preferences.song_ids:
            for rec in self.recommend_by_song(song_id, top_k=top_k * 2):
                candidates.setdefault(rec.item.id, []).append(rec)

        for artist_id in preferences.artist_ids:
            for rec in self.recommend_by_artist(artist_id, top_k=top_k * 2):
                candidates.setdefault(rec.item.id, []).append(rec)

        for mood in preferences.moods:
            for rec in self.recommend_by_mood(mood, top_k=top_k * 2):
                candidates.setdefault(rec.item.id, []).append(rec)

        for genre in preferences.genres:
            for rec in self.recommend_by_genre(genre, top_k=top_k * 2):
                candidates.setdefault(rec.item.id, []).append(rec)

        if not candidates:
            return []

        # Fusionar: promediar puntuaciones, combinar caminos, elegir mejor explicación
        merged: List[Recommendation] = []
        for node_id, recs in candidates.items():
            avg_score = sum(r.score for r in recs) / len(recs)
            # Elegir la explicación con más pasos de razonamiento
            best_explanation = max(recs, key=lambda r: len(r.explanation.reasoning_steps)).explanation
            # Combinar caminos semánticos únicos
            all_paths: List[SemanticPath] = []
            seen_path_keys: set = set()
            for r in recs:
                for p in r.semantic_paths:
                    key = tuple(p.nodes)
                    if key not in seen_path_keys:
                        seen_path_keys.add(key)
                        all_paths.append(p)

            merged.append(
                Recommendation(
                    item=recs[0].item,
                    score=avg_score,
                    explanation=best_explanation,
                    semantic_paths=all_paths,
                )
            )

        merged.sort(key=lambda r: r.score, reverse=True)
        return merged[:top_k]
