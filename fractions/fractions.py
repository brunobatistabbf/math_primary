from __future__ import annotations

class fraction():
    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador
        self.fraction_type = self.fraction_type(numerador, denominador)


class fraction_type(fraction):
    def proper_fraction(self, numerador, denominador):
        if(numerador < denominador):
            fraction_type = "proper"
            return fraction_type
        else:
            fraction_type = "No proper"
            return fraction_type

    def improper_fraction(self, numerador, denominador):
        if(numerador > denominador):
            fraction_type = "improper"
            return fraction_type
        else:
            fraction_type = "No improper"
            return fraction_type