# 🎵 Agente Inteligente basado en Redes Semánticas para Recomendación Musical

Proyecto de investigación para la Maestría en Inteligencia Artificial — Fundamentos de IA.

## Descripción

Agente inteligente que utiliza **redes semánticas** (representación del conocimiento mediante nodos y arcos tipados) para recomendar música. A diferencia del filtrado colaborativo o basado en contenido, este enfoque captura relaciones semánticas profundas entre entidades musicales y genera recomendaciones **explicables** con caminos de razonamiento trazables.

## Arquitectura

```
┌─────────────────────────────────┐
│   Capa de Percepción (CLI)      │
│   Consultas en lenguaje natural │
├─────────────────────────────────┤
│   Capa de Razonamiento          │
│   Motor de Inferencia BFS       │
│   Motor de Recomendación        │
│   Generador de Explicaciones    │
├─────────────────────────────────┤
│   Capa de Conocimiento          │
│   Red Semántica (grafo)         │
│   Base de Conocimiento Musical  │
└─────────────────────────────────┘
```

## Base de Conocimiento

| Entidad        | Cantidad |
|----------------|----------|
| Canciones      | 23       |
| Artistas       | 22       |
| Géneros        | 12       |
| Estados de ánimo | 8      |
| Instrumentos   | 9        |
| Épocas         | 8        |
| Álbumes        | 18       |
| **Total nodos** | **100** |
| **Total arcos** | **360** |

## Requisitos

- Python >= 3.10

## Instalación

```bash
# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install pytest hypothesis
```

## Uso

```bash
python main.py
```

### Ejemplos de consultas

```
🎵 > recomiéndame algo como Bohemian Rhapsody
🎵 > recomiéndame canciones de Queen
🎵 > quiero música relajada
🎵 > recomiéndame rock
🎵 > salir
```

Cada recomendación incluye una puntuación de relevancia semántica y una explicación trazable basada en los caminos encontrados en la red de conocimiento.

## Estructura del Proyecto

```
├── src/
│   ├── models/          # Red semántica, enums, dataclasses
│   ├── engine/          # Motor de inferencia y recomendación
│   ├── knowledge/       # Constructor de base de conocimiento
│   └── cli/             # Interfaz de línea de comandos
├── data/                # Base de conocimiento musical (JSON)
├── docs/                # Secciones del documento de investigación
├── tests/               # Tests unitarios y de propiedades
├── context/             # PDFs de referencia (capítulos del libro)
└── main.py              # Punto de entrada
```

## Documento de Investigación

Las secciones del trabajo académico se encuentran en `docs/`:

- `planteamiento_del_problema.md` — Sobrecarga de información y limitaciones de enfoques tradicionales
- `justificacion.md` — Ventajas de redes semánticas y comparación con otras técnicas
- `preguntas_de_investigacion.md` — Pregunta principal y 4 preguntas secundarias
- `objetivos.md` — Objetivo general y 5 objetivos específicos
- `estado_del_arte.md` — Análisis de 6 papers, tabla comparativa, brecha de investigación
- `alcance_y_limitaciones.md` — Alcance, limitaciones y metodología
- `estructura_documento.md` — Estructura completa, glosario y bibliografía APA

## Referencias Principales

- H. Li et al. (2016) — *Music Recommendation Based on Semantic Network*
- F. Bani Younes et al. (2018) — *A Semantic Network Approach to Movie Recommendation*
- F. Tang et al. (2017) — *Knowledge Representation in Semantic Networks for Organizations*
- J. Zhang et al. (2019) — *Product Recommendation Using Semantic Networks*
- Russell, S. & Norvig, P. (2010) — *Artificial Intelligence: A Modern Approach*, Capítulos 2 y 10
