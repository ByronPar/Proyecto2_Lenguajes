class Estado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.transiciones = []
        self.tipo = "normal"