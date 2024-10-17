# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod

from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, \
    NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError

class ReglaValidacion(ABC):

    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada: int = _longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("La clave debe tener una longitud de más caracteres")

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")

    @abstractmethod
    def es_valida(self, clave: str) ->bool:
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        return True


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave):
        especiales = "@_#$%"
        if not any(char in especiales for char in clave):
            raise NoTieneCaracterEspecialError("La clave debe contener almenos un caracter especial")

    def es_valida(self, clave: str) ->bool:
        pass


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) ->bool:
        pass

    def es_valida(self, clave: str) ->bool:
        pass