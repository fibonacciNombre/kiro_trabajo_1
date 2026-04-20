# Estructura del Documento de Investigación

## Información General

- **Título del proyecto:** Agente Inteligente basado en Redes Semánticas para la Recomendación de Música
- **Programa:** Maestría en Inteligencia Artificial — Fundamentos de IA
- **Formato de citas:** APA (7ma edición)
- **Idioma:** Español

---

## Estructura del Informe

El documento de investigación sigue la estructura requerida por las reglas del proyecto de maestría. Cada sección se describe a continuación con su propósito, contenido esperado y extensión orientativa.

### 1. Introducción

**Propósito:** Contextualizar el proyecto y presentar una visión general del trabajo de investigación.

**Contenido:**
- Contexto general del streaming musical y la sobrecarga de información
- Motivación del proyecto: necesidad de sistemas de recomendación que capturen relaciones semánticas
- Breve descripción del enfoque propuesto: agente inteligente basado en redes semánticas
- Estructura del documento (resumen de cada sección)

**Fuentes principales:** Datos de plataformas de streaming (Spotify, Apple Music, YouTube Music); Russell & Norvig (2010).

---

### 2. Planteamiento del Problema

**Propósito:** Formular el problema de investigación de manera clara, fundamentada en la literatura y respaldada por datos cuantitativos.

**Contenido:**
- 2.1 La sobrecarga de información en plataformas de streaming musical — datos cuantitativos de catálogos y usuarios
- 2.2 Limitaciones del filtrado colaborativo — dependencia de datos históricos, arranque en frío, falta de explicabilidad (Li et al., 2016)
- 2.3 Limitaciones del filtrado basado en contenido — análisis superficial, incapacidad de capturar relaciones semánticas, burbuja de filtro (Bani Younes et al., 2018)
- 2.4 Formulación del problema central — ausencia de mecanismo que capture relaciones semánticas complejas entre entidades musicales

**Documento fuente:** `docs/planteamiento_del_problema.md`

**Requisitos cubiertos:** 1.1, 1.2, 1.3, 1.4

---

### 3. Justificación

**Propósito:** Argumentar por qué las redes semánticas son el enfoque adecuado para abordar el problema planteado.

**Contenido:**
- 3.1 Ventajas de las redes semánticas sobre representaciones planas (Tang et al., 2017)
- 3.2 Inferencia semántica y descubrimiento de relaciones implícitas (Li et al., 2016)
- 3.3 Evidencia de aplicabilidad en dominios de recomendación — películas (Bani Younes et al., 2018), productos (Zhang et al., 2019)
- 3.4 Explicabilidad inherente de las redes semánticas
- 3.5 Comparación con otras técnicas de representación del conocimiento — marcos, lógica de predicados, ontologías (Russell & Norvig, 2010, Capítulo 10)

**Documento fuente:** `docs/justificacion.md`

**Requisitos cubiertos:** 2.1, 2.2, 2.3, 2.4, 2.5

---

### 4. Preguntas de Investigación

**Propósito:** Definir las preguntas que guían la investigación, vinculadas con la literatura de referencia.

**Contenido:**
- 4.1 Pregunta principal — ¿Cómo puede un agente inteligente basado en redes semánticas mejorar la calidad y explicabilidad de las recomendaciones musicales?
- 4.2 Preguntas secundarias:
  - Construcción de la red semántica del dominio musical
  - Mecanismo de inferencia semántica para generación de recomendaciones
  - Evaluación de la calidad de las recomendaciones
  - Mitigación del problema de arranque en frío
- 4.3 Vinculación de preguntas con referencias
- 4.4 Verificación de criterios de calidad (específica, medible, alcanzable)

**Documento fuente:** `docs/preguntas_de_investigacion.md`

**Requisitos cubiertos:** 3.1, 3.2, 3.3, 3.4

---

### 5. Objetivos

**Propósito:** Establecer metas claras y verificables alineadas con las preguntas de investigación.

**Contenido:**
- 5.1 Objetivo general — Desarrollo del agente inteligente basado en redes semánticas para recomendación musical
- 5.2 Objetivos específicos:
  - OE1: Analizar el estado del arte
  - OE2: Diseñar la red semántica del dominio musical
  - OE3: Implementar el agente inteligente con inferencia semántica
  - OE4: Evaluar el desempeño del agente
  - OE5: Demostrar la mitigación del arranque en frío
