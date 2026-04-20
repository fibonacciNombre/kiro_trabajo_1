"""Red semántica: grafo dirigido con nodos y arcos tipados."""

from collections import deque
from typing import Dict, List, Optional

from src.models.enums import NodeType, RelationType
from src.models.data_models import Node, Edge, SemanticPath


class SemanticNetwork:
    """Estructura de datos de grafo dirigido para la red semántica musical.

    Usa un diccionario de adyacencia para almacenar nodos y arcos.
    """

    def __init__(self) -> None:
        self._nodes: Dict[str, Node] = {}
        self._edges: List[Edge] = []
        self._adjacency: Dict[str, List[Edge]] = {}

    def add_node(
        self,
        node_id: str,
        node_type: NodeType,
        name: str,
        attributes: Optional[dict] = None,
    ) -> Node:
        """Agrega un nodo a la red. Si ya existe, lo sobreescribe."""
        node = Node(id=node_id, node_type=node_type, name=name, attributes=attributes or {})
        self._nodes[node_id] = node
        if node_id not in self._adjacency:
            self._adjacency[node_id] = []
        return node

    def add_edge(
        self,
        source_id: str,
        target_id: str,
        relation: RelationType,
        weight: float = 1.0,
    ) -> Edge:
        """Agrega un arco dirigido entre dos nodos existentes.

        Raises:
            ValueError: Si alguno de los nodos no existe en la red.
        """
        if source_id not in self._nodes:
            raise ValueError(f"Nodo origen '{source_id}' no existe en la red.")
        if target_id not in self._nodes:
            raise ValueError(f"Nodo destino '{target_id}' no existe en la red.")

        edge = Edge(source_id=source_id, target_id=target_id, relation=relation, weight=weight)
        self._edges.append(edge)
        self._adjacency[source_id].append(edge)
        return edge

    def get_node(self, node_id: str) -> Optional[Node]:
        """Retorna el nodo con el id dado, o None si no existe."""
        return self._nodes.get(node_id)

    def get_neighbors(
        self,
        node_id: str,
        relation: Optional[RelationType] = None,
    ) -> List[Node]:
        """Retorna los vecinos de un nodo, opcionalmente filtrados por tipo de relación.

        Considera arcos salientes del nodo dado.

        Raises:
            ValueError: Si el nodo no existe en la red.
        """
        if node_id not in self._nodes:
            raise ValueError(f"Nodo '{node_id}' no existe en la red.")

        edges = self._adjacency.get(node_id, [])
        if relation is not None:
            edges = [e for e in edges if e.relation == relation]

        neighbors: List[Node] = []
        seen: set = set()
        for edge in edges:
            if edge.target_id not in seen:
                node = self._nodes.get(edge.target_id)
                if node is not None:
                    neighbors.append(node)
                    seen.add(edge.target_id)
        return neighbors

    def get_nodes_by_type(self, node_type: NodeType) -> List[Node]:
        """Retorna todos los nodos de un tipo dado."""
        return [n for n in self._nodes.values() if n.node_type == node_type]

    def find_paths(
        self,
        source_id: str,
        target_id: str,
        max_depth: int = 4,
    ) -> List[SemanticPath]:
        """Encuentra todos los caminos entre dos nodos usando BFS hasta max_depth.

        Retorna lista vacía si alguno de los nodos no existe o no hay caminos.
        """
        if source_id not in self._nodes or target_id not in self._nodes:
            return []
        if source_id == target_id:
            return [SemanticPath(nodes=[source_id], relations=[], total_weight=0.0)]

        results: List[SemanticPath] = []
        # BFS: cada elemento es (nodo_actual, camino_nodos, camino_relaciones, peso_acumulado)
        queue: deque = deque()
        queue.append((source_id, [source_id], [], 0.0))

        while queue:
            current, path_nodes, path_relations, weight = queue.popleft()

            if len(path_relations) >= max_depth:
                continue

            for edge in self._adjacency.get(current, []):
                next_node = edge.target_id
                # Evitar ciclos dentro del mismo camino
                if next_node in path_nodes:
                    continue

                new_nodes = path_nodes + [next_node]
                new_relations = path_relations + [edge.relation]
                new_weight = weight + edge.weight

                if next_node == target_id:
                    results.append(
                        SemanticPath(
                            nodes=new_nodes,
                            relations=new_relations,
                            total_weight=new_weight,
                        )
                    )
                else:
                    queue.append((next_node, new_nodes, new_relations, new_weight))

        return results

    # ── Persistencia JSON ──────────────────────────────────────────────

    def serialize(self) -> dict:
        """Serializa la red semántica a un diccionario JSON-compatible."""
        return {
            "nodes": [
                {
                    "id": n.id,
                    "type": n.node_type.value,
                    "name": n.name,
                    "attributes": n.attributes,
                }
                for n in self._nodes.values()
            ],
            "edges": [
                {
                    "source": e.source_id,
                    "target": e.target_id,
                    "relation": e.relation.value,
                    "weight": e.weight,
                }
                for e in self._edges
            ],
        }

    def deserialize(self, data: dict) -> None:
        """Reconstruye la red semántica a partir de un diccionario serializado.

        Limpia el estado actual antes de cargar los datos nuevos.

        Raises:
            KeyError: Si faltan campos obligatorios en los datos.
            ValueError: Si un tipo de nodo o relación no es válido.
        """
        self._nodes.clear()
        self._edges.clear()
        self._adjacency.clear()

        for node_data in data.get("nodes", []):
            node_type = NodeType(node_data["type"])
            self.add_node(
                node_id=node_data["id"],
                node_type=node_type,
                name=node_data["name"],
                attributes=node_data.get("attributes", {}),
            )

        for edge_data in data.get("edges", []):
            relation = RelationType(edge_data["relation"])
            self.add_edge(
                source_id=edge_data["source"],
                target_id=edge_data["target"],
                relation=relation,
                weight=edge_data.get("weight", 1.0),
            )

    # ── Utilidades ─────────────────────────────────────────────────────

    @property
    def nodes(self) -> Dict[str, Node]:
        """Acceso de solo lectura al diccionario de nodos."""
        return dict(self._nodes)

    @property
    def edges(self) -> List[Edge]:
        """Acceso de solo lectura a la lista de arcos."""
        return list(self._edges)

    def __len__(self) -> int:
        """Retorna la cantidad de nodos en la red."""
        return len(self._nodes)

    def __contains__(self, node_id: str) -> bool:
        """Verifica si un nodo existe en la red."""
        return node_id in self._nodes
