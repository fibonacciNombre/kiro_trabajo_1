"""Punto de entrada del agente de recomendación musical."""

from src.models.semantic_network import SemanticNetwork
from src.knowledge.knowledge_builder import KnowledgeBuilder
from src.engine.inference_engine import InferenceEngine
from src.engine.recommendation_engine import RecommendationEngine
from src.cli.agent_cli import AgentCLI


def main() -> None:
    network = SemanticNetwork()
    builder = KnowledgeBuilder(network)
    builder.load_from_json("data/music_knowledge_base.json")

    inference = InferenceEngine(network)
    recommendations = RecommendationEngine(inference)
    cli = AgentCLI(recommendations)
    cli.run()


if __name__ == "__main__":
    main()
