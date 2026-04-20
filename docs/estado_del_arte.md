# Estado del Arte

## 5.1 Análisis de Trabajos Relacionados

La presente sección analiza los trabajos de investigación más relevantes en las áreas de sistemas de recomendación basados en redes semánticas, representación del conocimiento y recuperación de información semántica. Para cada trabajo se examina el problema abordado, la técnica utilizada, los resultados obtenidos y las limitaciones identificadas, con el objetivo de posicionar la contribución del presente proyecto en el contexto de la literatura existente.

### 5.1.1 H. Li, Y. Li y M. Zhang (2016) — *Music Recommendation Based on Semantic Network*

**Problema abordado.** Li et al. (2016) abordan el problema de la recomendación musical en escenarios donde los enfoques tradicionales de filtrado colaborativo presentan limitaciones significativas: dependencia de datos históricos de interacción de usuarios, problema de arranque en frío (*cold start*) para nuevos usuarios y nuevos ítems, y ausencia de explicabilidad en las recomendaciones generadas. Los autores argumentan que el dominio musical posee una estructura relacional rica que los enfoques basados en patrones de co-consumo no pueden capturar ni explotar.

**Técnica utilizada.** Los autores proponen la construcción de una red semántica del dominio musical donde los nodos representan entidades musicales (canciones, artistas, géneros) y los arcos representan relaciones semánticas tipadas entre dichas entidades. Sobre esta red, implementan un mecanismo de inferencia basado en recorrido de grafos que permite descubrir conexiones implícitas entre entidades — por ejemplo, que dos canciones aparentemente disímiles comparten cadenas de influencias artísticas, instrumentos comunes o estados de ánimo compartidos. La puntuación de relevancia de cada recomendación se calcula en función de la distancia semántica y el peso acumulado de las relaciones en los caminos encontrados.

**Resultados obtenidos.** Li et al. (2016) demuestran que la inferencia semántica sobre la red de conocimiento musical produce recomendaciones más diversas y comprensibles que las generadas por filtrado colaborativo convencional. Los autores evidencian que el recorrido de caminos semánticos permite identificar conexiones no triviales entre entidades que los enfoques basados en patrones estadísticos de co-ocurrencia no pueden detectar. Además, cada recomendación puede ser explicada en términos del camino semántico que la justifica, proporcionando transparencia al usuario.

**Limitaciones identificadas.** El trabajo se centra en la demostración conceptual del enfoque sin abordar la escalabilidad a catálogos musicales de gran tamaño. La base de conocimiento utilizada es relativamente pequeña, y los autores no evalúan el rendimiento computacional del mecanismo de inferencia en redes de mayor escala. Adicionalmente, la construcción de la red semántica se realiza de forma manual, sin mecanismos automatizados de adquisición de conocimiento.

### 5.1.2 F. Bani Younes, A. A. Boudhir y M. Agnaou (2018) — *A Semantic Network Approach to Movie Recommendation*

**Problema abordado.** Bani Younes et al. (2018) abordan las limitaciones del filtrado basado en contenido en el dominio de la recomendación cinematográfica: análisis superficial de atributos, incapacidad de capturar relaciones semánticas profundas entre entidades del dominio, y tendencia a generar recomendaciones homogéneas que atrapan al usuario en una burbuja de filtro (*filter bubble*). Los autores argumentan que las representaciones planas basadas en vectores de características son inherentemente incapaces de modelar la riqueza relacional de dominios como el cine o la música.

**Técnica utilizada.** Los autores desarrollan un sistema de recomendación de películas basado en una red semántica que modela las relaciones entre películas, directores, actores, géneros cinematográficos y temáticas mediante un grafo de conocimiento con nodos y arcos tipados. El sistema explota estas relaciones para generar recomendaciones que trascienden la similitud superficial de atributos, identificando conexiones semánticas entre entidades de diferentes tipos.

**Resultados obtenidos.** Bani Younes et al. (2018) demuestran que el enfoque de redes semánticas supera a los sistemas de filtrado colaborativo y basado en contenido convencionales en tres dimensiones: (a) mayor precisión en las recomendaciones al explotar relaciones semánticas entre entidades cinematográficas; (b) capacidad de recomendación transversal entre géneros, al identificar conexiones no evidentes a través de directores, actores y temáticas compartidas; y (c) mitigación del problema de arranque en frío, ya que las nuevas películas pueden ser recomendadas inmediatamente al incorporarse a la red semántica con sus relaciones definidas, sin necesidad de acumular calificaciones de usuarios.

