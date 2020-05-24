import os

from byron_Manejadores.terminal import Terminal


class NoTerminal:
    def __init__(self, nombre="instancia"):
        if nombre != "instancia":
            self.nombre = nombre
            self.producciones = []

    @staticmethod
    def ingresoNT(gramatica):
        listaNoTerminales = list(gramatica.noTerminales)
        listaTerminales = list(gramatica.terminales)
        nuevoNoTerminal = input("Ingrese un Nuevo NO Terminal  para su Gramatica:")
        if NoTerminal.verificarNoTerminal(listaNoTerminales, nuevoNoTerminal) == True and Terminal.verificarTerminal(
                listaTerminales, nuevoNoTerminal) == True and NoTerminal.verificarMayuscula(nuevoNoTerminal) == True:
            noTerminalNuevo = NoTerminal(nuevoNoTerminal)
            listaNoTerminales.append(noTerminalNuevo)  # CREO UN OBJETO NO TERMINAL Y LO AGREGO A MI LISTA
            os.system("cls")
            print("\n                  Nuevo NoTerminal Agregado Correctamente")
            return listaNoTerminales
        else:
            print("Este NoTerminal no es valido debe ingresar un Nuevo NoTerminal:")
            return listaNoTerminales

    @staticmethod
    def verificarMayuscula(cadena):
        try:
            if cadena[0].isupper():
                return True
            return False
        except IndexError:
            return False

    @staticmethod
    def verificarNoTerminal(listaNoTerminales, nombre):
        if listaNoTerminales:
            for j in listaNoTerminales:
                noTerminal = j
                if noTerminal.nombre == nombre:
                    return False
            return True

        else:
            return True

    @staticmethod
    def ntInicial(gramatica):
        listaNoTerminales = list(gramatica.noTerminales)
        nuevoNoTerminalInicial = input(
            "\n Ingrese el NoTerminal que desea que sea su nuevo  Inicial para su Gramatica:")
        if not NoTerminal.verificarNoTerminal(listaNoTerminales, nuevoNoTerminalInicial):
            gramatica.simboloInicial = nuevoNoTerminalInicial
            print("\n Nuevo No Terminal Inicial Registrado Exitosamente")
            return gramatica
        else:
            os.system("cls")
            print("\n El NoTerminal no existe debe ingresar un NoTerminal Registrado")
            return gramatica

