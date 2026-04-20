# Preguntas de Investigación

## 3.1 Pregunta Principal

La pregunta central que guía la presente investigación se formula a partir de la brecha identificada en el planteamiento del problema — la ausencia de mecanismos de recomendación musical que capturen y exploten relaciones semánticas complejas entre entidades del dominio — y de la justificación del enfoque de redes semánticas como técnica de representación del conocimiento adecuada para abordar dicha brecha:

> **¿Cómo puede un Agente Inteligente basado en Redes Semánticas mejorar la calidad y explicabilidad de las recomendaciones musicales al capturar relaciones semánticas entre entidades del dominio musical?**

Esta pregunta integra los tres ejes fundamentales del proyecto: (1) la representación del conocimiento musical mediante redes semánticas, (2) la inferencia semántica como mecanismo de razonamiento del agente inteligente, y (3) la evaluación de la calidad y explicabilidad de las recomendaciones generadas. Su formulación es consistente con los hallazgos de H. Li et al. (2016), quienes demuestran que la representación semántica del dominio musical permite descubrir relaciones implícitas que los enfoques tradicionales de filtrado colaborativo y basado en contenido no pueden detectar, y con los resultados de F. Bani Younes et al. (2018), quienes evidencian que las redes semánticas mejoran la precisión y diversidad de las recomendaciones en dominios con entidades interconectadas por relaciones tipadas.

La pregunta es **específica** porque delimita el enfoque al dominio musical y a la técnica de redes semánticas; **medible** porque la calidad y explicabilidad de las recomendaciones pueden evaluarse mediante métricas cuantitativas (precision@k, recall@k) y cualitativas (evaluación de usuarios sobre la comprensibilidad de las explicaciones); y **alcanzable** porque el alcance del proyecto contempla el desarrollo de un prototipo funcional con una base de conocimiento acotada que permite la verificación empírica de la propuesta.


## 3.2 Preguntas Secundarias

Las preguntas secundarias descomponen la pregunta principal en dimensiones específicas que corresponden a las fases del proyecto y permiten abordar de manera sistemática los aspectos de construcción, inferencia y evaluación del agente inteligente.

### Pregunta Secundaria 1: Construcción de la Red Semántica del Dominio Musical

> **¿Cómo se puede modelar el conocimiento del dominio musical mediante una red semántica que represente las relaciones tipadas entre canciones, artistas, géneros, estados de ánimo, instrumentos y épocas, de forma que la estructura resultante sea suficientemente expresiva para soportar inferencia semántica?**

**Fundamentación:** F. Tang et al. (2017) demuestran que las redes semánticas permiten representar relaciones complejas entre entidades de un dominio mediante nodos y arcos tipados, superando las limitaciones de las representaciones planas basadas en vectores de características. En el contexto musical, esto implica definir una taxonomía de tipos de nodos (canción, artista, género, estado de ánimo, instrumento, época) y una tipología de relaciones semánticas (interpretada_por, pertenece_a_género, evoca_estado, presenta_instrumento, influenciado_por, similar_a, subgénero_de, de_época) que capture la riqueza relacional del dominio. Adicionalmente, F. Bani Younes et al. (2018) evidencian en el dominio cinematográfico que la definición adecuada de tipos de nodos y relaciones es un factor determinante en la calidad de las recomendaciones generadas a partir de la red.

**Especificidad:** La pregunta delimita las seis categorías de entidades musicales y exige que la red resultante soporte inferencia semántica, lo que establece un criterio de suficiencia verificable.

**Medibilidad:** Se puede evaluar mediante la validación de integridad de la red (todos los nodos referenciados existen, todos los tipos son válidos), la conectividad del grafo (todos los nodos son alcanzables), y el cumplimiento del tamaño mínimo de la base de conocimiento definido en el alcance del proyecto.

**Alcanzabilidad:** El proyecto contempla la construcción de una base de conocimiento con al menos 20 canciones, 15 artistas, 8 géneros, 6 estados de ánimo, 6 instrumentos y 5 épocas, un tamaño manejable que permite la construcción manual curada y la verificación exhaustiva de la estructura.


### Pregunta Secundaria 2: Mecanismo de Inferencia Semántica para la Generación de Recomendaciones

> **¿De qué manera un mecanismo de inferencia semántica basado en recorrido de grafos ponderado puede descubrir conexiones implícitas entre entidades musicales y generar recomendaciones con explicaciones trazables a través de caminos semánticos en la red?**

