"""Modelos de datos (dataclasses) para la red semántica musical."""

from dataclasses import dataclass, field
from typing import List

from src.models.enums import NodeType, RelationType


@dataclass
class Node:
    """Nodo de la red semántica que representa un concepto del dominio musical."""
    id: str
    node_type: NodeType
    name: str
    attributes: dict = field(default_factory=dict)


@dataclass
class Edge:
    """Arco dirigido y etiquetado entre dos nodos de la red semántica."""
    source_id: str
    target_id: str
    relation: RelationType
    weight: float = 1.0


@dataclass
class ScoredNode:
    """Nodo con puntuación de relevancia calculada por el motor de inferencia."""
    node_id: str
    node: "Node"
    score: float


@dataclass
class SemanticPath:
    """Camino semántico entre nodos de la red."""
    nodes: List[str] = field(default_factory=list)
    relations: List[RelationType] = field(default_factory=list)
    total_weight: float = 0.0


@dataclass
class Explanation:
    """Explicación de una recomendación con caminos semánticos."""
    summary: str = ""
    paths: List[SemanticPath] = field(default_factory=list)
    reasoning_steps: List[str] = field(default_factory=list)


@dataclass
class Recommendation:
    """Recomendación generada por el agente con explicación y caminos."""
    item: Node = field(default_factory=lambda: Node("", NodeType.SONG, ""))
    score: float = 0.0
    explanation: Explanation = field(default_factory=Explanation)
    semantic_paths: List[SemanticPath] = field(default_factory=list)


@dataclass
class UserPreferences:
    """Preferencias del usuario para recomendaciones compuestas."""
    song_ids: List[str] = field(default_factory=list)
    artist_ids: List[str] = field(default_factory=list)
    moods: List[str] = field(default_factory=list)
    genres: List[str] = field(default_factory=list)


@dataclass
class ValidationResult:
    """Resultado de la validación de integridad de la red semántica."""
    is_valid: bool = True
    errors: List[str] = field(default_factory=list)
