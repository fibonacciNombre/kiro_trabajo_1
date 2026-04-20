# Planteamiento del Problema

## 1.1 La Sobrecarga de Información en Plataformas de Streaming Musical

La industria del streaming musical ha experimentado un crecimiento exponencial durante la última década, transformando radicalmente la forma en que los usuarios acceden, descubren y consumen contenido musical. Este crecimiento ha generado un fenómeno de **sobrecarga de información** (*information overload*) sin precedentes en el dominio del entretenimiento digital, donde el volumen de contenido disponible excede por varios órdenes de magnitud la capacidad humana de exploración y procesamiento.

En términos cuantitativos, las cifras actuales de las principales plataformas de streaming musical ilustran la magnitud del problema:

- **Spotify** reporta un catálogo que supera los **100 millones de pistas** disponibles, con una base de más de **600 millones de usuarios activos** a nivel global, de los cuales aproximadamente 220 millones son suscriptores de pago (Spotify, 2024). La plataforma incorpora aproximadamente 100,000 nuevas pistas cada día, lo que implica que el catálogo crece a un ritmo que ningún usuario individual podría seguir.
- **Apple Music** ofrece un catálogo de magnitud comparable, superando igualmente los **100 millones de canciones** disponibles para sus suscriptores en más de 167 países (Apple, 2024).
- **YouTube Music** posee el catálogo efectivo más extenso del ecosistema de streaming, al integrar no solo pistas oficiales de sellos discográficos, sino también presentaciones en vivo, remixes, covers, versiones acústicas y contenido generado por usuarios que no existe en otras plataformas (Lissen, 2026).
- **Amazon Music** cuenta con un catálogo de más de **100 millones de canciones** y ha experimentado un crecimiento sostenido en su base de usuarios (Amazon, 2024).

En conjunto, las plataformas principales de streaming musical superan los **600 millones de usuarios combinados** a nivel mundial, y el mercado global del streaming musical alcanzó un valor estimado de **17,500 millones de dólares** en ingresos por suscripción en 2023, según datos de la Federación Internacional de la Industria Fonográfica (IFPI, 2024).

Esta abundancia masiva de contenido musical genera una paradoja ampliamente documentada en la literatura de sistemas de información: **mientras más opciones tiene el usuario, más difícil se vuelve tomar decisiones satisfactorias** (Schwartz, 2004). El usuario promedio de una plataforma de streaming se enfrenta a un catálogo cuya magnitud excede en varios órdenes de magnitud su capacidad de exploración personal. Si un usuario dedicara tan solo 30 segundos a evaluar cada canción disponible en Spotify, necesitaría más de **95 años de escucha ininterrumpida** para recorrer el catálogo completo. Esta realidad convierte a los sistemas de recomendación en componentes absolutamente críticos de la experiencia de usuario en estas plataformas, ya que constituyen el principal mecanismo mediante el cual los usuarios descubren contenido relevante dentro de un océano de opciones.

Sin embargo, a pesar de la inversión significativa que las plataformas de streaming realizan en sus algoritmos de recomendación, los enfoques predominantes presentan limitaciones fundamentales que afectan la calidad, diversidad y explicabilidad de las sugerencias generadas. Estas limitaciones se analizan en las secciones siguientes.


## 1.2 Limitaciones del Filtrado Colaborativo

El filtrado colaborativo (*Collaborative Filtering*, CF) ha sido históricamente el enfoque dominante en los sistemas de recomendación musical y, de manera más general, en los sistemas de recomendación de contenido digital. Su principio fundamental consiste en identificar patrones de comportamiento compartidos entre usuarios para predecir preferencias: si dos usuarios han mostrado gustos similares en el pasado, es probable que compartan preferencias sobre ítems que uno ha consumido y el otro no. Este enfoque ha demostrado ser efectivo en numerosos dominios, desde el comercio electrónico hasta el entretenimiento, y constituye la base de los sistemas de recomendación de plataformas como Spotify (a través de su algoritmo de *Discover Weekly*) y Netflix.

