# Objetivos de Investigación

## 4.1 Objetivo General

A partir del problema identificado — la ausencia de un mecanismo de recomendación musical que capture y explote relaciones semánticas complejas entre entidades del dominio — y de la justificación del enfoque de redes semánticas como técnica de representación del conocimiento adecuada para abordarlo, se formula el siguiente objetivo general:

> **Desarrollar un Agente Inteligente basado en Redes Semánticas que permita generar recomendaciones musicales de calidad, diversas y explicables, mediante la representación del conocimiento del dominio musical como un grafo de nodos y arcos tipados y la aplicación de inferencia semántica para descubrir relaciones implícitas entre entidades musicales.**

Este objetivo integra los tres ejes fundamentales del proyecto: (1) la representación estructurada del conocimiento musical mediante una red semántica con tipos de nodos (canción, artista, género, estado de ánimo, instrumento, época) y relaciones tipadas (interpretada_por, pertenece_a_género, evoca_estado, presenta_instrumento, influenciado_por, similar_a, subgénero_de, de_época); (2) la inferencia semántica como mecanismo de razonamiento del agente inteligente para descubrir conexiones no evidentes entre entidades; y (3) la generación de recomendaciones explicables donde cada sugerencia se fundamenta en caminos semánticos trazables a través de la red de conocimiento.

El objetivo es **alcanzable** dentro del alcance de un proyecto de maestría, ya que contempla el desarrollo de un prototipo funcional con una base de conocimiento acotada (al menos 20 canciones, 15 artistas, 8 géneros, 6 estados de ánimo, 6 instrumentos y 5 épocas) que permite la verificación empírica de la propuesta. Es **medible** porque la calidad de las recomendaciones puede evaluarse mediante métricas cuantitativas (precision@k, recall@k) y la explicabilidad mediante la verificación de que cada recomendación incluye caminos semánticos válidos y comprensibles.


## 4.2 Objetivos Específicos

Los objetivos específicos descomponen el objetivo general en metas concretas y verificables que corresponden a las fases del proyecto y se alinean con las preguntas de investigación formuladas en la sección 3.

### Objetivo Específico 1: Análisis del Estado del Arte

> **Analizar el estado del arte en sistemas de recomendación basados en redes semánticas y técnicas de representación del conocimiento, identificando las contribuciones, limitaciones y brechas de investigación existentes en la literatura.**

**Verbo medible:** *Analizar* — implica la revisión sistemática, extracción de hallazgos clave y síntesis comparativa de los trabajos relacionados.

**Trazabilidad con preguntas de investigación:**
- **Pregunta Principal** — El análisis del estado del arte fundamenta la viabilidad de utilizar redes semánticas para mejorar la calidad y explicabilidad de las recomendaciones musicales, al identificar evidencia empírica en dominios análogos (H. Li et al., 2016; F. Bani Younes et al., 2018).
- **Pregunta Secundaria 3** (Evaluación) — La revisión de trabajos previos establece las métricas y criterios de comparación con enfoques tradicionales de filtrado colaborativo y basado en contenido (J. Zhang et al., 2019; R. Gupta et al., 2017).

**Criterio de verificación:** Se considera cumplido cuando se ha producido un análisis estructurado de al menos cinco de los ocho papers de referencia, clasificados en categorías temáticas, con una tabla comparativa y la identificación explícita de la brecha de investigación que el proyecto aborda.


### Objetivo Específico 2: Diseño de la Red Semántica

> **Diseñar una red semántica del dominio musical que represente las relaciones tipadas entre canciones, artistas, géneros, estados de ánimo, instrumentos y épocas, definiendo una taxonomía de tipos de nodos y una tipología de relaciones semánticas suficientemente expresivas para soportar inferencia semántica.**

**Verbo medible:** *Diseñar* — implica la definición formal de la estructura de la red, los tipos de entidades, los tipos de relaciones y las restricciones de integridad del modelo.