**Fundamentación:** H. Li et al. (2016) demuestran que la inferencia sobre grafos de conocimiento musical permite identificar conexiones no triviales entre entidades que los enfoques convencionales no pueden detectar — por ejemplo, que dos canciones aparentemente disímiles comparten conexiones profundas a través de cadenas de influencias artísticas, instrumentos compartidos y estados de ánimo comunes. Los autores evidencian que el recorrido de caminos semánticos produce recomendaciones más diversas y comprensibles que las generadas por filtrado colaborativo. Complementariamente, G. Wu et al. (2018) muestran que los sistemas de recuperación de información basados en redes semánticas mejoran la relevancia de los resultados al explotar relaciones multi-nivel entre entidades, y A. Ba et al. (2015) demuestran que la integración de redes semánticas en motores de búsqueda permite descubrir relaciones implícitas que mejoran la precisión de la recuperación de información.

**Especificidad:** La pregunta precisa el tipo de mecanismo (recorrido de grafos ponderado), el resultado esperado (descubrimiento de conexiones implícitas) y la propiedad diferenciadora (explicaciones trazables mediante caminos semánticos).

**Medibilidad:** Se puede evaluar verificando que el motor de inferencia descubre conexiones indirectas entre nodos conectados por caminos de longitud ≤ max_depth (Propiedad 2 del diseño), que la puntuación de recomendación es consistente con la distancia semántica (Propiedad 3), y que toda recomendación incluye al menos un camino de explicación válido (Propiedad 4).

**Alcanzabilidad:** El diseño técnico del proyecto define un algoritmo de inferencia BFS ponderado con fórmula de puntuación explícita, cuya implementación y verificación son factibles dentro del alcance del proyecto.


### Pregunta Secundaria 3: Evaluación de la Calidad de las Recomendaciones

> **¿En qué medida las recomendaciones generadas por el agente inteligente basado en redes semánticas superan en diversidad y explicabilidad a las producidas por enfoques tradicionales de filtrado colaborativo y basado en contenido?**

**Fundamentación:** J. Zhang et al. (2019) demuestran en el dominio de recomendación de productos que las recomendaciones basadas en grafos de conocimiento mejoran la precisión en comparación con enfoques de filtrado colaborativo y basado en contenido, particularmente en escenarios con datos de interacción escasos. Además, los autores evidencian que la explicabilidad de las recomendaciones — fundamentada en caminos semánticos trazables — aumenta la aceptación por parte de los usuarios. F. Bani Younes et al. (2018) reportan resultados análogos en el dominio cinematográfico, donde el enfoque de redes semánticas supera a los sistemas convencionales en precisión, capacidad de recomendación transversal entre géneros y mitigación del problema de arranque en frío. R. Gupta et al. (2017), por su parte, demuestran que el análisis de redes semánticas permite capturar relaciones contextuales que mejoran la calidad del procesamiento de información en dominios complejos.

**Especificidad:** La pregunta identifica las dos dimensiones de evaluación (diversidad y explicabilidad) y establece como punto de comparación los enfoques tradicionales (filtrado colaborativo y basado en contenido).

**Medibilidad:** La diversidad puede evaluarse mediante métricas de cobertura de géneros y tipos de entidades en las recomendaciones. La explicabilidad puede evaluarse verificando que cada recomendación incluye un camino semántico válido y comprensible (Propiedad 4 del diseño), y mediante evaluación cualitativa con un grupo reducido de usuarios sobre la comprensibilidad y utilidad de las explicaciones generadas.

**Alcanzabilidad:** El proyecto contempla la evaluación del prototipo mediante métricas cuantitativas (precision@k, recall@k) y evaluación cualitativa con un grupo reducido de usuarios, lo que permite una comparación fundamentada dentro del alcance definido.


### Pregunta Secundaria 4: Mitigación del Problema de Arranque en Frío

> **¿Cómo puede el conocimiento estructurado en una red semántica mitigar el problema de arranque en frío (*cold start*) al permitir la generación de recomendaciones para entidades musicales nuevas basándose en sus relaciones semánticas con entidades existentes, sin depender de datos históricos de interacción de usuarios?**

**Fundamentación:** H. Li et al. (2016) identifican el problema de arranque en frío como una de las limitaciones más críticas del filtrado colaborativo, particularmente aguda en el dominio musical donde artistas emergentes y lanzamientos recientes carecen de historial de interacciones. Los autores proponen que la representación semántica del dominio permite generar recomendaciones para nuevos ítems basándose en sus relaciones con entidades existentes en la red. M. Wang et al. (2019) corroboran este hallazgo en el dominio de la salud, demostrando que las redes semánticas permiten integrar nuevas entidades al sistema de conocimiento mediante la definición de sus relaciones con entidades preexistentes, sin necesidad de datos históricos de uso. F. Bani Younes et al. (2018) reportan que en su sistema de recomendación de películas, las nuevas películas pueden ser recomendadas inmediatamente al incorporarse a la red semántica con sus relaciones de director, actores, género y temática.