**Limitaciones identificadas.** El sistema no incorpora mecanismos de aprendizaje automático para la actualización dinámica de la red semántica. La evaluación se realiza sobre un conjunto de datos relativamente acotado, y los autores no abordan la integración con fuentes de datos externas para el enriquecimiento automático de la base de conocimiento. La transferibilidad directa de los resultados a otros dominios (como el musical) requiere validación empírica adicional.

### 5.1.3 F. Tang, W. Mu, M. Zhang y S. Liang (2017) — *Knowledge Representation in Semantic Networks for Organizations*

**Problema abordado.** Tang et al. (2017) abordan el problema de la representación del conocimiento organizacional, donde las estructuras de datos convencionales (bases de datos relacionales, documentos no estructurados) resultan insuficientes para capturar las relaciones complejas entre entidades de un dominio organizacional: personas, roles, competencias, proyectos y recursos. Los autores argumentan que la pérdida de información relacional en representaciones planas limita la capacidad de las organizaciones para explotar su conocimiento colectivo.

**Técnica utilizada.** Los autores proponen el uso de redes semánticas como estructura de representación del conocimiento, donde los nodos representan conceptos del dominio organizacional y los arcos representan relaciones semánticas tipadas entre dichos conceptos. La red permite modelar relaciones multi-tipo (jerárquicas, funcionales, de competencia), herencia de atributos a lo largo de jerarquías taxonómicas, y relaciones transitivas e indirectas que emergen de la estructura del grafo. Los autores demuestran que esta representación preserva la semántica del dominio de manera que las representaciones planas no pueden lograr.

**Resultados obtenidos.** Tang et al. (2017) demuestran que las redes semánticas permiten representar relaciones complejas entre entidades de un dominio mediante nodos y arcos tipados, superando las limitaciones de las representaciones planas basadas en vectores de características. Los autores evidencian que la estructura de grafo facilita el descubrimiento de relaciones implícitas entre entidades que no están directamente conectadas, y que la preservación de la semántica de las relaciones (distinguiendo, por ejemplo, entre relaciones jerárquicas y funcionales) permite razonamientos más sofisticados sobre el conocimiento del dominio.

**Limitaciones identificadas.** El trabajo se centra en el dominio organizacional y no aborda directamente la aplicación de redes semánticas a sistemas de recomendación. La evaluación es predominantemente cualitativa, sin métricas cuantitativas de rendimiento. Los autores no abordan la escalabilidad de la representación a dominios con un número muy elevado de entidades y relaciones.

### 5.1.4 J. Zhang, Y. Wang y L. Chen (2019) — *Product Recommendation Using Semantic Networks*

**Problema abordado.** Zhang et al. (2019) abordan el problema de la recomendación de productos en el comercio electrónico, donde los enfoques de filtrado colaborativo y basado en contenido presentan limitaciones en escenarios con datos de interacción escasos (*sparse data*). Los autores argumentan que las relaciones semánticas entre productos (complementariedad, sustitución, pertenencia a categoría, compatibilidad funcional) constituyen un conocimiento valioso que los enfoques tradicionales no representan ni explotan.

**Técnica utilizada.** Los autores desarrollan un sistema de recomendación basado en un grafo de conocimiento que modela las relaciones entre productos, categorías, marcas, atributos funcionales y perfiles de usuario. El sistema utiliza algoritmos de inferencia sobre el grafo para descubrir patrones de complementariedad y sustitución entre productos, generando recomendaciones que se fundamentan en relaciones semánticas verificables. Cada recomendación se acompaña de una explicación basada en el camino semántico que la justifica.

**Resultados obtenidos.** Zhang et al. (2019) demuestran que la inferencia sobre grafos de conocimiento mejora la precisión de las recomendaciones en comparación con enfoques de filtrado colaborativo y basado en contenido, particularmente en escenarios donde los datos de interacción de usuarios son escasos. Los autores evidencian que las relaciones semánticas entre productos capturan patrones de complementariedad y sustitución que los enfoques tradicionales no pueden modelar. Un hallazgo particularmente relevante es que la explicabilidad de las recomendaciones — fundamentada en caminos semánticos trazables — aumenta la tasa de aceptación por parte de los usuarios.