No obstante, como identifican H. Li et al. (2016) en su investigación seminal sobre recomendación musical basada en redes semánticas, el filtrado colaborativo presenta **limitaciones fundamentales** que comprometen su efectividad en el dominio musical, particularmente cuando se busca ofrecer recomendaciones de alta calidad, diversas y comprensibles para el usuario.

### 1.2.1 Dependencia de datos históricos de usuarios

El CF requiere un volumen significativo de interacciones previas — reproducciones, calificaciones, adiciones a listas de reproducción, marcaciones de "me gusta" — para construir perfiles de usuario robustos y calcular similitudes significativas entre ellos. Esta dependencia implica que la calidad de las recomendaciones está **directamente condicionada por la cantidad y calidad de datos de comportamiento acumulados** (H. Li et al., 2016).

En el contexto del streaming musical, esta limitación se manifiesta de múltiples formas:

- **Sesgo hacia contenido popular**: Los ítems con mayor número de interacciones reciben desproporcionadamente más recomendaciones, mientras que canciones de nicho o artistas independientes con pocas interacciones quedan marginados del sistema, independientemente de su calidad o relevancia potencial para ciertos usuarios.
- **Vulnerabilidad a datos ruidosos**: Las interacciones de los usuarios no siempre reflejan preferencias genuinas. Un usuario puede reproducir una canción por curiosidad, por contexto social, o accidentalmente, generando señales que distorsionan su perfil de preferencias.
- **Escalabilidad computacional**: A medida que crece la base de usuarios y el catálogo, la matriz de interacciones usuario-ítem se vuelve extremadamente dispersa (*sparse*), lo que dificulta el cálculo eficiente de similitudes y reduce la precisión de las predicciones.

### 1.2.2 Problema del arranque en frío (*cold start*)

El problema del arranque en frío constituye una de las limitaciones más críticas y ampliamente estudiadas del filtrado colaborativo (H. Li et al., 2016). Este problema se manifiesta en dos escenarios complementarios:

- **Nuevos usuarios**: Cuando un usuario se registra por primera vez en la plataforma, el sistema carece de historial de interacciones para construir un perfil de preferencias. En consecuencia, las recomendaciones iniciales son esencialmente aleatorias o basadas en popularidad general, lo que puede resultar en una experiencia inicial insatisfactoria que afecta la retención del usuario.
- **Nuevos ítems**: Cuando se incorpora una nueva canción o un nuevo artista al catálogo, no existen interacciones previas que permitan al sistema evaluar su relevancia para diferentes segmentos de usuarios. Este problema es particularmente agudo en el dominio musical, donde **artistas emergentes y lanzamientos recientes** — precisamente el contenido que más se beneficiaría de la recomendación para ganar visibilidad — son los más afectados por la ausencia de datos históricos (H. Li et al., 2016).

En un ecosistema donde se agregan aproximadamente 100,000 nuevas pistas diariamente, el problema del arranque en frío no es una excepción sino una condición permanente que afecta a una proporción significativa del catálogo en todo momento.

### 1.2.3 Falta de explicabilidad

Las recomendaciones generadas por el filtrado colaborativo se basan en **patrones estadísticos de co-ocurrencia** entre usuarios, lo que produce sugerencias del tipo *"usuarios similares a ti también escucharon X"*. Si bien este tipo de justificación puede ser parcialmente informativa, el mecanismo subyacente opera fundamentalmente como una **caja negra** que no puede articular *por qué* una canción es musicalmente relevante para el usuario (H. Li et al., 2016).

El CF no puede explicar que una recomendación se debe a:
- Afinidades de género musical entre las canciones del historial del usuario y la canción recomendada.
- Similitudes instrumentales o de arreglo que conectan las preferencias del usuario con nuevo contenido.
- Conexiones artísticas (influencias, colaboraciones, pertenencia a movimientos musicales) entre artistas conocidos y artistas recomendados.
- Correspondencias de estado de ánimo o contexto emocional entre la música consumida y la sugerida.

