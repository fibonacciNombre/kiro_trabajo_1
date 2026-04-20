"""Motor de inferencia semántica sobre la red semántica musical.

Implementa recorrido BFS ponderado, cálculo de distancia semántica,
búsqueda de caminos y generación de explicaciones.
"""

from collections import deque
from typing import Dict, List, Set

from src.models.enums import NodeType, RelationType
from src.models.data_models import (
    Explanation,
    Node,
    ScoredNode,
    SemanticPath,
)
from src.models.semantic_network import SemanticNetwork

# Relaciones consideradas simétricas para el cálculo de distancia
_SYMMETRIC_RELATIONS = {RelationType.SIMILAR_TO}


class InferenceEngine:
    """Motor de inferencia semántica que opera sobre una ``SemanticNetwork``.

    Proporciona:
    - Descubrimiento de nodos relacionados mediante BFS ponderado
    - Filtrado por tipo de nodo objetivo
    - Cálculo de distancia semántica entre pares de nodos
    - Búsqueda de caminos semánticos
    - Generación de explicaciones en lenguaje natural (español)
    """

    def __init__(self, network: SemanticNetwork) -> None:
        self._network = network

    # ── Helpers internos ───────────────────────────────────────────────

    @staticmethod
    def _path_weight(path: SemanticPath) -> float:
        """Producto de los pesos de las aristas en el camino.

        Si ``total_weight`` almacena la *suma* de pesos (como hace
        ``SemanticNetwork.find_paths``), recalculamos el producto a partir
        de los pesos individuales cuando están disponibles.  Como
        ``SemanticPath`` solo guarda ``total_weight`` como suma, usamos
        una aproximación: ``total_weight / path_length`` elevado a
        ``path_length`` no es exacta, así que preferimos usar
        ``total_weight`` directamente como proxy del peso acumulado.

        Para caminos construidos internamente con producto real, se usa
        el campo ``total_weight`` tal cual.
        """
        return path.total_weight if path.total_weight > 0 else 1e-9

    @staticmethod
    def _path_length(path: SemanticPath) -> int:
        """Número de aristas en el camino."""
        return max(len(path.relations), 1)

    @staticmethod
    def _diversity_bonus(path: SemanticPath) -> float:
        """Factor que premia variedad de tipos de relación en el camino.

        ``diversity_bonus = unique_relation_types / total_relations``
        Mínimo 1.0 para no penalizar caminos de una sola arista.
        """
        if not path.relations:
            return 1.0
        unique = len(set(path.relations))
        total = len(path.relations)
        # Escala entre 1.0 (todas iguales) y 2.0 (todas distintas)
        return 1.0 + (unique / total)

    def _score_paths(self, paths: List[SemanticPath]) -> float:
        """Calcula la puntuación agregada de un conjunto de caminos.

        Fórmula:
            score = Σ (path_weight(p) / path_length(p)) * diversity_bonus(p)
        """
        total = 0.0
        for p in paths:
            pw = self._path_weight(p)
            pl = self._path_length(p)
            db = self._diversity_bonus(p)
            total += (pw / pl) * db
        return total

    def _collect_paths_bfs(
        self,
        start_id: str,
        max_depth: int,
    ) -> Dict[str, List[SemanticPath]]:
        """BFS ponderado desde *start_id* hasta *max_depth*.

        Retorna un diccionario ``{node_id: [SemanticPath, ...]}`` con todos
        los caminos encontrados hacia cada nodo alcanzable.  Los pesos se
        calculan como *producto* de los pesos de aristas (no suma).
        """
        if start_id not in self._network:
            return {}

        # Cada elemento: (nodo_actual, nodos_visitados, relaciones, peso_producto)
        queue: deque = deque()
        queue.append((start_id, [start_id], [], 1.0))

        result: Dict[str, List[SemanticPath]] = {}

        while queue:
            current, path_nodes, path_rels, weight_product = queue.popleft()

            if len(path_rels) >= max_depth:
                continue

            for edge in self._network._adjacency.get(current, []):
                next_id = edge.target_id
                if next_id in path_nodes:
                    continue  # evitar ciclos

                new_nodes = path_nodes + [next_id]
                new_rels = path_rels + [edge.relation]
                new_weight = weight_product * edge.weight

                sp = SemanticPath(
                    nodes=new_nodes,
                    relations=new_rels,
                    total_weight=new_weight,
                )
                result.setdefault(next_id, []).append(sp)
                queue.append((next_id, new_nodes, new_rels, new_weight))

        return result

    # ── API pública ────────────────────────────────────────────────────

    def infer_related(
        self,
        node_id: str,
        max_depth: int = 3,
    ) -> List[ScoredNode]:
        """Descubre nodos relacionados mediante BFS ponderado.

        Retorna una lista de ``ScoredNode`` ordenada por puntuación
        descendente.  El nodo de origen no se incluye en los resultados.
        """
        paths_by_node = self._collect_paths_bfs(node_id, max_depth)

        scored: List[ScoredNode] = []
        for nid, paths in paths_by_node.items():
            node = self._network.get_node(nid)
            if node is None:
                continue
            score = self._score_paths(paths)
            scored.append(ScoredNode(node_id=nid, node=node, score=score))

        scored.sort(key=lambda s: s.score, reverse=True)
        return scored

    def infer_by_similarity(
        self,
        node_id: str,
        target_type: NodeType,
    ) -> List[ScoredNode]:
        """Infiere nodos relacionados filtrados por tipo de nodo objetivo.

        Equivale a ``infer_related`` pero solo retorna nodos cuyo
        ``node_type`` coincide con *target_type*.
        """
        all_related = self.infer_related(node_id)
        return [s for s in all_related if s.node.node_type == target_type]

    def compute_semantic_distance(
        self,
        node_a: str,
        node_b: str,
    ) -> float:
        """Calcula la distancia semántica entre dos nodos.

        La distancia es la inversa de la mejor puntuación de camino.
        Si no existe camino, retorna ``float('inf')``.

        Para relaciones simétricas (``SIMILAR_TO``), se consideran
        caminos en ambas direcciones y se toma el mínimo.
        """
        if node_a not in self._network or node_b not in self._network:
            return float("inf")
        if node_a == node_b:
            return 0.0

        def _best_score(src: str, tgt: str) -> float:
            paths_map = self._collect_paths_bfs(src, max_depth=4)
            paths = paths_map.get(tgt, [])
            if not paths:
                return 0.0
            return self._score_paths(paths)

        score_ab = _best_score(node_a, node_b)
        score_ba = _best_score(node_b, node_a)

        best = max(score_ab, score_ba)
        if best <= 0:
            return float("inf")
        return 1.0 / best

    def find_semantic_paths(
        self,
        source: str,
        target: str,
    ) -> List[SemanticPath]:
        """Encuentra caminos semánticos entre *source* y *target*.

        Delega a ``SemanticNetwork.find_paths`` y recalcula los pesos
        como producto de aristas para consistencia con la fórmula de
        puntuación.
        """
        raw_paths = self._network.find_paths(source, target, max_depth=4)

        # Recalcular pesos como producto
        result: List[SemanticPath] = []
        for rp in raw_paths:
            weight_product = 1.0
            for i in range(len(rp.relations)):
                src = rp.nodes[i]
                tgt = rp.nodes[i + 1]
                rel = rp.relations[i]
                # Buscar el peso real de la arista
                edge_weight = 1.0
                for edge in self._network._adjacency.get(src, []):
                    if edge.target_id == tgt and edge.relation == rel:
                        edge_weight = edge.weight
                        break
                weight_product *= edge_weight
            result.append(
                SemanticPath(
                    nodes=rp.nodes,
                    relations=rp.relations,
                    total_weight=weight_product,
                )
            )
        return result

    def explain_recommendation(
        self,
        source: str,
        recommended: str,
    ) -> Explanation:
        """Genera una explicación en español de por qué se recomienda un nodo.

        Encuentra el mejor camino semántico y construye un resumen en
        lenguaje natural con los pasos de razonamiento.
        """
        paths = self.find_semantic_paths(source, recommended)
        if not paths:
            return Explanation(
                summary="No se encontró una conexión semántica directa.",
                paths=[],
                reasoning_steps=["No existe un camino entre los nodos en la red semántica."],
            )

        # Elegir el mejor camino (mayor peso / menor longitud)
        best_path = max(
            paths,
            key=lambda p: (self._path_weight(p) / self._path_length(p)) * self._diversity_bonus(p),
        )

        source_node = self._network.get_node(source)
        target_node = self._network.get_node(recommended)
        source_name = source_node.name if source_node else source
        target_name = target_node.name if target_node else recommended

        # Construir pasos de razonamiento
        steps: List[str] = []
        for i, rel in enumerate(best_path.relations):
            from_node = self._network.get_node(best_path.nodes[i])
            to_node = self._network.get_node(best_path.nodes[i + 1])
            from_name = from_node.name if from_node else best_path.nodes[i]
            to_name = to_node.name if to_node else best_path.nodes[i + 1]
            steps.append(f"{from_name} → ({rel.value}) → {to_name}")

        # Resumen en lenguaje natural
        summary = (
            f"Se recomienda \"{target_name}\" a partir de \"{source_name}\" "
            f"porque existe una conexión semántica de {len(best_path.relations)} "
            f"paso(s) en la red de conocimiento musical: "
            + " → ".join(steps)
            + "."
        )

        return Explanation(
            summary=summary,
            paths=paths,
            reasoning_steps=steps,
        )