**Trazabilidad con preguntas de investigación:**
- **Pregunta Secundaria 1** (Construcción de la Red Semántica) — Este objetivo responde directamente a la pregunta sobre cómo modelar el conocimiento del dominio musical mediante una red semántica con relaciones tipadas entre las seis categorías de entidades definidas (F. Tang et al., 2017; F. Bani Younes et al., 2018).

**Criterio de verificación:** Se considera cumplido cuando se ha definido la taxonomía completa de tipos de nodos (al menos 6 tipos) y tipos de relaciones (al menos 8 tipos), se ha construido una base de conocimiento que cumple el tamaño mínimo declarado en el alcance, y la red resultante pasa las validaciones de integridad (todos los nodos referenciados existen, todos los tipos son válidos, el grafo es conexo).


### Objetivo Específico 3: Implementación del Agente Inteligente

> **Implementar un agente inteligente basado en conocimiento que, mediante un motor de inferencia semántica con recorrido BFS ponderado sobre la red semántica, descubra conexiones implícitas entre entidades musicales y genere recomendaciones con explicaciones trazables a través de caminos semánticos.**

**Verbo medible:** *Implementar* — implica la codificación, integración y puesta en funcionamiento del prototipo completo del agente con todos sus componentes (red semántica, motor de inferencia, motor de recomendación, interfaz de usuario).

**Trazabilidad con preguntas de investigación:**
- **Pregunta Secundaria 2** (Mecanismo de Inferencia Semántica) — Este objetivo responde directamente a la pregunta sobre cómo un mecanismo de inferencia basado en recorrido de grafos ponderado puede descubrir conexiones implícitas y generar recomendaciones con explicaciones trazables (H. Li et al., 2016; G. Wu et al., 2018; A. Ba et al., 2015).
- **Pregunta Secundaria 4** (Mitigación del Arranque en Frío) — La implementación del agente basado en conocimiento estructurado permite generar recomendaciones para entidades nuevas basándose en sus relaciones semánticas con entidades existentes, sin depender de datos históricos de interacción (H. Li et al., 2016; M. Wang et al., 2019).

**Criterio de verificación:** Se considera cumplido cuando el prototipo funcional permite: (a) cargar la base de conocimiento musical desde formato JSON, (b) procesar consultas de recomendación por canción, artista, género y estado de ánimo, (c) generar recomendaciones ordenadas por puntuación de relevancia semántica, y (d) producir explicaciones basadas en caminos semánticos válidos para cada recomendación.


### Objetivo Específico 4: Evaluación del Desempeño del Agente

> **Evaluar el desempeño del agente inteligente en términos de diversidad y explicabilidad de las recomendaciones generadas, verificando que la inferencia semántica sobre la red de conocimiento produce resultados superiores en estas dimensiones respecto a los enfoques tradicionales de filtrado colaborativo y basado en contenido.**

**Verbo medible:** *Evaluar* — implica la aplicación de métricas cuantitativas y criterios cualitativos para medir el desempeño del agente y compararlo con los enfoques tradicionales documentados en la literatura.

**Trazabilidad con preguntas de investigación:**
- **Pregunta Secundaria 3** (Evaluación de la Calidad de las Recomendaciones) — Este objetivo responde directamente a la pregunta sobre en qué medida las recomendaciones del agente superan en diversidad y explicabilidad a las producidas por enfoques tradicionales (J. Zhang et al., 2019; F. Bani Younes et al., 2018; R. Gupta et al., 2017).

**Criterio de verificación:** Se considera cumplido cuando se ha realizado: (a) evaluación cuantitativa mediante métricas de precision@k y recall@k sobre un conjunto de prueba, (b) verificación de que cada recomendación incluye al menos un camino semántico válido y comprensible, (c) evaluación de la diversidad de las recomendaciones mediante cobertura de géneros y tipos de entidades, y (d) evaluación cualitativa con un grupo reducido de usuarios sobre la comprensibilidad y utilidad de las explicaciones generadas.