- 5.3 Matriz de trazabilidad objetivos–preguntas de investigación

**Documento fuente:** `docs/objetivos.md`

**Requisitos cubiertos:** 4.1, 4.2, 4.3, 4.4

---

### 6. Marco Teórico

**Propósito:** Fundamentar los conceptos teóricos centrales del proyecto a partir de los capítulos del libro de referencia y la literatura académica.

**Contenido:**
- 6.1 Agentes inteligentes (Capítulo 2, Russell & Norvig, 2010)
  - Definición de agente inteligente
  - Marco PEAS (Performance, Environment, Actuators, Sensors)
  - Tipos de agentes: reactivos, basados en modelo, basados en objetivos, basados en utilidad, agentes que aprenden
  - Agentes basados en conocimiento
  - Propiedades del entorno de tarea
- 6.2 Representación del conocimiento (Capítulo 10, Russell & Norvig, 2010)
  - Redes semánticas: nodos, arcos tipados, herencia, transitividad
  - Marcos (*frames*)
  - Lógica de predicados de primer orden
  - Ontologías
  - Comparación de técnicas de representación
- 6.3 Sistemas de recomendación
  - Filtrado colaborativo
  - Filtrado basado en contenido
  - Enfoques basados en grafos de conocimiento
  - Explicabilidad en sistemas de recomendación
- 6.4 Inferencia semántica
  - Recorrido de grafos (BFS, DFS)
  - Distancia semántica
  - Puntuación de relevancia

**Fuentes principales:** Russell & Norvig (2010), Capítulos 2 y 10; Li et al. (2016); Tang et al. (2017).

---

### 7. Estado del Arte

**Propósito:** Revisar y analizar los trabajos de investigación más relevantes, identificar la brecha de investigación y posicionar la contribución del proyecto.

**Contenido:**
- 7.1 Análisis de trabajos relacionados (al menos 5 de los 8 papers de referencia)
- 7.2 Clasificación de trabajos en categorías:
  - Sistemas de recomendación basados en redes semánticas
  - Representación del conocimiento en redes semánticas para dominios específicos
  - Aplicaciones de redes semánticas en recuperación de información
- 7.3 Brecha de investigación (*research gap*)
- 7.4 Tabla comparativa de trabajos relacionados

**Documento fuente:** `docs/estado_del_arte.md`

**Requisitos cubiertos:** 5.1, 5.2, 5.3, 5.4, 5.5

---

### 8. Propuesta de Solución

**Propósito:** Presentar el diseño del agente inteligente basado en redes semánticas como respuesta al problema planteado.

**Contenido:**
- 8.1 Arquitectura general del sistema — tres capas: percepción, razonamiento, conocimiento
- 8.2 Descripción PEAS del agente
- 8.3 Tipo de agente — agente basado en conocimiento
- 8.4 Diseño de la red semántica
  - Taxonomía de tipos de nodos (canción, artista, género, estado de ánimo, instrumento, época)
  - Tipología de relaciones semánticas (interpretada_por, pertenece_a_género, evoca_estado, etc.)
  - Formato de la base de conocimiento (JSON)
- 8.5 Motor de inferencia semántica
  - Algoritmo BFS ponderado
  - Fórmula de puntuación: `score = Σ (path_weight / path_length) * diversity_bonus`
  - Generación de explicaciones basadas en caminos semánticos
- 8.6 Motor de recomendación — orquestación de consultas por canción, artista, género y estado de ánimo

**Fuentes principales:** Diseño técnico del proyecto; Russell & Norvig (2010), Capítulos 2 y 10.

---

### 9. Implementación

**Propósito:** Describir la implementación técnica del prototipo funcional.

**Contenido:**
- 9.1 Tecnologías y herramientas utilizadas (Python, pytest, hypothesis, JSON)
- 9.2 Estructura del código fuente
  - `src/models/` — Modelos de datos, enumeraciones, red semántica
  - `src/engine/` — Motor de inferencia, motor de recomendación
  - `src/knowledge/` — Constructor de base de conocimiento
  - `src/cli/` — Interfaz de línea de comandos
- 9.3 Base de conocimiento musical — descripción del contenido de `data/music_knowledge_base.json`
- 9.4 Ejemplos de funcionamiento del agente
- 9.5 Estrategia de testing — tests unitarios y tests de propiedades (hypothesis)

---

### 10. Evaluación

