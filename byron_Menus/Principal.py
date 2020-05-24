import os
import sys
from byron_Menus.menuGramaticaTipo2 import menuGramaticaTipo2


def mostrar_menu():
    print("""
########################      Menu Principal      ########################
1 Menu Gramatica Tipo2 y Automata Pila
2 Menu AFD
3 Menu Gramatica
4 Menu Validar Cadena
5 Menu Cargar Archivo
6 Menu Guardar Archivo
7 Salir 
""")


def quit():
    print("\n FIN DE LA APLICACIÓN  ")
    sys.exit(0)


class Menu:
    def __init__(self):
        self.GramaticaTipo2 = menuGramaticaTipo2()
        self.elecciones = {  # mi diccionario menu
            "1": self.gramaticaTipo2,
            # "2": self.afd,
            # "3": self.gramaticaRegular,
            # "4": self.validar,
            # "5": self.cargarArchivo,
            # "6": self.guardarArchivo,
            "7": quit
        }

    def gramaticaTipo2(self):
        os.system("cls")
        self.GramaticaTipo2.run()



    def run(self):  # Para Correr mi menu

        while True:
            mostrar_menu()
            eleccion = input("Seleccione una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
                break

            else:
                print("{0} no es una elección válida".format(eleccion))


def mostrar_Info():
    print("""
########################      DATOS DEL ESTUDIANTE      ########################


       Lenguajes formales y de Programación

       Sección :  A+
                                                                 Proyecto No.2
       Byron Josué Par Rancho  

       Carnet : 201701078


########################                                 ########################



""")




def run():  # Para Correr mi menu de Información
    mostrar_Info()
    input("\n Presione Enter Para Continuar")
    os.system("cls")
    if __name__ == "__main__":
        Menu().run()


if __name__ == "__main__":
    run()
