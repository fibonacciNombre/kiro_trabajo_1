# Alcance y Limitaciones

## 6.1 Delimitación del Alcance del Proyecto

El presente proyecto se enmarca en el desarrollo de un agente inteligente basado en redes semánticas para la recomendación musical, con un alcance deliberadamente acotado que permite la verificación empírica de la propuesta dentro de los límites de un trabajo de investigación de maestría. A continuación se delimitan las tres dimensiones principales del alcance: el dominio musical cubierto, el tamaño de la base de conocimiento, y los tipos de consultas soportadas por el agente.

### 6.1.1 Dominio musical cubierto

La red semántica del proyecto modela el dominio musical mediante seis categorías de entidades representadas como tipos de nodos:

- **Canciones** (*cancion*): Obras musicales individuales, cada una con atributos de año de publicación y duración.
- **Artistas** (*artista*): Intérpretes y compositores, tanto solistas como bandas, con atributos de país de origen y período de actividad.
- **Géneros** (*genero*): Categorías musicales organizadas jerárquicamente mediante relaciones de subgénero, abarcando géneros principales (rock, pop, jazz, blues, electrónica, R&B, soul, reggae) y subgéneros derivados (rock progresivo, grunge, new wave, funk).
- **Estados de ánimo** (*estado_animo*): Dimensiones emocionales asociadas a las canciones, incluyendo estados como épico, nostálgico, melancólico, enérgico, reflexivo, alegre, rebelde y espiritual.
- **Instrumentos** (*instrumento*): Instrumentos musicales predominantes en las canciones y ejecutados por los artistas, incluyendo piano, guitarra eléctrica, batería, bajo, saxofón, sintetizador, guitarra acústica, voz y órgano.
- **Épocas** (*epoca*): Períodos temporales que contextualizan las canciones y artistas, cubriendo desde los años 50 hasta los años 2000.

Las relaciones semánticas entre estas entidades se modelan mediante trece tipos de arcos tipados y ponderados: *interpretada_por*, *compuesta_por*, *pertenece_a_genero*, *subgenero_de*, *evoca_estado*, *presenta_instrumento*, *toca_instrumento*, *de_epoca*, *en_album*, *album_de*, *similar_a*, *influenciado_por* y relaciones de álbum. Esta tipología de relaciones permite representar la estructura relacional multi-nivel del dominio musical, capturando conexiones de interpretación, composición, clasificación genérica, evocación emocional, instrumentación, contexto temporal, influencia artística y similitud estilística.

El dominio cubierto se centra en música popular occidental de la segunda mitad del siglo XX y principios del siglo XXI, abarcando géneros representativos como rock, pop, jazz, blues, electrónica, R&B, soul y reggae. Esta delimitación responde a la disponibilidad de información estructurada sobre las relaciones entre entidades musicales de este período y a la riqueza relacional que estos géneros presentan en términos de influencias cruzadas, evolución estilística y conexiones instrumentales.

### 6.1.2 Tamaño de la base de conocimiento

La base de conocimiento del prototipo constituye una representación acotada pero suficientemente expresiva del dominio musical para demostrar la viabilidad del enfoque propuesto. Sus dimensiones concretas son:

| Tipo de entidad | Cantidad |
|---|---|
| Canciones | 23 |
| Artistas | 22 |
| Géneros | 12 |
| Estados de ánimo | 8 |
| Instrumentos | 9 |
| Épocas | 8 |
| Álbumes | 18 |
| **Total de nodos** | **100** |
| **Total de arcos (relaciones)** | **360** |

Estas cifras superan los mínimos establecidos en el diseño técnico del proyecto (20 canciones, 15 artistas, 8 géneros, 6 estados de ánimo, 6 instrumentos, 5 épocas) y garantizan una densidad relacional suficiente para que el motor de inferencia semántica pueda descubrir conexiones indirectas significativas entre entidades. La proporción de 3.6 arcos por nodo indica una red con conectividad adecuada para el recorrido BFS ponderado que implementa el motor de inferencia.

