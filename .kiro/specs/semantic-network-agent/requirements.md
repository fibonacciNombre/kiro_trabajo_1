# Documento de Requisitos

## Introducción

Este documento define los requisitos para la fase de **Identificación del Problema** del trabajo de investigación de Maestría en Inteligencia Artificial (Fundamentos de IA). El proyecto consiste en el desarrollo de un agente inteligente basado en Redes Semánticas para la recomendación de música.

La identificación del problema se fundamenta en los siguientes papers de referencia:
- "Music Recommendation Based on Semantic Network" — H. Li et al. (2016)
- "A Semantic Network Approach to Movie Recommendation" — F. Bani Younes et al. (2018)
- "Knowledge Representation in Semantic Networks for Organizations" — F. Tang et al. (2017)
- "Enhancing Search Engines with Semantic Networks" — A. Ba et al. (2015)
- "Knowledge Representation in Semantic Networks for Healthcare" — M. Wang et al. (2019)
- "Semantic Network Analysis of Social Media Data for Opinion Mining" — R. Gupta et al. (2017)
- "Product Recommendation Using Semantic Networks" — J. Zhang et al. (2019)
- "Semantic Network-Based Information Retrieval System" — G. Wu et al. (2018)

El marco teórico se apoya en los capítulos de referencia sobre Agentes Inteligentes (Capítulo 2) y Representación del Conocimiento (Capítulo 10) del libro de texto de la materia.

## Glosario

- **Agente_Inteligente**: Entidad autónoma que percibe su entorno mediante sensores y actúa sobre él mediante actuadores, siguiendo una función de agente que mapea secuencias de percepciones a acciones (definición según Capítulo 2 del libro de referencia).
- **Red_Semántica**: Estructura de representación del conocimiento compuesta por nodos (conceptos) y arcos (relaciones etiquetadas) que permite modelar relaciones semánticas entre entidades de un dominio específico (definición según Capítulo 10 del libro de referencia).
- **Nodo**: Unidad fundamental de la Red_Semántica que representa un concepto del dominio (artista, canción, género, estado de ánimo, instrumento, época).
- **Arco**: Conexión dirigida y etiquetada entre dos Nodos que representa una relación semántica tipada.
- **Sistema_de_Recomendación**: Sistema que predice la preferencia o calificación que un usuario daría a un ítem, utilizado para sugerir contenido relevante.
- **Filtrado_Colaborativo**: Técnica de recomendación que utiliza patrones de comportamiento de usuarios similares para generar sugerencias.
- **Filtrado_Basado_en_Contenido**: Técnica de recomendación que utiliza atributos de los ítems previamente consumidos por el usuario para sugerir ítems similares.
- **Sobrecarga_de_Información**: Fenómeno donde el volumen de información disponible excede la capacidad del usuario para procesarla y tomar decisiones efectivas.
- **Representación_del_Conocimiento**: Área de la IA que estudia cómo codificar información sobre el mundo en formas que un sistema computacional pueda utilizar para razonar y resolver problemas.
- **Inferencia_Semántica**: Proceso de derivar nuevo conocimiento a partir de relaciones existentes en la Red_Semántica mediante recorrido de grafos y transitividad de relaciones.
- **Trabajo_de_Investigación**: Documento académico que sigue la estructura definida en las reglas del proyecto: identificación del problema, marco teórico, propuesta de solución, implementación, evaluación y conclusiones.

## Requisitos

### Requisito 1: Planteamiento del Problema

**Historia de Usuario:** Como investigador de maestría, quiero formular un planteamiento del problema claro y fundamentado en la literatura, para que el Trabajo_de_Investigación tenga una base sólida que justifique el desarrollo del agente inteligente.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL describir el problema de la Sobrecarga_de_Información en plataformas de streaming musical, citando datos cuantitativos de catálogos musicales actuales (millones de canciones disponibles en plataformas como Spotify, Apple Music, YouTube Music).
2. THE Trabajo_de_Investigación SHALL identificar las limitaciones específicas del Filtrado_Colaborativo: dependencia de datos históricos de usuarios, problema del arranque en frío (cold start), y falta de explicabilidad en las recomendaciones, fundamentándose en los hallazgos de H. Li et al. (2016).
3. THE Trabajo_de_Investigación SHALL identificar las limitaciones específicas del Filtrado_Basado_en_Contenido: análisis superficial de atributos, incapacidad de capturar relaciones semánticas profundas entre entidades musicales, y tendencia a recomendaciones homogéneas, fundamentándose en los hallazgos de F. Bani Younes et al. (2018).
4. THE Trabajo_de_Investigación SHALL formular el problema central como la ausencia de un mecanismo de recomendación que capture y explote relaciones semánticas complejas entre entidades del dominio musical (géneros, artistas, canciones, estados de ánimo, instrumentos, épocas).

