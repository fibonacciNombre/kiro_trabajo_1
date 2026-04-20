# Plan de Implementación: Agente Inteligente basado en Redes Semánticas para Recomendación Musical

## Visión General

Este plan cubre los dos entregables del proyecto: (1) el prototipo funcional del agente inteligente y (2) las secciones del documento de investigación académico. Las tareas están organizadas de forma incremental — cada tarea construye sobre las anteriores, y el código se integra progresivamente.

## Tareas

- [x] 1. Configurar estructura del proyecto y dependencias
  - Crear la estructura de directorios: `src/`, `src/models/`, `src/engine/`, `src/cli/`, `src/knowledge/`, `tests/`, `data/`
  - Crear `pyproject.toml` o `requirements.txt` con dependencias: `hypothesis`, `pytest`
  - Crear los archivos `__init__.py` necesarios
  - Crear `src/models/enums.py` con las enumeraciones `NodeType` y `RelationType` según el diseño
  - Crear `src/models/data_models.py` con los dataclasses `Node`, `Edge`, `Recommendation`, `Explanation`, `SemanticPath`, `ValidationResult`
  - _Requisitos: 6.1, 6.3_

- [ ] 2. Implementar el módulo de Red Semántica
  - [x] 2.1 Implementar la clase `SemanticNetwork` en `src/models/semantic_network.py`
    - Métodos: `add_node`, `add_edge`, `get_node`, `get_neighbors`, `find_paths`, `get_nodes_by_type`
    - Implementar `serialize` y `deserialize` para persistencia JSON
    - Usar un diccionario de adyacencia para almacenar el grafo
    - _Requisitos: 2.1, 6.1_

  - [ ]* 2.2 Escribir test de propiedad para serialización de la red semántica
    - **Propiedad 1: Viaje de ida y vuelta de serialización preserva la red**
    - Generar redes semánticas aleatorias con nodos y arcos válidos usando `hypothesis`
    - Verificar que `deserialize(serialize(red))` produce una red equivalente
    - **Valida: Requisitos 6.1**

  - [ ]* 2.3 Escribir tests unitarios para `SemanticNetwork`
    - Probar agregar/consultar nodos y arcos
    - Probar `get_neighbors` con y sin filtro de tipo de relación
    - Probar `find_paths` entre nodos conectados y desconectados
    - Probar `get_nodes_by_type` para cada `NodeType`
    - Probar casos borde: red vacía, nodo inexistente, arco duplicado
    - _Requisitos: 2.1, 6.1_

- [ ] 3. Implementar el Motor de Inferencia Semántica
  - [x] 3.1 Implementar la clase `InferenceEngine` en `src/engine/inference_engine.py`
    - Método `infer_related`: recorrido BFS ponderado hasta `max_depth`
    - Método `infer_by_similarity`: inferencia filtrada por tipo de nodo objetivo
    - Método `compute_semantic_distance`: cálculo de distancia semántica entre dos nodos
    - Método `find_semantic_paths`: encontrar caminos semánticos entre dos nodos
    - Método `explain_recommendation`: generar explicación con camino semántico
    - Implementar la fórmula de puntuación: `score = Σ (path_weight / path_length) * diversity_bonus`
    - _Requisitos: 2.2, 2.4_

  - [ ]* 3.2 Escribir test de propiedad para descubrimiento de conexiones indirectas
    - **Propiedad 2: El motor de inferencia descubre conexiones indirectas**
    - Generar redes con caminos de longitud ≤ `max_depth` entre pares de nodos
    - Verificar que `infer_related` encuentra al menos un camino
    - **Valida: Requisitos 2.2**

  - [ ]* 3.3 Escribir test de propiedad para consistencia de puntuación
    - **Propiedad 3: Consistencia de puntuación con distancia semántica**
    - Generar redes donde nodo A tiene camino más corto/pesado que nodo B al nodo de consulta
    - Verificar que `score(A) >= score(B)`
    - **Valida: Diseño del módulo inference_engine**

  - [ ]* 3.4 Escribir test de propiedad para simetría de distancia semántica
    - **Propiedad 5: Simetría de distancia semántica para relaciones simétricas**
    - Generar pares de nodos conectados exclusivamente por relaciones `SIMILAR_TO`
    - Verificar que `compute_semantic_distance(A, B) == compute_semantic_distance(B, A)`
    - **Valida: Diseño del módulo inference_engine**

  - [ ]* 3.5 Escribir tests unitarios para `InferenceEngine`
    - Probar inferencia sobre una red de ejemplo (Bohemian Rhapsody, Queen, Beatles)
    - Probar que nodos más cercanos reciben puntuación más alta
    - Probar `explain_recommendation` genera explicaciones con caminos válidos
    - Probar caso borde: nodo aislado, red vacía
    - _Requisitos: 2.2, 2.4_

- [x] 4. Checkpoint — Verificar que todos los tests pasan
  - Ejecutar todos los tests, consultar al usuario si surgen dudas.