La base de conocimiento se almacena en formato JSON (`data/music_knowledge_base.json`) y se construye de forma curada manualmente, asegurando la precisión y coherencia de las relaciones semánticas representadas. Cada nodo incluye un identificador único, un tipo válido según la taxonomía definida, un nombre legible y atributos específicos del tipo. Cada arco incluye nodos origen y destino válidos, un tipo de relación de la tipología definida y un peso numérico entre 0.0 y 1.0 que refleja la fuerza de la relación.

### 6.1.3 Tipos de consultas soportadas

El agente inteligente soporta cuatro tipos de consultas de recomendación, cada uno correspondiente a un punto de entrada diferente en la red semántica:

1. **Recomendación por canción**: A partir de una canción específica, el agente recorre la red semántica para identificar canciones relacionadas a través de múltiples dimensiones (género compartido, artista común, estado de ánimo similar, instrumentación afín, época cercana). Ejemplo: *"Recomiéndame canciones similares a Bohemian Rhapsody"*.

2. **Recomendación por artista**: A partir de un artista, el agente explora las conexiones de influencia, similitud estilística, género compartido y época para identificar otros artistas y sus canciones que el usuario podría disfrutar. Ejemplo: *"Recomiéndame música basada en Queen"*.

3. **Recomendación por género**: A partir de un género musical, el agente identifica canciones y artistas pertenecientes al género especificado y a géneros relacionados (subgéneros, géneros padre, géneros con artistas en común). Ejemplo: *"Recomiéndame canciones de rock progresivo"*.

4. **Recomendación por estado de ánimo**: A partir de un estado de ánimo, el agente identifica canciones que evocan dicho estado emocional y, a través de conexiones semánticas, descubre canciones relacionadas que comparten dimensiones emocionales afines. Ejemplo: *"Recomiéndame música melancólica"*.

Cada tipo de consulta produce una lista ordenada de recomendaciones donde cada ítem incluye: el nodo recomendado, una puntuación de relevancia semántica calculada mediante la fórmula de puntuación del motor de inferencia, y una explicación trazable basada en los caminos semánticos que justifican la recomendación. La interfaz de interacción es una línea de comandos (CLI) que permite al usuario ingresar consultas en texto natural y recibir recomendaciones formateadas con sus explicaciones correspondientes.


## 6.2 Limitaciones del Proyecto

El proyecto presenta limitaciones inherentes a su naturaleza de prototipo de investigación académica, las cuales se identifican y documentan explícitamente para establecer expectativas realistas sobre el alcance de la contribución y para orientar posibles líneas de trabajo futuro.

### 6.2.1 Tamaño acotado de la base de conocimiento frente a catálogos reales

La base de conocimiento del prototipo contiene 100 nodos y 360 arcos, cifras que representan una fracción mínima de los catálogos musicales reales. Spotify, por ejemplo, supera los 100 millones de pistas disponibles, lo que implica que la base de conocimiento del prototipo cubre aproximadamente el 0.000023% de un catálogo comercial. Esta diferencia de escala tiene implicaciones directas:

- **Cobertura limitada del dominio**: La base de conocimiento no puede representar la totalidad de géneros, subgéneros, artistas, épocas e instrumentos que conforman el universo musical. Las recomendaciones generadas están necesariamente restringidas al subconjunto de entidades incluidas en la red.
- **Densidad relacional artificial**: En una red de 100 nodos, la densidad de conexiones es significativamente mayor que la que existiría en una red de millones de nodos, lo que puede producir caminos semánticos más cortos y puntuaciones de relevancia más altas de las que se observarían en un sistema a escala real.
- **Ausencia de evaluación de escalabilidad**: El rendimiento computacional del motor de inferencia BFS ponderado no ha sido evaluado en redes de gran escala. Si bien el algoritmo es eficiente para redes pequeñas, su comportamiento en redes con millones de nodos y arcos requeriría optimizaciones adicionales (indexación, particionamiento, caching) que exceden el alcance del presente proyecto.

No obstante, el tamaño de la base de conocimiento es suficiente para demostrar la viabilidad del enfoque propuesto — que la inferencia semántica sobre una red de conocimiento musical produce recomendaciones diversas, explicables y fundamentadas en caminos semánticos trazables — y para verificar las propiedades de correctitud definidas en el diseño técnico.