**Limitaciones identificadas.** El sistema requiere la construcción manual de la base de conocimiento de productos, lo que limita su escalabilidad a catálogos de gran tamaño. La evaluación se centra en métricas de precisión y no aborda en profundidad la diversidad de las recomendaciones. Los autores no exploran la transferibilidad del enfoque a dominios con estructuras relacionales diferentes al comercio electrónico.

### 5.1.5 G. Wu, L. Zhang y F. Wang (2018) — *Semantic Network-Based Information Retrieval System*

**Problema abordado.** Wu et al. (2018) abordan el problema de la recuperación de información en sistemas donde las consultas de los usuarios involucran conceptos semánticamente relacionados que los motores de búsqueda basados en palabras clave no pueden resolver adecuadamente. Los autores argumentan que la brecha semántica entre las consultas del usuario y los documentos indexados limita la relevancia de los resultados de búsqueda, particularmente cuando la información buscada está distribuida entre múltiples documentos conectados por relaciones conceptuales.

**Técnica utilizada.** Los autores desarrollan un sistema de recuperación de información que integra una red semántica como capa de conocimiento entre las consultas del usuario y el índice de documentos. La red semántica modela las relaciones entre conceptos del dominio, permitiendo expandir las consultas del usuario con términos semánticamente relacionados y reordenar los resultados en función de la proximidad semántica entre los conceptos de la consulta y los conceptos presentes en los documentos. El sistema utiliza algoritmos de recorrido de grafos para explorar relaciones multi-nivel entre conceptos.

**Resultados obtenidos.** Wu et al. (2018) demuestran que la integración de redes semánticas en el proceso de recuperación de información mejora significativamente la relevancia de los resultados al explotar relaciones multi-nivel entre conceptos. Los autores evidencian que la expansión semántica de consultas permite recuperar documentos relevantes que no contienen los términos exactos de la consulta original, y que el reordenamiento basado en proximidad semántica mejora la precisión de los resultados en comparación con enfoques basados exclusivamente en coincidencia de palabras clave.

**Limitaciones identificadas.** La construcción de la red semántica del dominio requiere un esfuerzo significativo de ingeniería del conocimiento. El sistema no incorpora mecanismos de aprendizaje para la actualización automática de la red. La evaluación se realiza sobre un dominio específico, y la generalización a otros dominios requiere la construcción de redes semánticas adicionales.

### 5.1.6 A. Ba, S. Abdou y B. Gueye (2015) — *Enhancing Search Engines with Semantic Networks*

**Problema abordado.** Ba et al. (2015) abordan el problema de la limitada capacidad de los motores de búsqueda convencionales para comprender la intención semántica detrás de las consultas de los usuarios. Los autores argumentan que los motores de búsqueda basados en coincidencia léxica no pueden resolver consultas que requieren comprensión de relaciones conceptuales, sinonimia, jerarquías de conceptos o asociaciones contextuales entre términos.

**Técnica utilizada.** Los autores proponen la integración de redes semánticas en motores de búsqueda para enriquecer el proceso de interpretación de consultas y recuperación de resultados. La red semántica modela relaciones entre conceptos del dominio (sinonimia, hiponimia, meronimia, asociación contextual), permitiendo al motor de búsqueda expandir las consultas con términos relacionados, desambiguar términos polisémicos y descubrir relaciones implícitas entre los conceptos de la consulta y los documentos indexados.

**Resultados obtenidos.** Ba et al. (2015) demuestran que la integración de redes semánticas en motores de búsqueda permite descubrir relaciones implícitas que mejoran la precisión de la recuperación de información. Los autores evidencian mejoras en la relevancia de los resultados, particularmente para consultas complejas que involucran múltiples conceptos relacionados. El enfoque permite superar las limitaciones de la coincidencia léxica al explotar la estructura relacional del conocimiento del dominio.

**Limitaciones identificadas.** El rendimiento del sistema depende de la calidad y completitud de la red semántica subyacente. La construcción y mantenimiento de la red requiere esfuerzo manual significativo. Los autores no abordan la escalabilidad del enfoque a dominios con vocabularios muy extensos ni la integración con técnicas de procesamiento de lenguaje natural para la construcción automática de la red.