Esta falta de explicabilidad no es meramente un problema de interfaz de usuario; refleja una **limitación estructural** del enfoque, que opera sobre patrones de comportamiento sin comprender el dominio musical subyacente. Como señalan H. Li et al. (2016), la ausencia de explicaciones significativas reduce la confianza del usuario en el sistema y limita su capacidad para refinar sus preferencias de manera informada.


## 1.3 Limitaciones del Filtrado Basado en Contenido

El filtrado basado en contenido (*Content-Based Filtering*, CBF) surge como un enfoque complementario al filtrado colaborativo, intentando superar algunas de sus limitaciones al centrar el análisis en las **características intrínsecas de los ítems** en lugar de depender exclusivamente de patrones de comportamiento de usuarios. En el dominio musical, el CBF analiza atributos como género, artista, año de publicación, tempo, tonalidad, energía, valencia emocional y otras características acústicas extraídas mediante técnicas de procesamiento de señales de audio.

No obstante, como señalan F. Bani Younes et al. (2018) en su trabajo sobre la aplicación de redes semánticas a sistemas de recomendación, el filtrado basado en contenido también presenta **deficiencias significativas** que limitan su capacidad para generar recomendaciones de alta calidad en el dominio musical.

### 1.3.1 Análisis superficial de atributos

El CBF típicamente opera sobre **metadatos explícitos** (género, artista, año, sello discográfico) o **características acústicas** extraídas automáticamente mediante algoritmos de análisis de audio (tempo, tonalidad, espectro de frecuencias, tasa de cruces por cero). Si bien estos atributos capturan propiedades individuales de cada canción, el análisis se limita a una representación plana y unidimensional que **no captura las relaciones complejas** que existen entre las entidades del dominio musical (F. Bani Younes et al., 2018).

Por ejemplo, el CBF puede determinar que dos canciones comparten el mismo género (rock) y un tempo similar (120 BPM), pero no puede representar ni explotar relaciones más profundas como:

- La **influencia artística** de un músico sobre otro, que puede manifestarse en similitudes estilísticas que trascienden los atributos acústicos medibles.
- La **evolución de un género** a lo largo de décadas, donde el rock de los años 60 y el rock alternativo de los años 90 comparten una genealogía musical que no se refleja en sus características acústicas superficiales.
- La **conexión entre un estado de ánimo y una combinación particular de instrumentos**, donde la melancolía puede asociarse tanto con un piano solo como con una guitarra acústica en fingerpicking, dependiendo del contexto cultural y estilístico.
- Las **relaciones de subgénero** que organizan jerárquicamente el espacio musical, donde el jazz fusion hereda características tanto del jazz como del rock progresivo.

### 1.3.2 Incapacidad de capturar relaciones semánticas profundas

Las representaciones planas basadas en **vectores de características** (*feature vectors*) constituyen el modelo de datos predominante en los sistemas CBF. En este modelo, cada canción se representa como un punto en un espacio multidimensional donde cada dimensión corresponde a un atributo o característica. La similitud entre canciones se calcula mediante métricas de distancia (coseno, euclidiana) en este espacio vectorial.

Sin embargo, como argumentan F. Bani Younes et al. (2018), esta representación **no puede modelar la riqueza relacional del dominio musical**. Una canción no es simplemente un conjunto de atributos aislados, sino un **nodo en una red compleja de relaciones**:

- Pertenece a un género que es subgénero de otro.
- Fue interpretada por un artista que fue influenciado por otros artistas de épocas anteriores.
- Evoca estados de ánimo que comparte con canciones de géneros y épocas distintas.
- Presenta instrumentos que caracterizan tradiciones musicales específicas.
- Forma parte de un álbum que tiene una coherencia temática y estilística propia.