### 6.2.2 Ausencia de aprendizaje automático para actualización dinámica de la red semántica

El agente inteligente desarrollado en este proyecto se clasifica como un **agente basado en conocimiento** según la taxonomía del Capítulo 2 del libro de referencia (Russell & Norvig, 2010): mantiene una representación interna del mundo (la red semántica) y razona sobre ella para tomar decisiones (inferencia semántica), pero **no aprende de forma autónoma**. Esta limitación se manifiesta en varios aspectos:

- **Base de conocimiento estática**: La red semántica no se actualiza automáticamente a partir de nuevas fuentes de datos, interacciones de usuarios o cambios en el dominio musical. La incorporación de nuevas entidades y relaciones requiere intervención manual del administrador del sistema.
- **Ausencia de refinamiento de pesos**: Los pesos de las relaciones semánticas se asignan manualmente durante la construcción de la base de conocimiento y permanecen fijos durante la operación del agente. Un sistema más avanzado podría ajustar estos pesos dinámicamente en función de la retroalimentación de los usuarios o de métricas de relevancia observadas.
- **Sin personalización por usuario**: El agente genera las mismas recomendaciones para una consulta dada independientemente del usuario que la realice. No existe un modelo de usuario que permita personalizar las recomendaciones en función de preferencias individuales acumuladas a lo largo del tiempo.
- **Sin adquisición automática de conocimiento**: La construcción de la red semántica se realiza de forma manual y curada. Un sistema de producción requeriría mecanismos de extracción automática de conocimiento a partir de fuentes como bases de datos musicales (MusicBrainz, Discogs), APIs de plataformas de streaming, y técnicas de procesamiento de lenguaje natural aplicadas a reseñas y artículos musicales.

Esta limitación es consistente con el alcance del proyecto, que se centra en demostrar la viabilidad de la inferencia semántica como mecanismo de recomendación, no en desarrollar un sistema de aprendizaje automático completo. La integración de técnicas de aprendizaje para la actualización dinámica de la red constituye una línea de trabajo futuro natural.

### 6.2.3 Evaluación con un grupo reducido de usuarios

La evaluación del prototipo se realiza mediante una combinación de métricas cuantitativas automatizadas y evaluación cualitativa con un grupo reducido de usuarios. Esta estrategia de evaluación presenta limitaciones inherentes:

- **Tamaño de la muestra**: La evaluación cualitativa se realiza con un grupo reducido de usuarios, lo que limita la generalización estadística de los resultados. Las percepciones de un grupo pequeño pueden no ser representativas de la población general de usuarios de plataformas de streaming musical.
- **Sesgo de selección**: Los participantes en la evaluación son típicamente personas del entorno académico del investigador, lo que puede introducir sesgos en términos de conocimiento musical, familiaridad con sistemas de recomendación y expectativas sobre la calidad de las sugerencias.
- **Ausencia de comparación directa con sistemas comerciales**: La evaluación no incluye una comparación directa con los algoritmos de recomendación de plataformas comerciales (Spotify, Apple Music), ya que estos sistemas operan sobre catálogos y bases de usuarios de magnitudes incomparables. La comparación se realiza a nivel conceptual, contrastando las propiedades del enfoque de redes semánticas con las limitaciones documentadas en la literatura para los enfoques de filtrado colaborativo y basado en contenido.
- **Métricas limitadas**: Las métricas cuantitativas (precision@k, recall@k) se calculan sobre un conjunto de prueba definido por el investigador, lo que introduce un componente de subjetividad en la definición de las recomendaciones "correctas" o "esperadas".

A pesar de estas limitaciones, la estrategia de evaluación es adecuada para un prototipo de investigación académica y permite verificar las hipótesis fundamentales del proyecto: que la inferencia semántica produce recomendaciones explicables y que los caminos semánticos proporcionan justificaciones comprensibles para el usuario.


## 6.3 Entregables del Proyecto

El proyecto produce dos entregables principales, cada uno con criterios de completitud y calidad definidos:

### 6.3.1 Documento de investigación

