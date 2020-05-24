import os

from byron_Manejadores.crearAutomataPila import AutomataPila
from byron_Manejadores.noterminal import NoTerminal
from byron_Manejadores.produccion import Produccion
from byron_Manejadores.terminal import Terminal

listaGRAMATICA = []

ruta = ""


def regresar():
    from byron_Menus.menuGramaticaTipo2 import menuGramaticaTipo2
    os.system("cls")
    menuGramaticaTipo2().run()


def menu():
    print("""
            ########################      Menu de GRAMATICA      ########################
            1 Ingresar NT   
            2 Ingresar Terminales
            3 NT Inicial
            4 Producciones
            5 Borrar Producciones
            6 Regresar
            """)


class menuGramatica:
    def __init__(self):
        self.noTerminal = NoTerminal()
        self.terminal = Terminal()
        self.Producciones = Produccion()
        self.gramatica = Gramatica()
        self.elecciones = {  # mi diccionario menu
            "1": self.ingresoNT,
            "2": self.ingresoTerminales,
            "3": self.ntInicial,
            "4": self.producciones,
            "5": self.borrarProducciones,
            "6": regresar
        }

    def ejecutarMenu(self):
        while True:
            menu()
            eleccion = input("Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break

            else:
                print("{0} no es una elección válida".format(eleccion))

    def run(self):
        global GRAMATICA
        ruta = input("\n Ingrese un nombre para SU GRAMATICA DE TIPO 2:     ")
        os.system("cls")
        if Gramatica.verificar(ruta):
            Gramatica.crear(ruta)
            GRAMATICA = Gramatica.gramaticaUtilizar(ruta)
            self.ejecutarMenu()
        else:
            GRAMATICA = Gramatica.gramaticaUtilizar(ruta)
            print("Se Modificara Su Gramatica Regular")
            self.ejecutarMenu()

    def ingresoNT(self):
        global GRAMATICA
        os.system("cls")
        GRAMATICA.noTerminales = self.noTerminal.ingresoNT(GRAMATICA)
        self.ejecutarMenu()

    def ingresoTerminales(self):
        global GRAMATICA
        os.system("cls")
        GRAMATICA.terminales = self.terminal.ingresoTerminales(GRAMATICA)
        self.ejecutarMenu()

    def ntInicial(self):
        global GRAMATICA
        os.system("cls")
        GRAMATICA = self.noTerminal.ntInicial(GRAMATICA)
        self.ejecutarMenu()

    def producciones(self):
        global GRAMATICA
        os.system("cls")
        GRAMATICA.noTerminales = self.Producciones.producciones(GRAMATICA)
        self.ejecutarMenu()

    def borrarProducciones(self):
        global GRAMATICA
        os.system("cls")
        GRAMATICA.noTerminales = self.Producciones.operarborrarProduccion(GRAMATICA)
        self.ejecutarMenu()


class Gramatica:

    def __init__(self, nombre="instancia"):

        if nombre != "instancia":
            self.tipo = "2"
            self.nombre = nombre
            self.simboloInicial = ""
            self.noTerminales = []
            self.terminales = []
            # self.recursiva = Gramatica
            # self.verificarRecursividad = 0
            self.automataPila = AutomataPila(nombre)

    @staticmethod
    def pintarDatos(Namegramatica):
        global listaGRAMATICA
        for i in listaGRAMATICA:
            gramatica = i
            if gramatica.nombre == Namegramatica:
                print("\n No Terminales:   ")
                for j in gramatica.noTerminales:
                    noterminal = j
                    print("\n    " + noterminal.nombre)

                print("\n    Terminales:   ")
                for j in gramatica.terminales:
                    terminal = j
                    print("\n    " + terminal.terminal)

                print("\n    Producciones:   ")
                for j in gramatica.noTerminales:
                    noTerminal = j
                    if noTerminal.producciones:
                        for k in noTerminal.producciones:
                            produccion = k
                            print("   \n   " + noTerminal.nombre + " > " + produccion.produccion)

    @staticmethod
    def gramaticaUtilizar(nombreGra):
        global listaGRAMATICA
        for i in listaGRAMATICA:
            gramatica = i
            if gramatica.nombre == nombreGra:
                return gramatica

    @staticmethod
    def verificar(nombreGramatica):
        global listaGRAMATICA
        if listaGRAMATICA:
            for i in listaGRAMATICA:
                gramatica = i
                if gramatica.nombre == nombreGramatica:
                    return False
            return True
        else:
            return True

    @staticmethod
    def crear(nombre):
        global listaGRAMATICA
        nuevoG = Gramatica(nombre)
        listaGRAMATICA.append(nuevoG)

    @staticmethod
    def verificarInicial(gramatica):
        if gramatica.simboloInicial != "":
            return True
        else:
            return False

    @staticmethod
    def verificarNoTerminales(gramatica):
        listaNoTerminales = list(gramatica.noTerminales)
        for _ in listaNoTerminales:
            return True
        return False

    @staticmethod
    def verificarTerminales(gramatica):
        listaTerminales = list(gramatica.terminales)
        for _ in listaTerminales:
            return True
        return False

    @staticmethod
    def cargaMasiva():
        global GRAMATICA
        ruta = input("\n  Ingrese la dirección donde se encuentre su Archivo .grm     ")
        extension = "grm"
        if ruta[len(ruta) - 3:len(ruta)] == extension:  # VERIFICO QUE SEA UNA Ruta con la extension adecuada
            if os.path.isfile(ruta):  # Verificar que el archivo exista
                f = open(ruta, 'r')
                conte = f.read()  # leo el contenido de mi archivo
                f.close()
                name = os.path.split(ruta)
                name2 = name[1].split(sep='.')

                if Gramatica.verificar(name2[0]):
                    Gramatica.crear(name2[0])
                    GRAMATICA = Gramatica.gramaticaUtilizar(name2[0])
                    GRAMATICA = Gramatica.cargarDatosMasivos(conte, GRAMATICA)
                else:
                    print("\n     El  archivo ya existe ingrese un nuevo archivo  ")
            else:
                print("\n     El  archivo no existe ingrese una dirección valida  ")
        else:
            print("\n  Debe Ingresar Un archivo con la extension solicitada,    VUELVA A INTENTARLO")

    @staticmethod
    def cargarDatosMasivos(contenido, gramatica):
        try:
            lineas = contenido.split(sep='\n')
            listaNoTerminales = list(gramatica.noTerminales)
            listaTerminales = list(gramatica.terminales)

            for linea in lineas:
                separados = linea.split(sep='>')
                parte1 = separados[0].strip()
                parte2 = separados[1].strip()
                if NoTerminal.verificarNoTerminal(listaNoTerminales, parte1) == True and Terminal.verificarTerminal(
                        listaTerminales, parte1) == True and NoTerminal.verificarMayuscula(parte1) == True:
                    noTerminalNuevo = NoTerminal(parte1)
                    listaNoTerminales.append(noTerminalNuevo)  # CREO UN OBJETO NO TERMINAL Y LO AGREGO A MI LISTA

            for linea in lineas:
                separados = linea.split(sep='>')
                parte1 = separados[0].strip()
                parte2 = separados[1].strip()
                multiple = False
                for i in parte2:
                    if i == "|":
                        multiple = True

                if parte2 != "epsilon" and multiple == False:
                    try:
                        sinEspacios = parte2.strip()
                        parte2 = sinEspacios.split(sep=' ')
                        for _ in parte2:
                            if _ != "epsilon" and _ != "":
                                if _[0].isupper():
                                    if NoTerminal.verificarNoTerminal(listaNoTerminales, _):
                                        if Terminal.verificarTerminal(listaTerminales, _):
                                            noTerminalNuevo = NoTerminal(_)
                                            listaNoTerminales.append(noTerminalNuevo)

                                else:
                                    if NoTerminal.verificarNoTerminal(listaNoTerminales,
                                                                      _) == True and Terminal.verificarTerminal(
                                        listaTerminales, _) == True and Terminal.verificarTodasMayusculas(
                                        _) == False:
                                        terminalNuevo = Terminal(_)
                                        listaTerminales.append(terminalNuevo)

                    except IndexError:
                        return gramatica

                elif multiple:
                    try:
                        separacion = parte2.split(sep='|')
                        for k in separacion:
                            sinEspacios = k.strip()
                            parte2 = sinEspacios.split(sep=' ')
                            for _ in parte2:
                                if _ != "epsilon" and _ != "":
                                    if _[0].isupper():
                                        if NoTerminal.verificarNoTerminal(listaNoTerminales, _):
                                            if Terminal.verificarTerminal(listaTerminales, _):
                                                noTerminalNuevo = NoTerminal(_)
                                                listaNoTerminales.append(noTerminalNuevo)
                                    else:
                                        if NoTerminal.verificarNoTerminal(listaNoTerminales,
                                                                          _) == True and Terminal.verificarTerminal(
                                            listaTerminales, _) == True and Terminal.verificarTodasMayusculas(
                                            _) == False:
                                            terminalNuevo = Terminal(_)
                                            listaTerminales.append(terminalNuevo)
                    except IndexError:
                        return gramatica
            noTerminal = listaNoTerminales[0]
            gramatica.simboloInicial = noTerminal.nombre
            gramatica.noTerminales = listaNoTerminales
            gramatica.terminales = listaTerminales

            for linea in lineas:
                listaNoTerminales = Produccion.enlistarProduccion(gramatica, linea)

            gramatica.noTerminales = listaNoTerminales

            return gramatica
        except IndexError:
            return gramatica


GRAMATICA = Gramatica("Byron")
