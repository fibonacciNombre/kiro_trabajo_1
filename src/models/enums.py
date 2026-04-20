"""Enumeraciones para tipos de nodos y relaciones de la red semántica musical."""

from enum import Enum


class NodeType(Enum):
    """Tipos de nodos en la red semántica musical."""
    SONG = "cancion"
    ARTIST = "artista"
    GENRE = "genero"
    MOOD = "estado_animo"
    INSTRUMENT = "instrumento"
    ERA = "epoca"
    ALBUM = "album"


class RelationType(Enum):
    """Tipos de relaciones semánticas entre nodos."""
    # Relaciones Artista-Canción
    PERFORMED_BY = "interpretada_por"
    COMPOSED_BY = "compuesta_por"

    # Relaciones de Género
    BELONGS_TO_GENRE = "pertenece_a_genero"
    SUBGENRE_OF = "subgenero_de"

    # Relaciones de Estado de Ánimo
    EVOKES_MOOD = "evoca_estado"

    # Relaciones de Instrumento
    FEATURES_INSTRUMENT = "presenta_instrumento"
    PLAYS_INSTRUMENT = "toca_instrumento"

    # Relaciones Temporales
    FROM_ERA = "de_epoca"

    # Relaciones de Álbum
    IN_ALBUM = "en_album"
    ALBUM_BY = "album_de"

    # Relaciones de Similitud
    SIMILAR_TO = "similar_a"
    INFLUENCED_BY = "influenciado_por"