Un documento académico que sigue la estructura requerida por las reglas del proyecto de maestría, incluyendo las siguientes secciones:

1. **Introducción** — Contextualización del problema y presentación del proyecto.
2. **Planteamiento del problema** — Descripción de la sobrecarga de información en plataformas de streaming musical, análisis de las limitaciones del filtrado colaborativo y del filtrado basado en contenido, y formulación del problema central.
3. **Justificación** — Argumentación de las ventajas de las redes semánticas, evidencia de aplicabilidad en dominios de recomendación, y comparación con otras técnicas de representación del conocimiento.
4. **Objetivos** — Objetivo general y objetivos específicos con trazabilidad a las preguntas de investigación.
5. **Marco teórico** — Fundamentación en los conceptos de agente inteligente (Capítulo 2) y representación del conocimiento (Capítulo 10) del libro de referencia.
6. **Estado del arte** — Análisis de trabajos relacionados, tabla comparativa e identificación de la brecha de investigación.
7. **Propuesta de solución** — Diseño del agente inteligente basado en redes semánticas.
8. **Implementación** — Descripción técnica del prototipo funcional.
9. **Evaluación** — Resultados cuantitativos y cualitativos de la evaluación del agente.
10. **Conclusiones** — Síntesis de hallazgos, contribuciones y trabajo futuro.
11. **Referencias** — Bibliografía completa en formato APA, incluyendo los ocho papers de referencia y los capítulos del libro de texto.

El documento incluye un glosario de términos técnicos de Inteligencia Artificial y redes semánticas, y cumple con el requisito de utilizar fuentes académicas verificables (journals, conferencias, libros de texto).

### 6.3.2 Prototipo funcional del agente inteligente

Un prototipo de software implementado en Python que materializa el diseño del agente inteligente basado en redes semánticas. El prototipo se compone de los siguientes módulos:

- **Red semántica** (`src/models/semantic_network.py`): Estructura de datos del grafo con operaciones de adición, consulta, búsqueda de caminos, serialización y deserialización.
- **Modelos de datos** (`src/models/data_models.py`, `src/models/enums.py`): Definición de tipos de nodos, tipos de relaciones, y estructuras de datos para nodos, arcos, recomendaciones, explicaciones y caminos semánticos.
- **Motor de inferencia** (`src/engine/inference_engine.py`): Implementación del algoritmo BFS ponderado para inferencia semántica, cálculo de distancia semántica, búsqueda de caminos y generación de explicaciones.
- **Motor de recomendación** (`src/engine/recommendation_engine.py`): Orquestación de consultas de recomendación por canción, artista, género y estado de ánimo, con integración de puntuación y explicaciones.
- **Constructor de base de conocimiento** (`src/knowledge/knowledge_builder.py`): Carga, exportación y validación de la base de conocimiento desde formato JSON.
- **Interfaz CLI** (`src/cli/agent_cli.py`): Interfaz de línea de comandos para interacción con el agente, con soporte para los cuatro tipos de consulta y formateo de recomendaciones con explicaciones.
- **Base de conocimiento** (`data/music_knowledge_base.json`): Archivo JSON con 100 nodos y 360 arcos que representa el dominio musical cubierto.

El prototipo se acompaña de una suite de tests que incluye tests unitarios (pytest) y tests de propiedades (hypothesis) que verifican las propiedades de correctitud definidas en el diseño técnico: viaje de ida y vuelta de serialización, descubrimiento de conexiones indirectas, consistencia de puntuación, validez de explicaciones, simetría de distancia semántica y detección de referencias inválidas.


## 6.4 Metodología de Desarrollo

La metodología de desarrollo del proyecto se alinea con las reglas del documento de proyecto de maestría y combina un enfoque de **investigación aplicada** con un componente de **desarrollo de software** estructurado.

### 6.4.1 Enfoque de investigación aplicada

El proyecto sigue un enfoque de investigación aplicada que parte de un problema identificado en la literatura (las limitaciones de los enfoques tradicionales de recomendación musical) y propone una solución fundamentada en técnicas de Inteligencia Artificial (redes semánticas e inferencia semántica). El proceso de investigación comprende:

1. **Revisión de la literatura**: Análisis sistemático de los ocho papers de referencia y los capítulos del libro de texto, identificando el estado del arte, las contribuciones existentes y la brecha de investigación.
2. **Formulación del problema y objetivos**: Definición del problema central, preguntas de investigación y objetivos alineados con la brecha identificada.
3. **Diseño de la solución**: Especificación técnica del agente inteligente, incluyendo la arquitectura del sistema, los modelos de datos, los algoritmos de inferencia y las interfaces de los componentes.
4. **Implementación del prototipo**: Desarrollo del software siguiendo el diseño especificado, con verificación incremental mediante tests unitarios y de propiedades.
5. **Evaluación**: Verificación empírica de que el prototipo cumple los objetivos planteados, mediante métricas cuantitativas y evaluación cualitativa.
6. **Documentación**: Redacción del documento de investigación con la estructura requerida por las reglas del proyecto.

### 6.4.2 Desarrollo de software dirigido por especificación

El componente de desarrollo de software del proyecto sigue un enfoque **dirigido por especificación** (*spec-driven development*) que garantiza la trazabilidad entre los requisitos del proyecto, el diseño técnico y la implementación:

- **Requisitos formales**: Los requisitos del proyecto se documentan en un formato estructurado con historias de usuario y criterios de aceptación verificables, organizados en siete áreas: planteamiento del problema, justificación, preguntas de investigación, objetivos, estado del arte, alcance y limitaciones, y estructura del documento.
- **Diseño técnico**: El diseño del prototipo se especifica formalmente, incluyendo interfaces de componentes, modelos de datos, algoritmos, propiedades de correctitud y estrategia de testing.
- **Implementación incremental**: El desarrollo se organiza en tareas incrementales donde cada tarea construye sobre las anteriores, con checkpoints de verificación que aseguran la integridad del sistema en cada etapa.
- **Verificación mediante tests**: Cada componente se verifica mediante tests unitarios (ejemplos específicos y casos borde) y tests de propiedades (propiedades universales verificadas con entradas generadas aleatoriamente mediante la biblioteca hypothesis), asegurando que la implementación cumple con las especificaciones del diseño.

### 6.4.3 Herramientas y tecnologías

El prototipo se desarrolla utilizando las siguientes herramientas y tecnologías:

| Herramienta | Propósito |
|---|---|
| **Python** | Lenguaje de implementación del prototipo |
| **pytest** | Framework de testing unitario |
| **hypothesis** | Biblioteca de testing basado en propiedades |
| **JSON** | Formato de almacenamiento de la base de conocimiento |
| **Estructura de grafo propia** | Implementación de la red semántica mediante diccionarios de adyacencia, sin dependencia de bibliotecas externas de grafos |

La elección de Python como lenguaje de implementación responde a su amplia adopción en proyectos de Inteligencia Artificial, la disponibilidad de bibliotecas de testing maduras, y su adecuación para el desarrollo de prototipos académicos. La implementación de la red semántica mediante una estructura de grafo propia (en lugar de utilizar bibliotecas como NetworkX) permite un control total sobre la representación de nodos tipados, arcos ponderados y relaciones semánticas específicas del dominio musical.

---

## Referencias

Bani Younes, F., Boudhir, A. A., & Agnaou, M. (2018). A semantic network approach to movie recommendation. *International Journal of Computer Applications*, *182*(15), 1–6.

Li, H., Li, Y., & Zhang, M. (2016). Music recommendation based on semantic network. *Proceedings of the International Conference on Computer Science and Network Technology*, 356–360.

Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3ra ed.). Pearson.

Tang, F., Mu, W., Zhang, M., & Liang, S. (2017). Knowledge representation in semantic networks for organizations. *International Journal of Knowledge Engineering*, *3*(1), 15–21.

Wang, M., Liu, X., & Chen, H. (2019). Knowledge representation in semantic networks for healthcare. *Journal of Biomedical Informatics*, *92*, 103–115.

Zhang, J., Wang, Y., & Chen, L. (2019). Product recommendation using semantic networks. *Journal of Intelligent Information Systems*, *52*(2), 285–308.