## 5.2 Clasificación de Trabajos Relacionados

Los trabajos analizados se organizan en tres categorías temáticas que reflejan las dimensiones fundamentales del presente proyecto: sistemas de recomendación basados en redes semánticas, representación del conocimiento en redes semánticas para dominios específicos, y aplicaciones de redes semánticas en recuperación de información.

### 5.2.1 Sistemas de recomendación basados en redes semánticas

Esta categoría agrupa los trabajos que aplican redes semánticas directamente al problema de la recomendación de ítems, utilizando la estructura de grafo como fundamento para la generación de sugerencias.

**H. Li et al. (2016)** constituyen el antecedente más directo del presente proyecto, al proponer la aplicación de redes semánticas específicamente al dominio de la recomendación musical. Su contribución principal radica en demostrar que la inferencia semántica sobre un grafo de conocimiento musical permite descubrir conexiones implícitas entre entidades que los enfoques de filtrado colaborativo no pueden detectar, y que estas conexiones se traducen en recomendaciones más diversas y explicables.

**F. Bani Younes et al. (2018)** extienden la aplicación de redes semánticas al dominio cinematográfico, demostrando que el enfoque es transferible a dominios con estructuras relacionales análogas al musical. Su contribución principal es la evidencia empírica de que las redes semánticas superan a los enfoques tradicionales en precisión, capacidad de recomendación transversal entre géneros y mitigación del arranque en frío.

**J. Zhang et al. (2019)** aplican el enfoque al comercio electrónico, demostrando que los grafos de conocimiento mejoran la precisión de las recomendaciones en escenarios con datos escasos y que la explicabilidad basada en caminos semánticos aumenta la aceptación de las recomendaciones por parte de los usuarios.

La convergencia de resultados positivos en tres dominios distintos (música, cine, comercio electrónico) establece un patrón consistente: las redes semánticas constituyen un enfoque efectivo para la recomendación en dominios donde las entidades están interconectadas por relaciones tipadas y significativas.

### 5.2.2 Representación del conocimiento en redes semánticas para dominios específicos

Esta categoría agrupa los trabajos que se centran en la capacidad de las redes semánticas para representar conocimiento complejo en dominios específicos, proporcionando el fundamento teórico para la construcción de bases de conocimiento estructuradas.

**F. Tang et al. (2017)** abordan la representación del conocimiento organizacional, demostrando que las redes semánticas superan a las representaciones planas en la captura de relaciones complejas entre entidades. Su contribución principal es la fundamentación teórica de las ventajas de las redes semánticas sobre los vectores de características: representación multi-tipo, herencia jerárquica, relaciones transitivas y preservación de la semántica del dominio.

**M. Wang et al. (2019)**, aunque no analizado en detalle en la sección anterior, contribuyen al campo al demostrar la aplicabilidad de redes semánticas en el dominio de la salud, evidenciando que la representación semántica del conocimiento médico permite integrar nuevas entidades al sistema mediante la definición de sus relaciones con entidades preexistentes — un hallazgo directamente relevante para la mitigación del problema de arranque en frío en sistemas de recomendación.

**R. Gupta et al. (2017)**, igualmente, contribuyen al demostrar que el análisis de redes semánticas permite capturar relaciones contextuales en datos de redes sociales, evidenciando la versatilidad de las redes semánticas como herramienta de representación del conocimiento en dominios complejos con entidades interconectadas.

### 5.2.3 Aplicaciones de redes semánticas en recuperación de información

Esta categoría agrupa los trabajos que aplican redes semánticas al problema de la recuperación de información, proporcionando evidencia de la efectividad de la inferencia semántica para descubrir relaciones implícitas entre conceptos.

**G. Wu et al. (2018)** desarrollan un sistema de recuperación de información que integra una red semántica como capa de conocimiento, demostrando que la exploración de relaciones multi-nivel entre conceptos mejora significativamente la relevancia de los resultados. Su contribución principal es la evidencia de que los algoritmos de recorrido de grafos sobre redes semánticas permiten superar la brecha semántica entre consultas y documentos.

**A. Ba et al. (2015)** proponen la integración de redes semánticas en motores de búsqueda, demostrando que la expansión semántica de consultas y el descubrimiento de relaciones implícitas mejoran la precisión de la recuperación de información. Su contribución principal es la demostración de que las redes semánticas permiten superar las limitaciones de la coincidencia léxica al explotar la estructura relacional del conocimiento.

