class Transicion:
    def __init__(self, estadoInicial, simboloEntrada, topePila, estadoFinal, nuevoTopePila):
        self.estadoInicial = estadoInicial
        self.simboloEntrada = simboloEntrada
        self.topePila = topePila
        self.estadoFinal = estadoFinal
        self.nuevoTopePila = list(nuevoTopePila)  # HACERLO LISTA