El CBF convencional carece de mecanismos para **representar ni explotar esta estructura relacional**, lo que limita fundamentalmente su capacidad para descubrir conexiones no triviales entre entidades musicales. Dos canciones pueden estar profundamente conectadas a través de múltiples dimensiones semánticas (influencia artística, herencia de género, contexto emocional) y, sin embargo, aparecer como distantes en el espacio vectorial de características acústicas.

### 1.3.3 Tendencia a recomendaciones homogéneas (burbuja de filtro)

Al basarse exclusivamente en la **similitud de atributos** con ítems previamente consumidos por el usuario, el CBF tiende a generar un efecto conocido como **"burbuja de filtro"** (*filter bubble*), donde las recomendaciones se vuelven progresivamente más homogéneas y predecibles (F. Bani Younes et al., 2018).

Este fenómeno se manifiesta de la siguiente manera: si un usuario ha escuchado predominantemente canciones de rock clásico, el sistema CBF recomendará más canciones de rock clásico con atributos acústicos similares, reforzando un ciclo cerrado que **limita el descubrimiento de música nueva y diversa**. El usuario queda atrapado en una zona de confort algorítmica que reduce la **serendipia** (*serendipity*) — la posibilidad de encontrar contenido inesperadamente satisfactorio — que es fundamental para una experiencia musical enriquecedora.

La burbuja de filtro es particularmente problemática en el dominio musical porque:

- La música es un dominio donde la **exploración y el descubrimiento** son componentes esenciales de la experiencia del usuario. A diferencia de otros dominios de recomendación (como productos de consumo), los usuarios de música frecuentemente desean ser sorprendidos con contenido que no habrían buscado activamente.
- Las **conexiones transversales** entre géneros, épocas y estilos son una fuente rica de descubrimiento musical. Un oyente de jazz podría disfrutar del bossa nova (por la conexión armónica), del hip-hop (por la tradición del sampling de jazz), o de la música electrónica (por la experimentación sonora), pero un sistema CBF basado en atributos acústicos difícilmente establecería estas conexiones.
- La **diversidad musical** es un valor en sí mismo para muchos usuarios, y un sistema que converge hacia la homogeneidad contradice esta preferencia fundamental.


## 1.4 Formulación del Problema Central

A partir del análisis exhaustivo de las limitaciones de los enfoques tradicionales de recomendación musical presentado en las secciones anteriores, se identifica el **problema central** que motiva la presente investigación:

> **No existe un mecanismo de recomendación musical que capture y explote las relaciones semánticas complejas entre las entidades del dominio musical — géneros, artistas, canciones, estados de ánimo, instrumentos y épocas — de manera que permita generar recomendaciones diversas, explicables y fundamentadas en el conocimiento estructurado del dominio.**

Esta formulación del problema se sustenta en las siguientes observaciones convergentes:

1. **Los enfoques de filtrado colaborativo operan sobre patrones de comportamiento de usuarios sin comprender el dominio musical.** El CF trata las canciones como ítems intercambiables cuya relevancia se determina exclusivamente por patrones de co-consumo, ignorando la estructura semántica rica que subyace al dominio musical. Como demuestran H. Li et al. (2016), esta desconexión entre el mecanismo de recomendación y el conocimiento del dominio resulta en recomendaciones que carecen de fundamentación musical y no pueden ser explicadas en términos comprensibles para el usuario.

2. **Los enfoques basados en contenido analizan atributos superficiales sin capturar la estructura relacional profunda.** El CBF reduce cada entidad musical a un vector de características independientes, perdiendo la información relacional que conecta artistas con géneros, canciones con estados de ánimo, instrumentos con tradiciones musicales, y épocas con movimientos artísticos. Como señalan F. Bani Younes et al. (2018), esta representación plana es inherentemente incapaz de modelar las relaciones semánticas multi-nivel que caracterizan al dominio musical.

