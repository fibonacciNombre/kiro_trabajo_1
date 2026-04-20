"""Constructor de base de conocimiento musical.

Carga, exporta y valida la red semántica a partir de archivos JSON.
"""

import json
from typing import Optional

from src.models.enums import NodeType, RelationType
from src.models.data_models import ValidationResult
from src.models.semantic_network import SemanticNetwork


# Conjuntos de valores válidos para validación
_VALID_NODE_TYPES = {t.value for t in NodeType}
_VALID_RELATION_TYPES = {t.value for t in RelationType}


class KnowledgeBuilder:
    """Construye y administra la base de conocimiento de la red semántica."""

    def __init__(self, network: SemanticNetwork) -> None:
        self._network = network

    # ── Persistencia ───────────────────────────────────────────────────

    def load_from_json(self, filepath: str) -> None:
        """Lee un archivo JSON y carga los datos en la red semántica.

        Raises:
            FileNotFoundError: Si el archivo no existe.
            json.JSONDecodeError: Si el JSON es inválido.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self._network.deserialize(data)

    def export_to_json(self, filepath: str) -> None:
        """Serializa la red semántica y la escribe a un archivo JSON."""
        data = self._network.serialize()
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    # ── Agregar entidades ──────────────────────────────────────────────

    def add_song(self, song_data: dict) -> str:
        """Agrega un nodo de tipo canción a la red.

        Args:
            song_data: Diccionario con claves ``id``, ``name`` y opcionalmente
                ``attributes``.

        Returns:
            El id del nodo creado.
        """
        node_id = song_data["id"]
        name = song_data["name"]
        attributes = song_data.get("attributes", {})
        self._network.add_node(node_id, NodeType.SONG, name, attributes)
        return node_id

    def add_artist(self, artist_data: dict) -> str:
        """Agrega un nodo de tipo artista a la red.

        Args:
            artist_data: Diccionario con claves ``id``, ``name`` y opcionalmente
                ``attributes``.

        Returns:
            El id del nodo creado.
        """
        node_id = artist_data["id"]
        name = artist_data["name"]
        attributes = artist_data.get("attributes", {})
        self._network.add_node(node_id, NodeType.ARTIST, name, attributes)
        return node_id

    # ── Relaciones ─────────────────────────────────────────────────────

    def build_relationships(self) -> int:
        """Retorna la cantidad de arcos actualmente en la red.

        Las relaciones se definen en el JSON de la base de conocimiento y se
        cargan mediante ``load_from_json`` / ``deserialize``.  Este método es
        un atajo de conveniencia que devuelve el conteo de arcos existentes.
        """
        return len(self._network.edges)

    # ── Validación ─────────────────────────────────────────────────────

    def validate_network(self) -> ValidationResult:
        """Verifica la integridad de la red semántica.

        Comprueba que:
        - Todos los arcos referencian nodos existentes.
        - Todos los tipos de nodo son válidos.
        - Todos los tipos de relación son válidos.

        Returns:
            ``ValidationResult`` con ``is_valid`` y lista de errores.
        """
        errors: list[str] = []
        nodes = self._network.nodes

        # Validar tipos de nodo
        for node_id, node in nodes.items():
            if node.node_type.value not in _VALID_NODE_TYPES:
                errors.append(
                    f"Nodo '{node_id}' tiene tipo inválido: {node.node_type}"
                )

        # Validar arcos
        for edge in self._network.edges:
            # Referencias a nodos existentes
            if edge.source_id not in nodes:
                errors.append(
                    f"Arco referencia nodo origen inexistente: '{edge.source_id}'"
                )
            if edge.target_id not in nodes:
                errors.append(
                    f"Arco referencia nodo destino inexistente: '{edge.target_id}'"
                )
            # Tipo de relación válido
            if edge.relation.value not in _VALID_RELATION_TYPES:
                errors.append(
                    f"Arco '{edge.source_id}' -> '{edge.target_id}' tiene relación inválida: {edge.relation}"
                )

        return ValidationResult(is_valid=len(errors) == 0, errors=errors)