Estos trabajos son relevantes para el presente proyecto porque los mecanismos de inferencia semántica utilizados en la recuperación de información — recorrido de grafos, expansión de consultas, cálculo de proximidad semántica — son directamente aplicables al problema de la recomendación musical, donde la consulta del usuario (una canción, un artista, un género o un estado de ánimo) debe ser expandida semánticamente para descubrir ítems relevantes conectados por caminos en la red de conocimiento.


## 5.3 Brecha de Investigación (*Research Gap*)

El análisis de los trabajos relacionados revela una convergencia de evidencia que sustenta la efectividad de las redes semánticas en sistemas de recomendación y recuperación de información. Sin embargo, la revisión también permite identificar una **brecha de investigación** significativa que el presente proyecto pretende abordar.

### 5.3.1 Contribuciones existentes y sus alcances

Los trabajos analizados han demostrado, de manera independiente, los siguientes hallazgos:

1. **Las redes semánticas mejoran la recomendación musical** al permitir la inferencia de conexiones implícitas entre entidades del dominio (Li et al., 2016), pero el trabajo se limita a una demostración conceptual sin abordar la implementación de un agente inteligente completo con capacidades de razonamiento autónomo.

2. **Las redes semánticas son transferibles a dominios de recomendación** con entidades interconectadas, como lo demuestran los resultados en cine (Bani Younes et al., 2018) y comercio electrónico (Zhang et al., 2019), pero ninguno de estos trabajos aborda el dominio musical con la profundidad relacional que este requiere — seis tipos de entidades (canciones, artistas, géneros, estados de ánimo, instrumentos, épocas) interconectadas por ocho o más tipos de relaciones semánticas.

3. **La representación del conocimiento mediante redes semánticas supera a las representaciones planas** en la captura de relaciones complejas (Tang et al., 2017), pero este hallazgo no ha sido integrado con un mecanismo de inferencia semántica orientado específicamente a la generación de recomendaciones explicables en el dominio musical.

4. **La inferencia semántica sobre grafos de conocimiento mejora la recuperación de información** al explotar relaciones multi-nivel (Wu et al., 2018; Ba et al., 2015), pero estos trabajos se centran en la recuperación de documentos y no abordan la generación de recomendaciones con explicaciones trazables basadas en caminos semánticos.

### 5.3.2 La brecha identificada

Como se formuló en el planteamiento del problema (sección 1.4), la brecha de investigación que el presente proyecto aborda es la **ausencia de un enfoque integrado que combine**:

- Un **agente inteligente** — diseñado según los principios de agentes basados en conocimiento (Russell & Norvig, 2010, Capítulo 2) — que perciba consultas del usuario, razone sobre una base de conocimiento estructurada y actúe generando recomendaciones fundamentadas.

- Una **red semántica del dominio musical** — construida según los principios de representación del conocimiento (Russell & Norvig, 2010, Capítulo 10) — que modele las relaciones tipadas entre canciones, artistas, géneros, estados de ánimo, instrumentos y épocas con la expresividad necesaria para soportar inferencia semántica multi-nivel.

- Un **motor de inferencia semántica** que, mediante recorrido de grafos ponderado, descubra conexiones implícitas entre entidades musicales y genere recomendaciones con explicaciones trazables a través de caminos semánticos en la red.

- **Explicabilidad inherente** en cada recomendación, donde la justificación de cada sugerencia se derive directamente de los caminos semánticos encontrados en la red de conocimiento, proporcionando transparencia y comprensibilidad al usuario.

Ninguno de los trabajos analizados integra estos cuatro componentes en un sistema cohesivo aplicado al dominio musical. Li et al. (2016) abordan la recomendación musical con redes semánticas pero no implementan un agente inteligente con arquitectura formal. Bani Younes et al. (2018) y Zhang et al. (2019) demuestran la efectividad del enfoque en otros dominios pero no lo aplican al dominio musical con su riqueza relacional específica. Tang et al. (2017) fundamentan la representación del conocimiento pero no la conectan con mecanismos de recomendación. Wu et al. (2018) y Ba et al. (2015) demuestran la efectividad de la inferencia semántica pero en el contexto de recuperación de información, no de recomendación.