### Objetivo Específico 5: Demostración de la Mitigación del Arranque en Frío

> **Demostrar que el conocimiento estructurado en la red semántica permite mitigar el problema de arranque en frío al generar recomendaciones para entidades musicales nuevas basándose en sus relaciones semánticas con entidades existentes, sin requerir datos históricos de interacción de usuarios.**

**Verbo medible:** *Demostrar* — implica la verificación empírica mediante la incorporación de nuevas entidades a la red y la comprobación de que el agente genera recomendaciones relevantes para dichas entidades.

**Trazabilidad con preguntas de investigación:**
- **Pregunta Secundaria 4** (Mitigación del Problema de Arranque en Frío) — Este objetivo responde directamente a la pregunta sobre cómo el conocimiento estructurado en una red semántica puede mitigar el cold start (H. Li et al., 2016; M. Wang et al., 2019; F. Bani Younes et al., 2018).

**Criterio de verificación:** Se considera cumplido cuando se ha incorporado al menos una entidad musical nueva a la red semántica (con sus relaciones semánticas definidas) y se ha verificado que el agente genera recomendaciones relevantes para dicha entidad sin disponer de datos de interacción de usuarios, midiendo la precisión de las recomendaciones generadas exclusivamente a partir de relaciones semánticas.


## 4.3 Matriz de Trazabilidad Objetivos–Preguntas de Investigación

La siguiente tabla sintetiza la correspondencia entre cada objetivo específico y las preguntas de investigación que aborda:

| Objetivo Específico | Pregunta Principal | Secundaria 1 (Construcción) | Secundaria 2 (Inferencia) | Secundaria 3 (Evaluación) | Secundaria 4 (Arranque en frío) |
|---|---|---|---|---|---|
| **OE1** — Analizar estado del arte | ✓ | | | ✓ | |
| **OE2** — Diseñar red semántica | | ✓ | | | |
| **OE3** — Implementar agente inteligente | | | ✓ | | ✓ |
| **OE4** — Evaluar desempeño | | | | ✓ | |
| **OE5** — Demostrar mitigación cold start | | | | | ✓ |

Esta matriz verifica que:
- Cada objetivo específico es trazable a al menos una pregunta de investigación (Requisito 4.4).
- Cada pregunta de investigación es abordada por al menos un objetivo específico, garantizando cobertura completa.
- El conjunto de objetivos específicos cubre las cuatro fases del proyecto: análisis (OE1), diseño (OE2), implementación (OE3) y evaluación (OE4, OE5).


## 4.4 Verificación de Criterios de Calidad

Cada objetivo específico cumple con los criterios de calidad requeridos para un proyecto de maestría:

| Criterio | OE1 (Analizar) | OE2 (Diseñar) | OE3 (Implementar) | OE4 (Evaluar) | OE5 (Demostrar) |
|---|---|---|---|---|---|
| **Verbo en infinitivo medible** | Analizar | Diseñar | Implementar | Evaluar | Demostrar |
| **Específico** | Delimita alcance a 5+ papers y 3 categorías | Precisa 6 tipos de nodos y 8+ tipos de relaciones | Define componentes y algoritmo BFS ponderado | Identifica métricas y dimensiones de evaluación | Se centra en cold start y mecanismo específico |
| **Medible** | Tabla comparativa, brecha identificada | Validación de integridad, conectividad, tamaño mínimo | Prototipo funcional con 4 tipos de consulta | Precision@k, recall@k, evaluación cualitativa | Recomendaciones para entidades nuevas sin historial |
| **Alcanzable** | 8 papers disponibles + 2 capítulos de referencia | Base de conocimiento de tamaño definido y verificable | Algoritmo BFS con fórmula de puntuación explícita | Conjunto de prueba acotado y grupo reducido de usuarios | Adición de nodos a la red y verificación empírica |
| **Trazable** | Pregunta Principal, Secundaria 3 | Secundaria 1 | Secundaria 2, Secundaria 4 | Secundaria 3 | Secundaria 4 |

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