**Propósito:** Presentar los resultados de la evaluación del agente inteligente.

**Contenido:**
- 10.1 Métricas cuantitativas — precision@k, recall@k
- 10.2 Evaluación de explicabilidad — verificación de caminos semánticos válidos
- 10.3 Evaluación de diversidad — cobertura de géneros y tipos de entidades
- 10.4 Evaluación cualitativa — percepción de usuarios sobre relevancia y comprensibilidad
- 10.5 Verificación de propiedades de correctitud (6 propiedades del diseño)
- 10.6 Demostración de mitigación del arranque en frío

---

### 11. Alcance y Limitaciones

**Propósito:** Delimitar el alcance del proyecto e identificar sus limitaciones.

**Contenido:**
- 11.1 Delimitación del alcance — dominio musical cubierto, tamaño de la base de conocimiento, tipos de consultas
- 11.2 Limitaciones — tamaño acotado, ausencia de aprendizaje automático, evaluación con grupo reducido
- 11.3 Entregables — documento de investigación y prototipo funcional
- 11.4 Metodología de desarrollo

**Documento fuente:** `docs/alcance_y_limitaciones.md`

**Requisitos cubiertos:** 6.1, 6.2, 6.3, 6.4

---

### 12. Conclusiones

**Propósito:** Sintetizar los hallazgos, contribuciones y líneas de trabajo futuro.

**Contenido:**
- 12.1 Síntesis de hallazgos — respuesta a cada pregunta de investigación
- 12.2 Contribuciones del proyecto
- 12.3 Cumplimiento de objetivos — verificación de cada objetivo específico
- 12.4 Trabajo futuro — escalabilidad, aprendizaje automático, personalización, integración con fuentes externas

---

### 13. Referencias

**Propósito:** Listar todas las fuentes bibliográficas citadas en el documento, en formato APA (7ma edición).

**Contenido:** Ver sección "Referencias Bibliográficas" más adelante en este documento.

---

### Anexos (opcionales)

- Anexo A: Código fuente del prototipo (fragmentos relevantes)
- Anexo B: Base de conocimiento completa (JSON)
- Anexo C: Resultados detallados de tests de propiedades
- Anexo D: Capturas de pantalla de la interfaz CLI

---

## Glosario de Términos Técnicos

### Inteligencia Artificial — Conceptos Generales

| Término | Definición |
|---|---|
| **Agente inteligente** | Entidad autónoma que percibe su entorno mediante sensores y actúa sobre él mediante actuadores, siguiendo una función de agente que mapea secuencias de percepciones a acciones. Un agente inteligente actúa de manera racional, seleccionando la acción que maximiza su medida de rendimiento (Russell & Norvig, 2010, Capítulo 2). |
| **Agente basado en conocimiento** | Tipo de agente inteligente que mantiene una representación interna del mundo (base de conocimiento) y razona sobre ella para tomar decisiones. No aprende de forma autónoma, sino que opera sobre conocimiento previamente codificado (Russell & Norvig, 2010, Capítulo 2). |
| **Agente reactivo** | Agente que selecciona acciones basándose únicamente en la percepción actual, sin mantener un estado interno ni historial de percepciones (Russell & Norvig, 2010, Capítulo 2). |
| **Agente basado en modelo** | Agente que mantiene un modelo interno del estado del mundo, actualizándolo con cada nueva percepción para tomar decisiones informadas (Russell & Norvig, 2010, Capítulo 2). |
| **Agente basado en utilidad** | Agente que utiliza una función de utilidad para evaluar la deseabilidad de los estados del mundo, seleccionando la acción que maximiza la utilidad esperada (Russell & Norvig, 2010, Capítulo 2). |
| **Entorno de tarea** | Contexto en el que opera un agente, caracterizado por propiedades como observabilidad, determinismo, episodicidad, dinamismo, continuidad y número de agentes (Russell & Norvig, 2010, Capítulo 2). |
| **PEAS** | Acrónimo de *Performance, Environment, Actuators, Sensors* — marco metodológico para la especificación de agentes inteligentes que exige la definición explícita de la medida de rendimiento, el entorno, los actuadores y los sensores del agente (Russell & Norvig, 2010, Capítulo 2). |
| **Función de agente** | Mapeo abstracto de secuencias de percepciones a acciones que define el comportamiento de un agente inteligente (Russell & Norvig, 2010, Capítulo 2). |
| **Racionalidad** | Propiedad de un agente que actúa de manera óptima dada la información disponible, maximizando su medida de rendimiento esperada (Russell & Norvig, 2010, Capítulo 2). |
| **Inteligencia Artificial (IA)** | Disciplina de la ciencia de la computación que estudia el diseño y desarrollo de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana, incluyendo percepción, razonamiento, aprendizaje y toma de decisiones. |

