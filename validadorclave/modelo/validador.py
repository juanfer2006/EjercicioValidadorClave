# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada):
        self._longitud_esperada = _longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave):
        return any(char.isupper() for char in clave)

    def _contiene_minuscula(self, clave):
        return any(char.islower() for char in clave)

    def _contiene_numero(self, clave):
        return any(char.isdigit() for char in clave)

    @abstractmethod
    def es_valida(self):
        pass

class ReglaValidacionGanimedes:

    def contiene_caracter_especial(self):
        pass


