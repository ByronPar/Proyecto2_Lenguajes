import os

from byron_Manejadores.crearGramatica import menuGramatica


def regresar():
    from byron_Menus.Principal import Menu
    os.system("cls")
    Menu().run()


def menu():
    print("""
            ########################      Menu de GRAMATICA TIPO 2      ########################
            1 Ingresar / modificar gramatica   
            2 Generar Autómata de Pila
            3 Visualizar autómata
            4 Validar Cadena
            5 Carga Masiva
            6 Regresar
            """)




class menuGramaticaTipo2:
    def __init__(self):
        self.gramaticaTipo2 = menuGramatica()
        self.elecciones = {  # mi diccionario menu
            "1": self.ingresoGramatica,
            "2": self.generarPila,
            "3": self.visualizarAutomata,
            "4": self.validarCadena,
            "5": self.cargaMasiva,
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
        self.ejecutarMenu()

    def ingresoGramatica(self):
        os.system("cls")
        self.gramaticaTipo2.run()

    def cargaMasiva(self):
        from byron_Manejadores.crearGramatica import Gramatica
        os.system("cls")
        Gramatica.cargaMasiva()
        self.run()

    def generarPila(self):
        from byron_Manejadores.crearAutomataPila import run
        os.system("cls")
        run()
        self.run()

    def visualizarAutomata(self):
        from byron_Manejadores.crearAutomataPila import imagen
        os.system("cls")
        imagen()
        self.run()

    def validarCadena(self):
        from byron_Manejadores.crearAutomataPila import cadenas
        os.system("cls")
        cadenas()
        self.run()