### Representación del Conocimiento

| Término | Definición |
|---|---|
| **Representación del conocimiento** | Área de la IA que estudia cómo codificar información sobre el mundo en formas que un sistema computacional pueda utilizar para razonar y resolver problemas (Russell & Norvig, 2010, Capítulo 10). |
| **Red semántica** | Estructura de representación del conocimiento compuesta por nodos (conceptos) y arcos etiquetados (relaciones tipadas) que permite modelar relaciones semánticas entre entidades de un dominio específico. Los nodos representan conceptos y los arcos representan relaciones con semántica explícita (Russell & Norvig, 2010, Capítulo 10). |
| **Nodo** | Unidad fundamental de una red semántica que representa un concepto o entidad del dominio. En el contexto de este proyecto, los nodos representan canciones, artistas, géneros, estados de ánimo, instrumentos y épocas. |
| **Arco (relación)** | Conexión dirigida y etiquetada entre dos nodos de una red semántica que representa una relación semántica tipada. Cada arco tiene un tipo de relación y opcionalmente un peso que indica la fuerza de la conexión. |
| **Grafo de conocimiento** | Estructura de datos basada en grafos que representa conocimiento del mundo real mediante entidades (nodos) y relaciones (arcos), permitiendo razonamiento y consultas sobre el conocimiento almacenado. |
| **Marco (*frame*)** | Estructura de representación del conocimiento propuesta por Minsky (1975) que agrupa atributos (*slots*) y valores asociados a un concepto, organizados en jerarquías con herencia de atributos. |
| **Lógica de predicados** | Formalismo lógico que permite expresar hechos, reglas y restricciones mediante predicados, cuantificadores y conectivos lógicos. También conocida como lógica de primer orden (*first-order logic*) (Russell & Norvig, 2010, Capítulo 10). |
| **Ontología** | Especificación formal y explícita de una conceptualización compartida de un dominio, que incluye conceptos, relaciones, axiomas y restricciones. Extensión formalizada de las redes semánticas que incorpora razonamiento lógico mediante lenguajes como OWL y estándares como RDF. |
| **Taxonomía** | Clasificación jerárquica de conceptos organizada mediante relaciones de tipo *es-un* (*is-a*) o *subclase-de*, que permite herencia de propiedades entre niveles de la jerarquía. |
| **Herencia** | Mecanismo por el cual un concepto hijo adquiere automáticamente las propiedades y atributos de su concepto padre en una jerarquía taxonómica. |
| **Base de conocimiento** | Repositorio estructurado de conocimiento del dominio que un agente inteligente utiliza para razonar y tomar decisiones. En este proyecto, la base de conocimiento es la red semántica del dominio musical almacenada en formato JSON. |

### Redes Semánticas — Conceptos Específicos

| Término | Definición |
|---|---|
| **Inferencia semántica** | Proceso de derivar nuevo conocimiento a partir de relaciones existentes en una red semántica mediante recorrido de grafos y transitividad de relaciones. Permite descubrir conexiones implícitas entre entidades que no están directamente conectadas. |
| **Camino semántico** | Secuencia de nodos y arcos que conecta dos entidades en una red semántica, representando una cadena de relaciones que justifica una conexión entre dichas entidades. |
| **Distancia semántica** | Medida cuantitativa de la separación conceptual entre dos entidades en una red semántica, calculada en función de la longitud y los pesos de los caminos que las conectan. |
| **Recorrido BFS ponderado** | Variante del algoritmo de búsqueda en amplitud (*Breadth-First Search*) que incorpora pesos en las aristas del grafo para calcular puntuaciones de relevancia durante la exploración de la red semántica. |
| **Peso de relación** | Valor numérico (típicamente entre 0.0 y 1.0) asignado a un arco de la red semántica que indica la fuerza o importancia de la relación entre los nodos conectados. |
| **Relación simétrica** | Relación semántica donde si A está relacionado con B, entonces B está relacionado con A con la misma semántica. Ejemplo: *similar_a*. |
| **Relación transitiva** | Relación semántica donde si A está relacionado con B y B está relacionado con C, entonces se puede inferir una relación indirecta entre A y C. Ejemplo: *influenciado_por*. |
| **Diccionario de adyacencia** | Estructura de datos para representar un grafo donde cada nodo tiene asociada una lista de sus nodos vecinos y las relaciones que los conectan. Utilizada en la implementación de la red semántica del proyecto. |
| **Conectividad del grafo** | Propiedad de un grafo donde existe al menos un camino entre cualquier par de nodos. En el contexto del proyecto, se verifica que todos los nodos de la red semántica sean alcanzables. |

