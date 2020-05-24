import os




class Terminal:
    def __init__(self, terminal="instancia"):
        if terminal != "instancia":
            self.terminal = terminal

    @staticmethod
    def ingresoTerminales(gramatica):
        from byron_Manejadores.noterminal import NoTerminal
        listaTerminales = list(gramatica.terminales)
        listaNoTerminales = list(gramatica.noTerminales)
        nuevoTerminal = input("Ingrese un nuevo terminal para su Gramatica:")

        if NoTerminal.verificarNoTerminal(listaNoTerminales, nuevoTerminal) == True and Terminal.verificarTerminal(
                listaTerminales, nuevoTerminal) == True and Terminal.verificarTodasMayusculas(
                nuevoTerminal) == False :  # compruebo que no exista en ningun lado
            terminalNuevo = Terminal(nuevoTerminal)
            listaTerminales.append(terminalNuevo)  # creo un objeto terminal y lo meto en mi lista de terminales
            os.system("cls")
            print("\n                  Nuevo Terminal Agregado Correctamente")
            return listaTerminales
        else:
            print("Este Terminal no es valido debe ingresar un Nuevo Terminal:")
            return listaTerminales

    @staticmethod
    def verificarTerminal(listaTerminales, nombre):
        if listaTerminales:
            for j in listaTerminales:
                terminal = j
                if terminal.terminal == nombre:
                    return False
            return True
        else:
            return True

    @staticmethod
    def verificarTodasMayusculas(cadena):
        try:
            for i in cadena:
                if i.isupper():
                    return True
            return False
        except IndexError:
            return True

    @staticmethod
    def verificarMayuscula(cadena):
        try:
            if cadena[0].isupper():
                return True
            return False
        except IndexError:
            return True