### Requisito 2: Justificación del Enfoque de Redes Semánticas

**Historia de Usuario:** Como investigador de maestría, quiero justificar por qué las redes semánticas son un enfoque adecuado para la recomendación musical, para que el Trabajo_de_Investigación demuestre la pertinencia de la técnica de Representación_del_Conocimiento elegida.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL argumentar que las Redes Semánticas permiten representar relaciones complejas entre entidades musicales mediante nodos y arcos tipados, superando las limitaciones de representaciones planas (vectores de características), fundamentándose en F. Tang et al. (2017).
2. THE Trabajo_de_Investigación SHALL demostrar que la Inferencia_Semántica sobre Redes Semánticas permite descubrir relaciones implícitas entre entidades musicales que no son evidentes en enfoques tradicionales, citando los resultados de H. Li et al. (2016).
3. THE Trabajo_de_Investigación SHALL presentar evidencia de la aplicabilidad de Redes Semánticas en dominios de recomendación, referenciando los resultados exitosos en recomendación de películas (F. Bani Younes et al., 2018) y recomendación de productos (J. Zhang et al., 2019).
4. THE Trabajo_de_Investigación SHALL justificar que el enfoque de Redes Semánticas proporciona explicabilidad inherente en las recomendaciones, ya que cada sugerencia se fundamenta en un camino semántico trazable entre nodos, a diferencia de modelos de caja negra.
5. THE Trabajo_de_Investigación SHALL fundamentar la elección de Redes Semánticas como técnica de Representación_del_Conocimiento según los principios del Capítulo 10 del libro de referencia, comparándolas con otras técnicas (marcos, lógica de predicados, ontologías).

### Requisito 3: Formulación de Preguntas de Investigación

**Historia de Usuario:** Como investigador de maestría, quiero definir preguntas de investigación precisas y alcanzables, para que el Trabajo_de_Investigación tenga un enfoque claro y medible.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL formular una pregunta de investigación principal: ¿Cómo puede un Agente_Inteligente basado en Redes Semánticas mejorar la calidad y explicabilidad de las recomendaciones musicales al capturar relaciones semánticas entre entidades del dominio musical?
2. THE Trabajo_de_Investigación SHALL formular al menos tres preguntas de investigación secundarias que aborden: (a) la construcción de la Red_Semántica del dominio musical, (b) el mecanismo de Inferencia_Semántica para generar recomendaciones, y (c) la evaluación de la calidad de las recomendaciones generadas.
3. THE Trabajo_de_Investigación SHALL vincular cada pregunta de investigación con al menos un paper de referencia que aborde un aspecto relacionado.
4. THE Trabajo_de_Investigación SHALL verificar que cada pregunta de investigación sea específica, medible y alcanzable dentro del alcance de un proyecto de maestría.

### Requisito 4: Definición de Objetivos de Investigación

**Historia de Usuario:** Como investigador de maestría, quiero definir objetivos generales y específicos alineados con las preguntas de investigación, para que el Trabajo_de_Investigación tenga metas claras y verificables.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL definir un objetivo general que establezca el desarrollo de un Agente_Inteligente basado en Redes Semánticas para la recomendación musical.
2. THE Trabajo_de_Investigación SHALL definir al menos cuatro objetivos específicos que correspondan a las fases del proyecto: (a) analizar el estado del arte en sistemas de recomendación y redes semánticas, (b) diseñar la Red_Semántica del dominio musical, (c) implementar el Agente_Inteligente con capacidad de Inferencia_Semántica, y (d) evaluar el desempeño del agente.
3. THE Trabajo_de_Investigación SHALL redactar cada objetivo específico comenzando con un verbo en infinitivo medible (analizar, diseñar, implementar, evaluar, comparar, demostrar).
4. THE Trabajo_de_Investigación SHALL asegurar que cada objetivo específico sea trazable a al menos una pregunta de investigación del Requisito 3.