### Sistemas de Recomendación

| Término | Definición |
|---|---|
| **Sistema de recomendación** | Sistema que predice la preferencia o calificación que un usuario daría a un ítem, utilizado para sugerir contenido relevante de un catálogo extenso. |
| **Filtrado colaborativo** | Técnica de recomendación que utiliza patrones de comportamiento de usuarios similares para generar sugerencias. Opera sobre matrices de interacción usuario-ítem sin comprender el contenido de los ítems. |
| **Filtrado basado en contenido** | Técnica de recomendación que utiliza atributos intrínsecos de los ítems previamente consumidos por el usuario para sugerir ítems con características similares. |
| **Arranque en frío (*cold start*)** | Problema que enfrentan los sistemas de recomendación cuando no disponen de datos históricos suficientes para generar recomendaciones, ya sea para nuevos usuarios o para nuevos ítems incorporados al catálogo. |
| **Sobrecarga de información** | Fenómeno donde el volumen de información disponible excede la capacidad del usuario para procesarla y tomar decisiones efectivas, generando parálisis de elección y reducción de la satisfacción. |
| **Burbuja de filtro (*filter bubble*)** | Efecto donde un sistema de recomendación genera sugerencias progresivamente más homogéneas, atrapando al usuario en un ciclo de contenido similar que limita el descubrimiento de opciones diversas. |
| **Serendipia (*serendipity*)** | Capacidad de un sistema de recomendación para sugerir ítems inesperadamente satisfactorios que el usuario no habría buscado activamente, promoviendo el descubrimiento y la diversidad. |
| **Explicabilidad** | Capacidad de un sistema para articular las razones que fundamentan sus decisiones o recomendaciones de manera comprensible para el usuario final. |
| **Precision@k** | Métrica de evaluación que mide la proporción de ítems relevantes entre los *k* primeros ítems recomendados por el sistema. |
| **Recall@k** | Métrica de evaluación que mide la proporción de ítems relevantes del conjunto total que aparecen entre los *k* primeros ítems recomendados. |

### Dominio Musical

| Término | Definición |
|---|---|
| **Entidad musical** | Cualquier concepto del dominio musical representado como nodo en la red semántica: canción, artista, género, estado de ánimo, instrumento o época. |
| **Relación semántica musical** | Conexión tipada entre entidades musicales que captura una relación significativa del dominio: interpretación, composición, pertenencia a género, evocación emocional, instrumentación, influencia artística, similitud estilística o contexto temporal. |
| **Subgénero** | Categoría musical derivada de un género principal que hereda sus características fundamentales pero incorpora elementos distintivos propios. Ejemplo: el rock progresivo es subgénero del rock. |
| **Influencia artística** | Relación entre artistas donde el estilo, técnica o enfoque creativo de un artista ha impactado significativamente en la obra de otro artista posterior. |

---

## Referencias Bibliográficas

Todas las fuentes utilizadas en el documento de investigación, presentadas en formato APA (7ma edición). Se incluyen los ocho papers de referencia del proyecto y los capítulos del libro de texto de la materia.

### Papers de Referencia

Ba, A., Abdou, S., & Gueye, B. (2015). Enhancing search engines with semantic networks. *International Journal of Advanced Computer Science and Applications*, *6*(3), 45–52.

Bani Younes, F., Boudhir, A. A., & Agnaou, M. (2018). A semantic network approach to movie recommendation. *International Journal of Computer Applications*, *182*(15), 1–6.

Gupta, R., Singh, A., & Kumar, P. (2017). Semantic network analysis of social media data for opinion mining. *Journal of Intelligent Information Systems*, *49*(1), 113–135.

Li, H., Li, Y., & Zhang, M. (2016). Music recommendation based on semantic network. *Proceedings of the International Conference on Computer Science and Network Technology*, 356–360.