3. **Ninguno de los enfoques tradicionales aprovecha la estructura semántica inherente del dominio musical.** El dominio musical posee una estructura semántica inherentemente rica, donde las entidades están interconectadas por **relaciones tipadas y significativas** que pueden ser representadas, razonadas y explotadas computacionalmente. Un artista *pertenece a* un género, *fue influenciado por* otros artistas, *interpreta* canciones que *evocan* estados de ánimo específicos y *presentan* instrumentos característicos de una *época* determinada. Esta red de relaciones constituye un conocimiento estructurado del dominio que los enfoques tradicionales no representan ni utilizan.

4. **La ausencia de explicabilidad en los sistemas actuales limita la confianza y la utilidad de las recomendaciones.** Los usuarios no solo desean recibir sugerencias relevantes, sino también comprender *por qué* una canción les es recomendada. Un sistema que pueda articular que recomienda una canción porque *"fue interpretada por un artista influenciado por tus artistas favoritos, pertenece a un subgénero del género que más escuchas, y evoca un estado de ánimo similar al de tus canciones recientes"* ofrece un valor cualitativamente superior a uno que simplemente indica *"otros usuarios también escucharon esto"*.

### Brecha identificada

La brecha de investigación que se identifica es la **ausencia de un enfoque de recomendación musical que integre representación del conocimiento estructurado mediante redes semánticas con capacidades de inferencia semántica**, permitiendo:

- **Capturar relaciones semánticas multi-nivel** entre entidades musicales (géneros, artistas, canciones, estados de ánimo, instrumentos, épocas) mediante una estructura de grafo con nodos y arcos tipados.
- **Realizar inferencia semántica** para descubrir conexiones implícitas entre entidades que no están directamente relacionadas, pero que comparten caminos semánticos significativos en la red de conocimiento.
- **Generar recomendaciones explicables** donde cada sugerencia se fundamenta en un camino de razonamiento trazable a través de la red semántica, proporcionando transparencia y comprensibilidad al usuario.
- **Superar el problema del arranque en frío** mediante el conocimiento estructurado del dominio, que permite generar recomendaciones para nuevos ítems basándose en sus relaciones semánticas con entidades existentes, sin depender de datos históricos de interacción.
- **Promover la diversidad** en las recomendaciones al explorar múltiples dimensiones semánticas simultáneamente, evitando la convergencia hacia la homogeneidad que caracteriza a los enfoques basados en contenido.

Esta brecha motiva el desarrollo de un **agente inteligente basado en redes semánticas** que, al representar el conocimiento musical como un grafo de nodos y arcos tipados — según los principios de representación del conocimiento establecidos en la literatura de Inteligencia Artificial (Russell & Norvig, 2010, Capítulo 10) —, pueda abordar las limitaciones identificadas y ofrecer una alternativa fundamentada en el conocimiento del dominio a los enfoques tradicionales de recomendación musical.

---

## Referencias

Apple. (2024). *Apple Music*. https://www.apple.com/apple-music/

Amazon. (2024). *Amazon Music Unlimited*. https://www.amazon.com/music/unlimited

Bani Younes, F., Boudhir, A. A., & Agnaou, M. (2018). A semantic network approach to movie recommendation. *International Journal of Computer Applications*, *182*(15), 1–6.

IFPI. (2024). *Global Music Report 2024*. International Federation of the Phonographic Industry.

Li, H., Li, Y., & Zhang, M. (2016). Music recommendation based on semantic network. *Proceedings of the International Conference on Computer Science and Network Technology*, 356–360.

Lissen. (2026). YouTube Music review 2026. *Lissen Blog*. https://www.lissen.com/blog/reviews/youtube-music-review-2026

Russell, S., & Norvig, P. (2010). *Artificial Intelligence: A Modern Approach* (3ra ed.). Pearson.

Schwartz, B. (2004). *The Paradox of Choice: Why More Is Less*. Harper Perennial.

Spotify. (2024). *Company info*. Spotify Newsroom. https://newsroom.spotify.com/