Esta brecha justifica el desarrollo del presente proyecto: un **agente inteligente basado en redes semánticas para la recomendación musical** que integre representación del conocimiento estructurado, inferencia semántica, generación de recomendaciones explicables y arquitectura de agente basado en conocimiento en un sistema cohesivo y verificable.


## 5.4 Tabla Comparativa de Trabajos Relacionados

La siguiente tabla sintetiza las características principales de los trabajos analizados, permitiendo una comparación estructurada de sus contribuciones, técnicas y limitaciones:

| Autor(es) | Año | Dominio de aplicación | Técnica de red semántica | Resultados principales | Limitaciones |
|---|---|---|---|---|---|
| H. Li, Y. Li y M. Zhang | 2016 | Recomendación musical | Red semántica con nodos de entidades musicales y arcos de relaciones tipadas; inferencia por recorrido de grafos | Recomendaciones más diversas y explicables que CF; descubrimiento de conexiones implícitas entre entidades musicales | Base de conocimiento pequeña; construcción manual; sin evaluación de escalabilidad |
| F. Bani Younes, A. A. Boudhir y M. Agnaou | 2018 | Recomendación de películas | Grafo de conocimiento cinematográfico con nodos tipados (películas, directores, actores, géneros, temáticas) | Mayor precisión que CF y CBF; recomendación transversal entre géneros; mitigación del arranque en frío | Sin aprendizaje automático para actualización; evaluación sobre conjunto acotado; sin integración con fuentes externas |
| F. Tang, W. Mu, M. Zhang y S. Liang | 2017 | Conocimiento organizacional | Red semántica con nodos de conceptos organizacionales y arcos de relaciones multi-tipo (jerárquicas, funcionales) | Superioridad sobre representaciones planas en captura de relaciones complejas; descubrimiento de relaciones implícitas | Evaluación cualitativa; sin métricas cuantitativas; sin aplicación a recomendación |
| J. Zhang, Y. Wang y L. Chen | 2019 | Recomendación de productos | Grafo de conocimiento de productos con relaciones de complementariedad, sustitución y compatibilidad funcional | Mejora en precisión vs. CF y CBF con datos escasos; explicabilidad aumenta aceptación del usuario | Construcción manual de base de conocimiento; evaluación centrada en precisión; sin exploración de diversidad |
| G. Wu, L. Zhang y F. Wang | 2018 | Recuperación de información | Red semántica como capa de conocimiento entre consultas y documentos; recorrido de grafos multi-nivel | Mejora significativa en relevancia de resultados; superación de brecha semántica consulta-documento | Esfuerzo de ingeniería del conocimiento; sin aprendizaje automático; evaluación en dominio específico |
| A. Ba, S. Abdou y B. Gueye | 2015 | Motores de búsqueda | Red semántica integrada en motor de búsqueda; expansión semántica de consultas; desambiguación de términos | Mejora en precisión para consultas complejas; descubrimiento de relaciones implícitas | Dependencia de calidad de la red; construcción manual; sin escalabilidad a vocabularios extensos |


## 5.5 Fundamentación Teórica

La presente sección fundamenta los conceptos teóricos centrales del proyecto a partir de los capítulos de referencia del libro de texto de la materia: el Capítulo 2 sobre Agentes Inteligentes y el Capítulo 10 sobre Representación del Conocimiento (Russell & Norvig, 2010).

### 5.5.1 Agentes Inteligentes (Capítulo 2)

El concepto de **agente inteligente** constituye el marco teórico fundamental para el diseño del sistema propuesto en este proyecto. Según Russell y Norvig (2010, Capítulo 2), un agente es una entidad autónoma que percibe su entorno mediante **sensores** y actúa sobre él mediante **actuadores**, siguiendo una **función de agente** que mapea secuencias de percepciones a acciones. Un agente inteligente es aquel que actúa de manera racional — es decir, que selecciona la acción que maximiza su medida de rendimiento dada la secuencia de percepciones recibida y el conocimiento incorporado.

#### Descripción PEAS

El marco **PEAS** (*Performance, Environment, Actuators, Sensors*) proporciona una metodología estructurada para la especificación de agentes inteligentes (Russell & Norvig, 2010, Capítulo 2). Este marco exige la definición explícita de cuatro componentes:

- **Medida de rendimiento (*Performance*)**: Los criterios cuantitativos y cualitativos que determinan el éxito del agente. En el contexto del presente proyecto, la medida de rendimiento incluye la precisión de las recomendaciones (precision@k, recall@k), la relevancia percibida por los usuarios, la diversidad de las sugerencias generadas y la calidad de las explicaciones proporcionadas.

- **Entorno (*Environment*)**: El contexto en el que opera el agente. El agente propuesto opera sobre una base de conocimiento musical estática representada como una red semántica, recibe consultas de usuario en formato de texto y opera dentro de un dominio acotado de géneros, artistas, canciones, estados de ánimo, instrumentos y épocas.

- **Actuadores (*Actuators*)**: Los mecanismos mediante los cuales el agente actúa sobre su entorno. El agente produce listas ordenadas de recomendaciones musicales acompañadas de explicaciones semánticas, donde cada explicación se fundamenta en caminos de inferencia trazables a través de la red de conocimiento.

- **Sensores (*Sensors*)**: Los mecanismos mediante los cuales el agente percibe su entorno. El agente recibe entrada de texto del usuario (consultas de recomendación, especificación de preferencias, selección de ítems del catálogo).

#### Tipos de agentes

Russell y Norvig (2010, Capítulo 2) presentan una taxonomía de agentes inteligentes que incluye: agentes reactivos simples, agentes reactivos basados en modelo, agentes basados en objetivos, agentes basados en utilidad y agentes que aprenden. El agente propuesto en este proyecto se clasifica como un **agente basado en conocimiento** (*knowledge-based agent*), una variante del agente basado en modelo que se caracteriza por:

- **Mantener una representación interna del mundo**: El agente posee una red semántica que modela el conocimiento del dominio musical, incluyendo entidades, relaciones y atributos.
- **Razonar sobre esa representación para tomar decisiones**: El agente utiliza un motor de inferencia semántica que recorre la red de conocimiento para descubrir conexiones implícitas y generar recomendaciones fundamentadas.
- **No aprender de forma autónoma**: El agente opera sobre una base de conocimiento estática, sin mecanismos de aprendizaje automático para la actualización dinámica de la red — una limitación declarada explícitamente en el alcance del proyecto.

Esta clasificación es consistente con la naturaleza del proyecto: un prototipo de investigación que demuestra la viabilidad del enfoque de redes semánticas para la recomendación musical, sin pretender implementar un sistema de producción con capacidades de aprendizaje continuo.

#### Propiedades del entorno de tarea

Russell y Norvig (2010, Capítulo 2) definen un conjunto de propiedades que caracterizan el entorno de tarea de un agente. El entorno del agente propuesto se clasifica como:

- **Totalmente observable**: El agente tiene acceso completo a toda la información de la base de conocimiento musical.
- **Determinista**: La misma consulta sobre la misma base de conocimiento produce siempre los mismos resultados.
- **Episódico**: Cada consulta de recomendación es independiente de las anteriores; el agente no mantiene estado entre consultas.
- **Estático**: La base de conocimiento no cambia durante la ejecución del agente.
- **Discreto**: El dominio está compuesto por un conjunto finito de entidades y relaciones.
- **Agente único**: Un solo agente opera sobre la base de conocimiento.

Estas propiedades simplifican significativamente el diseño del agente, ya que eliminan la necesidad de manejar incertidumbre, cambios dinámicos en el entorno o interacciones con otros agentes — complejidades que quedan fuera del alcance del presente proyecto.

### 5.5.2 Representación del Conocimiento (Capítulo 10)

La **representación del conocimiento** es el área de la Inteligencia Artificial que estudia cómo codificar información sobre el mundo en formas que un sistema computacional pueda utilizar para razonar y resolver problemas (Russell & Norvig, 2010, Capítulo 10). La elección de la técnica de representación del conocimiento es una decisión de diseño fundamental, ya que determina qué tipos de conocimiento pueden expresarse, qué tipos de inferencia son posibles y cuál es la eficiencia computacional del razonamiento.

#### Redes semánticas como técnica de representación

Las **redes semánticas** constituyen una de las técnicas de representación del conocimiento más establecidas en la literatura de IA (Russell & Norvig, 2010, Capítulo 10). Una red semántica es una estructura de grafo compuesta por:

- **Nodos**: Representan conceptos o entidades del dominio. En el contexto del presente proyecto, los nodos representan canciones, artistas, géneros musicales, estados de ánimo, instrumentos y épocas.
- **Arcos etiquetados**: Representan relaciones semánticas tipadas entre conceptos. Los arcos son dirigidos y etiquetados con el tipo de relación que representan (por ejemplo, *interpretada_por*, *pertenece_a_género*, *evoca_estado*, *influenciado_por*).

Las redes semánticas ofrecen varias propiedades que las hacen particularmente adecuadas para el dominio de la recomendación musical:

- **Expresividad relacional**: Permiten representar múltiples tipos de relaciones entre entidades, capturando la riqueza semántica del dominio musical donde las entidades están interconectadas por relaciones diversas y significativas.
- **Herencia y taxonomías**: Soportan relaciones jerárquicas (*es-un*, *subgénero-de*) que permiten organizar el conocimiento en taxonomías y propagar propiedades a lo largo de jerarquías.
- **Inferencia por recorrido de grafos**: Permiten derivar nuevo conocimiento mediante el recorrido de caminos en el grafo, descubriendo relaciones implícitas entre entidades que no están directamente conectadas.
- **Intuitividad**: La representación visual de nodos y arcos es intuitiva y comprensible, facilitando tanto el diseño de la base de conocimiento como la explicación de las recomendaciones al usuario.

#### Comparación con otras técnicas de representación

Russell y Norvig (2010, Capítulo 10) presentan diversas técnicas de representación del conocimiento, entre las que se incluyen los marcos (*frames*), la lógica de predicados de primer orden y las ontologías. Como se fundamentó en la justificación del proyecto (sección 2.5), las redes semánticas ofrecen un equilibrio óptimo entre expresividad, eficiencia de inferencia, explicabilidad y complejidad de implementación para el alcance del presente proyecto:

- Los **marcos** (*frames*) ofrecen estructuras estereotipadas con herencia de atributos, pero su rigidez estructural y limitada capacidad de inferencia relacional los hacen menos adecuados para un sistema de recomendación que debe explotar conexiones semánticas diversas entre entidades.
- La **lógica de predicados** ofrece máxima expresividad formal, pero su complejidad computacional (inferencia semi-decidible en el caso general), dificultad de modelado y ausencia de mecanismos nativos de ranking la hacen impráctica para un sistema de recomendación interactivo.
- Las **ontologías** extienden las redes semánticas con axiomas formales y razonamiento lógico, pero introducen una sobrecarga de formalización y dependencia de infraestructura especializada que excede las necesidades del presente prototipo de investigación.

La elección de redes semánticas se fundamenta, por tanto, en su adecuación al problema específico: representar el conocimiento del dominio musical con la expresividad necesaria para soportar inferencia semántica y generación de recomendaciones explicables, manteniendo una complejidad de implementación compatible con el alcance de un proyecto de maestría.

---

## Referencias

Ba, A., Abdou, S., & Gueye, B. (2015). Enhancing search engines with semantic networks. *International Journal of Advanced Computer Science and Applications*, *6*(3), 45–52.

Bani Younes, F., Boudhir, A. A., & Agnaou, M. (2018). A semantic network approach to movie recommendation. *International Journal of Computer Applications*, *182*(15), 1–6.

Gupta, R., Singh, A., & Kumar, P. (2017). Semantic network analysis of social media data for opinion mining. *Journal of Intelligent Information Systems*, *49*(1), 113–135.

Li, H., Li, Y., & Zhang, M. (2016). Music recommendation based on semantic network. *Proceedings of the International Conference on Computer Science and Network Technology*, 356–360.

Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3ra ed.). Pearson.

Tang, F., Mu, W., Zhang, M., & Liang, S. (2017). Knowledge representation in semantic networks for organizations. *International Journal of Knowledge Engineering*, *3*(1), 15–21.

Wang, M., Liu, X., & Chen, H. (2019). Knowledge representation in semantic networks for healthcare. *Journal of Biomedical Informatics*, *92*, 103–115.

Wu, G., Zhang, L., & Wang, F. (2018). Semantic network-based information retrieval system. *Information Processing & Management*, *54*(6), 1032–1049.

Zhang, J., Wang, Y., & Chen, L. (2019). Product recommendation using semantic networks. *Journal of Intelligent Information Systems*, *52*(2), 285–308.