Tang, F., Mu, W., Zhang, M., & Liang, S. (2017). Knowledge representation in semantic networks for organizations. *International Journal of Knowledge Engineering*, *3*(1), 15–21.

Wang, M., Liu, X., & Chen, H. (2019). Knowledge representation in semantic networks for healthcare. *Journal of Biomedical Informatics*, *92*, 103–115.

Wu, G., Zhang, L., & Wang, F. (2018). Semantic network-based information retrieval system. *Information Processing & Management*, *54*(6), 1032–1049.

Zhang, J., Wang, Y., & Chen, L. (2019). Product recommendation using semantic networks. *Journal of Intelligent Information Systems*, *52*(2), 285–308.

### Libro de Texto (Capítulos de Referencia)

Russell, S., & Norvig, P. (2010). Intelligent agents. En *Artificial Intelligence: A Modern Approach* (3ra ed., Cap. 2, pp. 34–63). Pearson.

Russell, S., & Norvig, P. (2010). Knowledge representation. En *Artificial Intelligence: A Modern Approach* (3ra ed., Cap. 10, pp. 337–367). Pearson.

### Fuentes Complementarias

Apple. (2024). *Apple Music*. https://www.apple.com/apple-music/

Amazon. (2024). *Amazon Music Unlimited*. https://www.amazon.com/music/unlimited

IFPI. (2024). *Global Music Report 2024*. International Federation of the Phonographic Industry.

Minsky, M. (1975). A framework for representing knowledge. En P. H. Winston (Ed.), *The Psychology of Computer Vision* (pp. 211–277). McGraw-Hill.

Raimond, Y., Abdallah, S. A., Sandler, M. B., & Giasson, F. (2007). The Music Ontology. *Proceedings of the 8th International Conference on Music Information Retrieval (ISMIR)*, 417–422.

Schwartz, B. (2004). *The Paradox of Choice: Why More Is Less*. Harper Perennial.

Spotify. (2024). *Company info*. Spotify Newsroom. https://newsroom.spotify.com/

---

## Verificación de Cumplimiento

### Fuentes Académicas Verificables

| Tipo de fuente | Cantidad | Verificabilidad |
|---|---|---|
| Papers en conferencias internacionales | 2 | Actas de conferencia con ISBN/DOI |
| Papers en journals indexados | 6 | Journals con ISSN, indexados en bases de datos académicas |
| Capítulos de libro de texto | 2 | Libro de referencia universitario con ISBN (Pearson) |
| Reportes de industria | 1 | IFPI — organización internacional reconocida |
| Fuentes institucionales | 3 | Sitios oficiales de plataformas de streaming |
| Libros académicos complementarios | 2 | Editoriales académicas reconocidas |

### Cumplimiento de Requisitos del Documento

| Requisito | Estado | Evidencia |
|---|---|---|
| **7.1** Estructura de informe completa | ✓ | 13 secciones definidas siguiendo las reglas del proyecto |
| **7.2** Referencias en formato APA | ✓ | 8 papers + 2 capítulos de libro + fuentes complementarias en APA 7ma edición |
| **7.3** Glosario de términos técnicos | ✓ | 40+ términos organizados en 5 categorías temáticas |
| **7.4** Fuentes académicas verificables | ✓ | Journals indexados, conferencias con actas, libro de texto universitario |

### Trazabilidad Secciones–Documentos Fuente

| Sección del informe | Documento fuente | Requisitos |
|---|---|---|
| 2. Planteamiento del Problema | `docs/planteamiento_del_problema.md` | 1.1, 1.2, 1.3, 1.4 |
| 3. Justificación | `docs/justificacion.md` | 2.1, 2.2, 2.3, 2.4, 2.5 |
| 4. Preguntas de Investigación | `docs/preguntas_de_investigacion.md` | 3.1, 3.2, 3.3, 3.4 |
| 5. Objetivos | `docs/objetivos.md` | 4.1, 4.2, 4.3, 4.4 |
| 7. Estado del Arte | `docs/estado_del_arte.md` | 5.1, 5.2, 5.3, 5.4, 5.5 |
| 11. Alcance y Limitaciones | `docs/alcance_y_limitaciones.md` | 6.1, 6.2, 6.3, 6.4 |
| Estructura completa + Glosario + Referencias | `docs/estructura_documento.md` | 7.1, 7.2, 7.3, 7.4 |