### Requisito 5: Revisión del Estado del Arte

**Historia de Usuario:** Como investigador de maestría, quiero realizar una revisión estructurada del estado del arte, para que el Trabajo_de_Investigación demuestre conocimiento del campo y posicione la contribución del proyecto.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL analizar al menos cinco de los ocho papers de referencia, extrayendo de cada uno: problema abordado, técnica utilizada, resultados obtenidos y limitaciones identificadas.
2. THE Trabajo_de_Investigación SHALL clasificar los trabajos relacionados en al menos tres categorías: (a) sistemas de recomendación basados en redes semánticas, (b) representación del conocimiento en redes semánticas para dominios específicos, y (c) aplicaciones de redes semánticas en recuperación de información.
3. THE Trabajo_de_Investigación SHALL identificar la brecha de investigación (gap) que el proyecto pretende abordar, comparando las contribuciones existentes con el problema planteado en el Requisito 1.
4. THE Trabajo_de_Investigación SHALL presentar una tabla comparativa de los trabajos relacionados que incluya: autor, año, dominio de aplicación, técnica de red semántica utilizada, y resultados principales.
5. THE Trabajo_de_Investigación SHALL fundamentar los conceptos de Agente_Inteligente según el Capítulo 2 del libro de referencia (tipos de agentes, entorno de tarea, propiedades PEAS) y los conceptos de Representación_del_Conocimiento según el Capítulo 10.

### Requisito 6: Definición del Alcance y Limitaciones

**Historia de Usuario:** Como investigador de maestría, quiero definir claramente el alcance y las limitaciones del proyecto, para que el Trabajo_de_Investigación establezca expectativas realistas y delimite la contribución.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL delimitar el alcance del proyecto especificando: el dominio musical cubierto (géneros, artistas, canciones), el tamaño mínimo de la Base_de_Conocimiento, y los tipos de consultas soportadas por el Agente_Inteligente.
2. THE Trabajo_de_Investigación SHALL identificar al menos tres limitaciones del proyecto: (a) tamaño acotado de la Base_de_Conocimiento frente a catálogos reales, (b) ausencia de aprendizaje automático para actualización dinámica de la Red_Semántica, y (c) evaluación con un grupo reducido de usuarios.
3. THE Trabajo_de_Investigación SHALL definir los entregables del proyecto: (a) documento de investigación con la estructura requerida, y (b) prototipo funcional del Agente_Inteligente.
4. THE Trabajo_de_Investigación SHALL especificar la metodología de desarrollo del prototipo, alineada con las reglas del documento de proyecto (metodología de investigación aplicada con componente de desarrollo de software).

### Requisito 7: Estructura del Documento de Investigación

**Historia de Usuario:** Como investigador de maestría, quiero que el documento de investigación siga la estructura requerida por las reglas del proyecto, para que el Trabajo_de_Investigación cumpla con los criterios de evaluación académica.

#### Criterios de Aceptación

1. THE Trabajo_de_Investigación SHALL seguir la estructura de informe definida en las reglas del proyecto, incluyendo como mínimo: introducción, planteamiento del problema, justificación, objetivos, marco teórico, estado del arte, propuesta de solución, implementación, evaluación, conclusiones y referencias.
2. THE Trabajo_de_Investigación SHALL incluir todas las referencias bibliográficas en formato académico estándar (APA o IEEE), citando los ocho papers de referencia y los capítulos del libro de texto.
3. THE Trabajo_de_Investigación SHALL incluir un glosario de términos técnicos de IA y redes semánticas utilizados en el documento.
4. THE Trabajo_de_Investigación SHALL cumplir con las fuentes de referencia especificadas en las reglas del proyecto, utilizando fuentes académicas verificables (journals, conferencias, libros de texto).