**Especificidad:** La pregunta se centra en un problema concreto (arranque en frío) y en un mecanismo específico (relaciones semánticas con entidades existentes como sustituto de datos históricos).

**Medibilidad:** Se puede evaluar incorporando nuevas entidades musicales a la red semántica y verificando que el agente genera recomendaciones relevantes para dichas entidades sin disponer de datos de interacción de usuarios, midiendo la precisión de las recomendaciones generadas exclusivamente a partir de relaciones semánticas.

**Alcanzabilidad:** El prototipo permite agregar nuevos nodos a la red semántica y verificar que el motor de inferencia genera recomendaciones basadas en las relaciones definidas, lo que constituye una demostración empírica factible dentro del alcance del proyecto.


## 3.3 Vinculación de Preguntas con Referencias

La siguiente tabla sintetiza la vinculación de cada pregunta de investigación con los papers de referencia que fundamentan su formulación:

| Pregunta | Referencias principales | Aspecto fundamentado |
|---|---|---|
| **Principal** | H. Li et al. (2016); F. Bani Younes et al. (2018) | Redes semánticas mejoran calidad y explicabilidad de recomendaciones en dominios con entidades interconectadas |
| **Secundaria 1** (Construcción) | F. Tang et al. (2017); F. Bani Younes et al. (2018) | Representación de relaciones complejas mediante nodos y arcos tipados; definición de taxonomías de entidades |
| **Secundaria 2** (Inferencia) | H. Li et al. (2016); G. Wu et al. (2018); A. Ba et al. (2015) | Descubrimiento de conexiones implícitas mediante recorrido de grafos; inferencia multi-nivel |
| **Secundaria 3** (Evaluación) | J. Zhang et al. (2019); F. Bani Younes et al. (2018); R. Gupta et al. (2017) | Superioridad en precisión, diversidad y explicabilidad frente a enfoques tradicionales |
| **Secundaria 4** (Arranque en frío) | H. Li et al. (2016); M. Wang et al. (2019); F. Bani Younes et al. (2018) | Mitigación del cold start mediante conocimiento estructurado |


## 3.4 Verificación de Criterios de Calidad

Cada pregunta de investigación cumple con los criterios de calidad requeridos para un proyecto de maestría:

| Criterio | Pregunta Principal | Secundaria 1 | Secundaria 2 | Secundaria 3 | Secundaria 4 |
|---|---|---|---|---|---|
| **Específica** | Delimita dominio musical y técnica de redes semánticas | Precisa tipos de entidades y relaciones | Define mecanismo de inferencia y tipo de resultado | Identifica dimensiones de evaluación y punto de comparación | Se centra en problema concreto y mecanismo específico |
| **Medible** | Precision@k, recall@k, evaluación cualitativa | Validación de integridad, conectividad, tamaño mínimo | Propiedades 2, 3 y 4 del diseño | Métricas de diversidad, evaluación cualitativa de explicabilidad | Precisión de recomendaciones para entidades nuevas |
| **Alcanzable** | Prototipo funcional con base de conocimiento acotada | Base de conocimiento de tamaño definido y verificable | Algoritmo BFS ponderado con fórmula explícita | Evaluación con métricas cuantitativas y grupo reducido de usuarios | Demostración empírica mediante adición de nodos a la red |

---

## Referencias

Ba, A., Abdou, S., & Gueye, B. (2015). Enhancing search engines with semantic networks. *International Journal of Advanced Computer Science and Applications*, *6*(3), 45–52.

Bani Younes, F., Boudhir, A. A., & Agnaou, M. (2018). A semantic network approach to movie recommendation. *International Journal of Computer Applications*, *182*(15), 1–6.

Gupta, R., Singh, A., & Kumar, P. (2017). Semantic network analysis of social media data for opinion mining. *Journal of Intelligent Information Systems*, *49*(1), 113–135.

Li, H., Li, Y., & Zhang, M. (2016). Music recommendation based on semantic network. *Proceedings of the International Conference on Computer Science and Network Technology*, 356–360.

Tang, F., Mu, W., Zhang, M., & Liang, S. (2017). Knowledge representation in semantic networks for organizations. *International Journal of Knowledge Engineering*, *3*(1), 15–21.

Wang, M., Liu, X., & Chen, H. (2019). Knowledge representation in semantic networks for healthcare. *Journal of Biomedical Informatics*, *92*, 103–115.

Wu, G., Zhang, L., & Wang, F. (2018). Semantic network-based information retrieval system. *Information Processing & Management*, *54*(6), 1032–1049.

Zhang, J., Wang, Y., & Chen, L. (2019). Product recommendation using semantic networks. *Journal of Intelligent Information Systems*, *52*(2), 285–308.