- [ ] 5. Implementar el Motor de Recomendación
  - [x] 5.1 Implementar la clase `RecommendationEngine` en `src/engine/recommendation_engine.py`
    - Métodos: `recommend_by_song`, `recommend_by_artist`, `recommend_by_mood`, `recommend_by_genre`
    - Método `recommend_composite` para preferencias combinadas
    - Cada recomendación incluye puntuación, explicación y caminos semánticos
    - Orquestar llamadas al `InferenceEngine` y formatear resultados como `Recommendation`
    - _Requisitos: 2.2, 2.4, 3.1_

  - [ ]* 5.2 Escribir test de propiedad para explicaciones válidas en recomendaciones
    - **Propiedad 4: Toda recomendación tiene un camino de explicación válido**
    - Generar consultas de recomendación sobre redes aleatorias
    - Verificar que cada `Recommendation` devuelta contiene al menos un `SemanticPath` donde cada arista existe en la red
    - **Valida: Requisitos 2.4**

  - [ ]* 5.3 Escribir tests unitarios para `RecommendationEngine`
    - Probar cada tipo de recomendación con la red de ejemplo
    - Probar que `top_k` limita correctamente el número de resultados
    - Probar que recomendaciones incluyen explicaciones no vacías
    - _Requisitos: 2.2, 2.4, 3.1_

- [ ] 6. Construir la Base de Conocimiento Musical
  - [x] 6.1 Implementar la clase `KnowledgeBuilder` en `src/knowledge/knowledge_builder.py`
    - Métodos: `load_from_json`, `export_to_json`, `add_song`, `add_artist`, `build_relationships`
    - Método `validate_network` que verifica integridad de la red (nodos referenciados existen, tipos válidos)
    - _Requisitos: 6.1_

  - [x] 6.2 Crear el archivo de datos `data/music_knowledge_base.json`
    - Incluir al menos 20 canciones, 15 artistas, 8 géneros, 6 estados de ánimo, 6 instrumentos, 5 épocas
    - Definir relaciones semánticas entre todas las entidades: `PERFORMED_BY`, `BELONGS_TO_GENRE`, `EVOKES_MOOD`, `FEATURES_INSTRUMENT`, `FROM_ERA`, `SIMILAR_TO`, `INFLUENCED_BY`, `SUBGENRE_OF`
    - Asegurar que el grafo sea conexo (todos los nodos alcanzables)
    - _Requisitos: 6.1, 1.4_

  - [ ]* 6.3 Escribir test de propiedad para validación de referencias inválidas
    - **Propiedad 6: La validación de red detecta referencias inválidas**
    - Generar redes con arcos que referencian nodos inexistentes
    - Verificar que `validate_network` reporta al menos un error
    - **Valida: Requisitos 6.1**

  - [ ]* 6.4 Escribir tests unitarios para `KnowledgeBuilder`
    - Probar carga desde JSON válido e inválido
    - Probar `validate_network` con red válida y con referencias rotas
    - Probar `export_to_json` genera archivo legible
    - _Requisitos: 6.1_

- [x] 7. Checkpoint — Verificar que todos los tests pasan
  - Ejecutar todos los tests, consultar al usuario si surgen dudas.

- [ ] 8. Implementar la Interfaz CLI del Agente
  - [x] 8.1 Implementar la clase `AgentCLI` en `src/cli/agent_cli.py`
    - Método `run`: bucle principal de interacción con el usuario
    - Método `process_query`: parsear consulta de texto y delegar al `RecommendationEngine`
    - Método `display_recommendations`: formatear recomendaciones para terminal
    - Método `display_explanation`: formatear explicaciones con caminos semánticos legibles
    - Soportar consultas por canción, artista, género y estado de ánimo
    - Incluir manejo de errores: nodo no encontrado, sin resultados, entrada inválida
    - _Requisitos: 6.1, 6.3_

  - [x] 8.2 Crear punto de entrada `main.py` en la raíz del proyecto
    - Cargar la base de conocimiento desde `data/music_knowledge_base.json`
    - Instanciar `SemanticNetwork`, `KnowledgeBuilder`, `InferenceEngine`, `RecommendationEngine`, `AgentCLI`
    - Conectar todos los componentes e iniciar el CLI
    - _Requisitos: 6.3_

  - [ ]* 8.3 Escribir tests unitarios para `AgentCLI`
    - Probar `process_query` con diferentes tipos de consulta
    - Probar manejo de errores: consulta vacía, entidad no encontrada
    - Probar formato de salida de recomendaciones
    - _Requisitos: 6.1_

- [ ] 9. Tests de integración
  - [ ]* 9.1 Escribir tests de integración del flujo completo
    - Probar flujo completo: carga de base de conocimiento → consulta → inferencia → recomendación → explicación
    - Verificar que la base de conocimiento de ejemplo cumple el tamaño mínimo declarado en el alcance
    - Verificar que todos los nodos son alcanzables desde al menos un nodo de consulta
    - _Requisitos: 6.1, 2.2, 2.4_

- [x] 10. Checkpoint final — Verificar que todos los tests pasan
  - Ejecutar todos los tests, consultar al usuario si surgen dudas.

- [ ] 11. Redactar secciones del documento de investigación
  - [x] 11.1 Crear `docs/planteamiento_del_problema.md`
    - Describir la sobrecarga de información en plataformas de streaming musical con datos cuantitativos
    - Identificar limitaciones del filtrado colaborativo (cold start, dependencia de datos, falta de explicabilidad) citando H. Li et al. (2016)
    - Identificar limitaciones del filtrado basado en contenido (análisis superficial, burbuja de filtro) citando F. Bani Younes et al. (2018)
    - Formular el problema central: ausencia de mecanismo que capture relaciones semánticas complejas
    - _Requisitos: 1.1, 1.2, 1.3, 1.4_

  - [x] 11.2 Crear `docs/justificacion.md`
    - Argumentar ventajas de redes semánticas sobre representaciones planas, citando F. Tang et al. (2017)
    - Demostrar que la inferencia semántica descubre relaciones implícitas, citando H. Li et al. (2016)
    - Presentar evidencia de aplicabilidad en dominios de recomendación: películas (Bani Younes, 2018), productos (Zhang, 2019)
    - Justificar explicabilidad inherente de las redes semánticas
    - Comparar con otras técnicas de representación del conocimiento (marcos, lógica de predicados, ontologías) según Capítulo 10
    - _Requisitos: 2.1, 2.2, 2.3, 2.4, 2.5_

  - [x] 11.3 Crear `docs/preguntas_de_investigacion.md`
    - Formular pregunta principal sobre cómo un agente basado en redes semánticas mejora recomendaciones musicales
    - Formular al menos tres preguntas secundarias: construcción de la red, mecanismo de inferencia, evaluación
    - Vincular cada pregunta con al menos un paper de referencia
    - Verificar que cada pregunta sea específica, medible y alcanzable
    - _Requisitos: 3.1, 3.2, 3.3, 3.4_

  - [x] 11.4 Crear `docs/objetivos.md`
    - Definir objetivo general: desarrollo del agente inteligente basado en redes semánticas
    - Definir al menos cuatro objetivos específicos (analizar, diseñar, implementar, evaluar)
    - Cada objetivo con verbo en infinitivo medible
    - Trazar cada objetivo a al menos una pregunta de investigación
    - _Requisitos: 4.1, 4.2, 4.3, 4.4_

  - [x] 11.5 Crear `docs/estado_del_arte.md`
    - Analizar al menos cinco de los ocho papers de referencia (problema, técnica, resultados, limitaciones)
    - Clasificar trabajos en categorías: recomendación con redes semánticas, representación del conocimiento, recuperación de información
    - Identificar la brecha de investigación (gap)
    - Crear tabla comparativa de trabajos relacionados
    - Fundamentar conceptos de agente inteligente (Capítulo 2) y representación del conocimiento (Capítulo 10)
    - _Requisitos: 5.1, 5.2, 5.3, 5.4, 5.5_

  - [x] 11.6 Crear `docs/alcance_y_limitaciones.md`
    - Delimitar alcance: dominio musical cubierto, tamaño mínimo de base de conocimiento, tipos de consultas
    - Identificar limitaciones: tamaño acotado, ausencia de aprendizaje automático, evaluación con grupo reducido
    - Definir entregables: documento de investigación y prototipo funcional
    - Especificar metodología de desarrollo alineada con reglas del proyecto
    - _Requisitos: 6.1, 6.2, 6.3, 6.4_

- [ ] 12. Crear estructura del documento final y glosario
  - [x] 12.1 Crear `docs/estructura_documento.md`
    - Definir la estructura completa del informe: introducción, planteamiento, justificación, objetivos, marco teórico, estado del arte, propuesta, implementación, evaluación, conclusiones, referencias
    - Incluir glosario de términos técnicos de IA y redes semánticas
    - Incluir lista de referencias bibliográficas en formato APA o IEEE (8 papers + capítulos del libro)
    - Verificar cumplimiento con fuentes académicas verificables
    - _Requisitos: 7.1, 7.2, 7.3, 7.4_

- [x] 13. Checkpoint final — Revisión completa
  - Verificar que todos los tests pasan, que la base de conocimiento es válida, y que todas las secciones del documento están completas. Consultar al usuario si surgen dudas.

## Notas

- Las tareas marcadas con `*` son opcionales y pueden omitirse para un MVP más rápido
- Cada tarea referencia requisitos específicos para trazabilidad
- Los checkpoints aseguran validación incremental
- Los tests de propiedades validan propiedades universales de correctitud definidas en el diseño (usando `hypothesis`)
- Los tests unitarios validan ejemplos específicos y casos borde
- El lenguaje de implementación es **Python** según el diseño técnico
