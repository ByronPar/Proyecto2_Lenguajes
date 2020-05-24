import os

# PRIMER PASO VERIFICAR QUE MI AUTOMATA EXISTA
# SEGUNDO VERIFICAR QUE MI AUTOMATA TENGA UN INICIAL, QUE TENGA TERMINALES , NO TERMINALES A AL MENOS UNO
from PIL import Image
from byron_Manejadores.estado import Estado
from byron_Manejadores.noterminal import NoTerminal
from byron_Manejadores.transicion import Transicion
from byron_Manejadores.terminal import Terminal

nombreCorrida = 0
def run():
    from byron_Manejadores.crearGramatica import Gramatica
    global GRAMATICA
    GRAMATICA = Gramatica("Byron")
    ruta = input("\n Ingrese el nombre de su Gramatica:     ")
    os.system("cls")
    if not Gramatica.verificar(ruta):
        GRAMATICA = Gramatica.gramaticaUtilizar(ruta)
        if Gramatica.verificarInicial(GRAMATICA) == True and Gramatica.verificarNoTerminales(
                GRAMATICA) == True and Gramatica.verificarTerminales(GRAMATICA) == True:
            GRAMATICA = AutomataPila.llenarAutomataPila(GRAMATICA)
            GRAMATICA = AutomataPila.generarImagen(GRAMATICA)
            print("Automata Pila Generado Correctamente")
        else:
            print("Error la Gramatica no posee los datos Suficientes")
    else:
        print("Error la Gramatica no esta Registrada")


def imagen():
    from byron_Manejadores.crearGramatica import Gramatica
    global GRAMATICA
    ruta = input("\n Ingrese el nombre de su Gramatica:     ")
    os.system("cls")
    if not Gramatica.verificar(ruta):
        GRAMATICA = Gramatica.gramaticaUtilizar(ruta)
        if GRAMATICA.automataPila.direccionImagenGrafo != "":
            # ABRIRE LA IMAGEN
            abrir = Image.open(GRAMATICA.automataPila.direccionImagenGrafo)
            abrir.show()
            datosAutomata = AutomataPila.datosAutomataPila(GRAMATICA.automataPila)
            print(datosAutomata)


        else:
            print("Error la Gramatica no posee una imagen creada")
    else:
        print("Error la Gramatica no esta Registrada")


def cadenas():
    from byron_Manejadores.crearGramatica import Gramatica
    global GRAMATICA
    ruta = input("\n Ingrese el nombre de su Gramatica:     ")
    os.system("cls")
    if not Gramatica.verificar(ruta):
        GRAMATICA = Gramatica.gramaticaUtilizar(ruta)
        if Gramatica.verificarInicial(GRAMATICA) == True and Gramatica.verificarNoTerminales(
                GRAMATICA) == True and Gramatica.verificarTerminales(GRAMATICA) == True:
            GRAMATICA = AutomataPila.llenarAutomataPila(GRAMATICA)  # genero mi automata pila en caso no se haya creado
            cadena = input("\n Ingrese la cadena que desee evaluar :")
            listaCadena = cadena.strip()
            cadena = []
            otro = listaCadena.split(sep=' ')
            listaCadena = ""
            for _ in otro:
                cadena.append(_)
                listaCadena = listaCadena + _
            cadena.append(" ")

            if AutomataPila.verificarCadena(GRAMATICA, GRAMATICA.automataPila, cadena):
                print("  CADENA    correcta")
                AutomataPila.arbol(GRAMATICA, GRAMATICA.automataPila, cadena)
                AutomataPila.reporte(GRAMATICA, GRAMATICA.automataPila, cadena, listaCadena)
            else:
                AutomataPila.reporteIncorrecto(GRAMATICA, GRAMATICA.automataPila, cadena, listaCadena)
                print("  CADENA    INCORRECTA")
        else:
            print("Error la Gramatica no posee los datos Suficientes")
    else:
        print("Error la Gramatica no esta Registrada")


class AutomataPila:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estados = [Estado("i"), Estado("p"), Estado("q"), Estado("f")]
        self.alfabeto = []
        self.simbolosPila = []
        self.transiciones = []
        self.estadoInicial = [Estado("i")]
        self.estadoAceptacion = [Estado("f")]
        self.pila = []
        self.direccionImagenGrafo = ""
        self.ultimaCadenaAnalizada = ""

    @staticmethod
    def reporte(gramatica, automatapila, cadena, cadena2):
        global nombreCorrida
        pila = ["#", gramatica.simboloInicial]
        datos = 'PILA$ ENTRADA$ TRANSICION'
        datos = datos + "\n\u03BB$ " + cadena2 + "$ (i, \u03BB, \u03BB; p, #)"
        datos = datos + "\n" + pila[0] + "$ " + cadena2 + "$ (p, \u03BB, \u03BB; q, " + gramatica.simboloInicial + ")"
        topePila = gramatica.simboloInicial
        contador = 0
        while contador < len(cadena) and len(pila) > 1:
            comprobarPaso = False
            primero = False
            segundo = False

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == topePila:

                        datos = datos + "\n"
                        largoPila = len(pila)
                        for _ in pila:
                            datos = datos + pila[largoPila - 1]
                            largoPila = largoPila - 1
                        datos = datos + "$ "
                        posCadena = contador
                        while posCadena < len(cadena):
                            datos = datos + cadena[posCadena]
                            posCadena = posCadena + 1
                        comprobarPaso = True
                        pila.pop()
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            nuevoTopePilaCompleto = ""
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                                nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)

                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                        else:
                            topePila = pila[len(pila) - 1]
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"

                        primero = True
                        break

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == "epsilon":
                        comprobarPaso = True
                        valor = len(transicion.nuevoTopePila)
                        datos = datos + "\n"
                        largoPila = len(pila)
                        for _ in pila:
                            datos = datos + pila[largoPila - 1]
                            largoPila = largoPila - 1
                        datos = datos + "$ "
                        posCadena = contador
                        while posCadena < len(cadena):
                            datos = datos + cadena[posCadena]
                            posCadena = posCadena + 1
                        if transicion.nuevoTopePila[0] != "epsilon":
                            nuevoTopePilaCompleto = ""
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                                nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                        else:
                            topePila = pila[len(pila) - 1]
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                        segundo = True
                        break

            if primero == False and segundo == False:

                repitencia = 0
                listaRepitencia = []
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                        listaRepitencia.append(transicion)
                        repitencia = repitencia + 1
                if repitencia == 1:
                    for transicion in automatapila.transiciones:
                        if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:

                            datos = datos + "\n"
                            largoPila = len(pila)
                            for _ in pila:
                                datos = datos + pila[largoPila - 1]
                                largoPila = largoPila - 1
                            datos = datos + "$ "
                            posCadena = contador
                            while posCadena < len(cadena):
                                datos = datos + cadena[posCadena]
                                posCadena = posCadena + 1

                            pila.pop()
                            valor = len(transicion.nuevoTopePila)
                            if transicion.nuevoTopePila[0] != "epsilon":
                                nuevoTopePilaCompleto = ""
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                    nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                            else:
                                topePila = pila[len(pila) - 1]
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                            break
                elif repitencia > 1:
                    encontre = False
                    for transicion in listaRepitencia:
                        if transicion.nuevoTopePila[0] != "epsilon":
                            if cadena[contador] == transicion.nuevoTopePila[0]:

                                datos = datos + "\n"
                                largoPila = len(pila)
                                for _ in pila:
                                    datos = datos + pila[largoPila - 1]
                                    largoPila = largoPila - 1
                                datos = datos + "$ "
                                posCadena = contador
                                while posCadena < len(cadena):
                                    datos = datos + cadena[posCadena]
                                    posCadena = posCadena + 1
                                nuevoTopePilaCompleto = ""
                                pila.pop()
                                valor = len(transicion.nuevoTopePila)
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                    nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                                encontre = True
                                break

                    if not encontre:
                        for transicion in listaRepitencia:
                            if transicion.nuevoTopePila[0] == "epsilon":

                                datos = datos + "\n"
                                largoPila = len(pila)
                                for _ in pila:
                                    datos = datos + pila[largoPila - 1]
                                    largoPila = largoPila - 1
                                datos = datos + "$ "
                                posCadena = contador
                                while posCadena < len(cadena):
                                    datos = datos + cadena[posCadena]
                                    posCadena = posCadena + 1
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                                pila.pop()
                                topePila = pila[len(pila) - 1]
                                break

            if comprobarPaso:
                contador = contador + 1
        datos = datos + "\n#$ -----$ (q, \u03BB, #; f, \u03BB)"
        datos = datos + "\n-----$ -----$ ACEPTACION"
        if pila[0] == "#":
            pila.pop()

        newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
        nombreCorrida = nombreCorrida + 1
        arch = open(newrut, 'w', encoding='utf-8')
        arch.write(datos)
        arch.close()

    @staticmethod
    def reporteIncorrecto(gramatica, automatapila, cadena, cadena2):
        global nombreCorrida
        pila = ["#", gramatica.simboloInicial]
        datos = 'PILA$ ENTRADA$ TRANSICION'

        for i in cadena:
            if Terminal.verificarTerminal(gramatica.terminales, i):
                newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
                nombreCorrida = nombreCorrida + 1
                arch = open(newrut, 'w', encoding='utf-8')
                arch.write(datos)
                arch.close()
                return True
        datos = datos + "\n\u03BB$ " + cadena2 + "$ (i, \u03BB, \u03BB; p, #)"
        datos = datos + "\n" + pila[0] + "$ " + cadena2 + "$ (p, \u03BB, \u03BB; q, " + gramatica.simboloInicial + ")"

        topePila = gramatica.simboloInicial
        contador = 0
        while contador < len(cadena) and len(pila) > 1:
            comprobarPaso = False
            primero = False
            segundo = False
            tercero = False

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == topePila:
                        datos = datos + "\n"
                        largoPila = len(pila)
                        for _ in pila:
                            datos = datos + pila[largoPila - 1]
                            largoPila = largoPila - 1
                        datos = datos + "$ "
                        posCadena = contador
                        while posCadena < len(cadena):
                            datos = datos + cadena[posCadena]
                            posCadena = posCadena + 1
                        comprobarPaso = True
                        pila.pop()
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            nuevoTopePilaCompleto = ""
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                                nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                        else:
                            topePila = pila[len(pila) - 1]
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                        primero = True
                        break

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == "epsilon":
                        comprobarPaso = True
                        valor = len(transicion.nuevoTopePila)
                        datos = datos + "\n"
                        largoPila = len(pila)
                        for _ in pila:
                            datos = datos + pila[largoPila - 1]
                            largoPila = largoPila - 1
                        datos = datos + "$ "
                        posCadena = contador
                        while posCadena < len(cadena):
                            datos = datos + cadena[posCadena]
                            posCadena = posCadena + 1
                        if transicion.nuevoTopePila[0] != "epsilon":
                            nuevoTopePilaCompleto = ""
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                                nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                        else:
                            topePila = pila[len(pila) - 1]
                            datos = datos + "$ (" + transicion.estadoInicial + ", " + transicion.simboloEntrada + ", " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                        segundo = True
                        break

            if primero == False and segundo == False:

                repitencia = 0
                listaRepitencia = []
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                        listaRepitencia.append(transicion)
                        repitencia = repitencia + 1
                if repitencia == 1:
                    for transicion in automatapila.transiciones:
                        if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                            datos = datos + "\n"
                            largoPila = len(pila)
                            for _ in pila:
                                datos = datos + pila[largoPila - 1]
                                largoPila = largoPila - 1
                            datos = datos + "$ "
                            posCadena = contador
                            while posCadena < len(cadena):
                                datos = datos + cadena[posCadena]
                                posCadena = posCadena + 1
                            pila.pop()
                            valor = len(transicion.nuevoTopePila)
                            if transicion.nuevoTopePila[0] != "epsilon":
                                nuevoTopePilaCompleto = ""
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                    nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                            else:
                                topePila = pila[len(pila) - 1]
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                            tercero = True
                            break
                elif repitencia > 1:
                    encontre = False
                    for transicion in listaRepitencia:
                        if transicion.nuevoTopePila[0] != "epsilon":
                            if cadena[contador] == transicion.nuevoTopePila[0]:
                                datos = datos + "\n"
                                largoPila = len(pila)
                                for _ in pila:
                                    datos = datos + pila[largoPila - 1]
                                    largoPila = largoPila - 1
                                datos = datos + "$ "
                                posCadena = contador
                                while posCadena < len(cadena):
                                    datos = datos + cadena[posCadena]
                                    posCadena = posCadena + 1
                                nuevoTopePilaCompleto = ""
                                pila.pop()
                                valor = len(transicion.nuevoTopePila)
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                    nuevoTopePilaCompleto = nuevoTopePilaCompleto + str(_)
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", " + nuevoTopePilaCompleto + ")"
                                tercero = True
                                encontre = True
                                break

                    if not encontre:
                        for transicion in listaRepitencia:
                            if transicion.nuevoTopePila[0] == "epsilon":
                                datos = datos + "\n"
                                largoPila = len(pila)
                                for _ in pila:
                                    datos = datos + pila[largoPila - 1]
                                    largoPila = largoPila - 1
                                datos = datos + "$ "
                                posCadena = contador
                                while posCadena < len(cadena):
                                    datos = datos + cadena[posCadena]
                                    posCadena = posCadena + 1
                                datos = datos + "$ (" + transicion.estadoInicial + ", \u03BB, " + transicion.topePila + "; " + transicion.estadoFinal + ", \u03BB)"
                                pila.pop()
                                topePila = pila[len(pila) - 1]
                                tercero = True
                                encontre = True
                                break

                    if not encontre:
                        newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
                        nombreCorrida = nombreCorrida + 1
                        arch = open(newrut, 'w', encoding='utf-8')
                        arch.write(datos)
                        arch.close()
                        return

                else:
                    newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
                    nombreCorrida = nombreCorrida + 1
                    arch = open(newrut, 'w', encoding='utf-8')
                    arch.write(datos)
                    arch.close()
                    return True

            if primero == True or segundo == True or tercero == True:  # COMPROBAR QUE ALGO SE ENCONTRO
                print(" ")
            else:
                newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
                nombreCorrida = nombreCorrida + 1
                arch = open(newrut, 'w', encoding='utf-8')
                arch.write(datos)
                arch.close()
                return True

            if comprobarPaso:
                contador = contador + 1

        if pila[0] == "#" and len(pila) < 2:
            datos = datos + "\n#$ -----$ (q, \u03BB, #; f, \u03BB)"
            datos = datos + "\n-----$ -----$ ACEPTACION"
            pila.pop()
        if pila:
            newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
            nombreCorrida = nombreCorrida + 1
            arch = open(newrut, 'w', encoding='utf-8')
            arch.write(datos)
            arch.close()
            return True
        else:
            newrut = 'C:/Users/ByronJosué/Desktop/reporte-entrada' + str(nombreCorrida) + ".CSV"
            nombreCorrida = nombreCorrida + 1
            arch = open(newrut, 'w', encoding='utf-8')
            arch.write(datos)
            arch.close()
            return True

    @staticmethod
    def llenarAutomataPila(gramatica):
        # --------------------------------------    paso # 1  -----------------------

        #             Designe el alfabetp del automata pila como los simbolos terminales de mi Gramatica , y los simbolos de pila de
        #             mi automata pila como los simbolos terminales y no terminales de mi gramatica, junto con el simbolo especial #
        #             (podemos suponer que # no es un simbolo terminal o no terminal de mi gramatica).
        NuevoautomataPila = AutomataPila(gramatica.nombre)  # reinicio el automata pila
        gramatica.automataPila = NuevoautomataPila
        for i in list(gramatica.terminales):
            terminal = i
            gramatica.automataPila.alfabeto.append(terminal.terminal)

        for i in list(gramatica.terminales):
            terminal = i
            gramatica.automataPila.simbolosPila.append(terminal.terminal)

        for i in list(gramatica.noTerminales):
            noTerminal = i
            gramatica.automataPila.simbolosPila.append(noTerminal.nombre)
        gramatica.automataPila.simbolosPila.append("#")

        # --------------------------------------    paso # 2  -----------------------

        # Designe los estados de mi automataPila como i,p,q,f donde i es el estado inicial y f el unico estado de aceptación
        # Los creo direcctamente en mi constructor aqui no hago nada mas

        # --------------------------------------    paso # 3  -----------------------

        # Introduzca la transicion (i,epsilon,epsilon ; p , #)

        nuevaTransicion = Transicion("i", "epsilon", "epsilon", "p", list(["#"]))
        gramatica.automataPila.transiciones.append(nuevaTransicion)

        # --------------------------------------    paso # 4  -----------------------

        # Introduzca una transicion (p,epsilon,epsilon ; q, S) donde S es el símbolo inicial de mi gramatica

        nuevaTransicion = Transicion("p", "epsilon", "epsilon", "q", list([gramatica.simboloInicial]))
        gramatica.automataPila.transiciones.append(nuevaTransicion)

        # --------------------------------------    paso # 5  -----------------------

        # introducir una transicion de la forma (q,epsilon,noTerminal ; q,w) para producción existente en mi gramatica

        for noTerminal in list(gramatica.noTerminales):
            for produccion in list(noTerminal.producciones):
                nuevaTransicion = Transicion("q", "epsilon", noTerminal.nombre, "q", list(produccion.produccion))
                gramatica.automataPila.transiciones.append(nuevaTransicion)

        # --------------------------------------    paso # 6  -----------------------

        # Introducir una transicion de la forma (q, x, x; q, epsilon) para cada terminal x de mi gramatica(es decir, para
        # cada simbolo del alfabeto de mi automata pila)

        for terminal in list(gramatica.terminales):
            nuevaTransicion = Transicion("q", terminal.terminal, terminal.terminal, "q", list(["epsilon"]))
            gramatica.automataPila.transiciones.append(nuevaTransicion)

        # --------------------------------------    paso # 7  -----------------------

        # introducir la transicion (q,epsilon,#; f , epsilon)

        nuevaTransicion = Transicion("q", "epsilon", "#", "f", list(["epsilon"]))
        gramatica.automataPila.transiciones.append(nuevaTransicion)
        return gramatica

    @staticmethod
    def generarImagen(gramatica):
        from graphviz import Digraph

        f = Digraph(format='png', name=gramatica.automataPila.nombre)
        f.attr(rankdir='LR', size='8,5')

        f.attr('node', shape='none')
        f.node(' ')

        # Creación de nodos
        f.attr('node', shape='circle')
        f.node('i', width='1.1', height='1.1')
        f.node('q', width='2.5', height='2.5')
        f.node('p', width='1.1', height='1.1')

        # Creación de nodos (aceptación)
        f.attr('node', shape='doublecircle')
        f.node('f', width='1.1', height='1.1')

        # Creación de los enlaces (transiciones)
        f.edge(' ', 'i', "Inicio")
        for transicion in gramatica.automataPila.transiciones:
            # print('lambda: \u03BB')
            info = ""
            if transicion.simboloEntrada == "epsilon":
                info = info + "\u03BB" + ","
            else:
                info = info + transicion.simboloEntrada + ","

            if transicion.topePila == "epsilon":
                info = info + "\u03BB" + ";"
            else:
                info = info + transicion.topePila + ";"

            poner = ""
            for i in transicion.nuevoTopePila:
                if i == "epsilon":
                    poner = poner + "\u03BB"
                else:
                    poner = poner + str(i)
            info = info + poner
            if transicion.estadoInicial == "q" and transicion.estadoFinal == "q":
                f.edge(transicion.estadoInicial, transicion.estadoFinal, info, tailport='w', headport='e')
            else:
                f.edge(transicion.estadoInicial, transicion.estadoFinal, info, minlen='3')
        # Creación del grafo
        f.render()
        gramatica.automataPila.direccionImagenGrafo = "C:/Users/ByronJosué/Documents/PyCharm_Projects/Proyecto2_Lenguajes/byron_Menus/" + gramatica.nombre + ".gv.png"
        return gramatica

    @staticmethod
    def datosAutomataPila(automatapila):
        # pintare estados
        datoTotal = "\nS : {"
        for i in automatapila.estados:
            estado = i
            datoTotal = datoTotal + estado.nombre + ", "
        datoTotal = datoTotal + "}"

        # pintare el alfabeto de maquina
        datoTotal = datoTotal + "\nΣ : {"
        for i in automatapila.alfabeto:
            datoTotal = datoTotal + i + ", "
        datoTotal = datoTotal + "}"

        # pintare simbolos de pila
        datoTotal = datoTotal + "\nΓ : {"
        for i in automatapila.simbolosPila:
            datoTotal = datoTotal + i + ", "
        datoTotal = datoTotal + "}"

        # pintare mi estado inicial
        datoTotal = datoTotal + "\n L: i"

        # pintare mi estado de Aceptación
        datoTotal = datoTotal + "\nF : f"

        # pintare mis transiciones de mi automata Pila
        datoTotal = datoTotal + "\nT :   {"

        for transicion in automatapila.transiciones:
            datoTotal = datoTotal + "\n      " + transicion.estadoInicial + ", "
            if transicion.simboloEntrada == "epsilon":
                datoTotal = datoTotal + "\u03BB" + ", "
            else:
                datoTotal = datoTotal + transicion.simboloEntrada + ", "
            if transicion.topePila == "epsilon":
                datoTotal = datoTotal + "\u03BB" + "; "
            else:
                datoTotal = datoTotal + transicion.topePila + "; "
            datoTotal = datoTotal + transicion.estadoFinal + ", "
            for i in transicion.nuevoTopePila:
                if i == "epsilon":
                    datoTotal = datoTotal + "\u03BB"
                else:
                    datoTotal = datoTotal + str(i)

        datoTotal = datoTotal + "\n    }"

        return datoTotal

    @staticmethod
    def verificarCadena(gramatica, automatapila, cadena):
        for i in cadena:
            if i != " ":
                if Terminal.verificarTerminal(gramatica.terminales, i):
                    return False

        # SI LLEGA AQUI ES PORQUE TODOS MIS LETRAS SON CORRECTAS

        pila = list(automatapila.pila)
        # primero sacar de la pila y luego guardar en la pila
        # i --> p    pasa sin problemas
        # p --> q    pasa solo si encuentra un simbolo en alguna transicion del no terminal inicial

        # "EstadoInicial","Simbolo que se tomo","EstadoFinal","simbolo que debe estar en el tope pila","simbolo que se pondra en el tope pila"

        pila.append("#")
        pila.append(gramatica.simboloInicial)
        topePila = gramatica.simboloInicial
        contador = 0
        while contador < len(cadena) and len(pila) > 1:
            comprobarPaso = False
            primero = False
            segundo = False
            tercero = False

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == topePila:
                        comprobarPaso = True
                        pila.pop()
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                        else:
                            topePila = pila[len(pila) - 1]
                        primero = True
                        break

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == "epsilon":
                        comprobarPaso = True
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                        else:
                            topePila = pila[len(pila) - 1]
                        segundo = True
                        break

            if primero == False and segundo == False:

                repitencia = 0
                listaRepitencia = []
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                        listaRepitencia.append(transicion)
                        repitencia = repitencia + 1
                if repitencia == 1:
                    for transicion in automatapila.transiciones:
                        if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                            pila.pop()
                            valor = len(transicion.nuevoTopePila)
                            if transicion.nuevoTopePila[0] != "epsilon":
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                            else:
                                topePila = pila[len(pila) - 1]
                            tercero = True
                            break
                elif repitencia > 1:
                    encontre = False
                    for transicion in listaRepitencia:
                        if transicion.nuevoTopePila[0] != "epsilon":
                            if cadena[contador] == transicion.nuevoTopePila[0]:
                                pila.pop()
                                valor = len(transicion.nuevoTopePila)
                                for _ in transicion.nuevoTopePila:
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                tercero = True
                                encontre = True
                                break

                    if not encontre:
                        for transicion in listaRepitencia:
                            if transicion.nuevoTopePila[0] == "epsilon":
                                pila.pop()
                                topePila = pila[len(pila) - 1]
                                tercero = True
                                encontre = True
                                break

                    if not encontre:
                        return False

                else:
                    return False

            if primero == True or segundo == True or tercero == True:  # COMPROBAR QUE ALGO SE ENCONTRO
                print(" ")
            else:
                return False

            if comprobarPaso:
                contador = contador + 1

        if pila[0] == "#" and len(pila) < 2:
            pila.pop()
        if pila:
            return False
        else:
            return True

    @staticmethod
    def arbol(gramatica, automatapila, cadena):
        from graphviz import Digraph

        f = Digraph(format='png', name="Arbol-sintactico-" + gramatica.automataPila.nombre)
        f.attr(size='19,5')
        # Creación de nodos
        pila = ["#", gramatica.simboloInicial]
        topePila = gramatica.simboloInicial
        contador = 0
        numeroNodo = 0
        listaNumerosNodos = []

        f.attr('node', shape='none')  # NODO INICIAL SIEMPRE
        f.node(str(numeroNodo), label=gramatica.simboloInicial)

        listaNumerosNodos.append(numeroNodo)
        numeroNodo = numeroNodo + 1
        while contador < len(cadena) and len(pila) > 1:
            comprobarPaso = False
            primero = False
            segundo = False

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == topePila:
                        comprobarPaso = True
                        pila.pop()
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                        else:
                            topePila = pila[len(pila) - 1]
                        primero = True
                        break

            if not primero:
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == cadena[contador] and transicion.topePila == "epsilon":
                        comprobarPaso = True
                        valor = len(transicion.nuevoTopePila)
                        if transicion.nuevoTopePila[0] != "epsilon":
                            for _ in transicion.nuevoTopePila:
                                pila.append(transicion.nuevoTopePila[valor - 1])
                                topePila = transicion.nuevoTopePila[valor - 1]
                                valor = valor - 1
                        else:
                            topePila = pila[len(pila) - 1]
                        segundo = True
                        break

            if primero == False and segundo == False:

                repitencia = 0
                listaRepitencia = []
                for transicion in automatapila.transiciones:
                    if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                        listaRepitencia.append(transicion)
                        repitencia = repitencia + 1
                if repitencia == 1:
                    for transicion in automatapila.transiciones:
                        if transicion.simboloEntrada == "epsilon" and transicion.topePila == topePila:
                            pila.pop()
                            valor = len(transicion.nuevoTopePila)

                            if transicion.nuevoTopePila[0] != "epsilon":
                                numeroDeNodoqueViene = str(listaNumerosNodos[-1])
                                posInsertar = len(listaNumerosNodos) - 1
                                listaNumerosNodos.pop()

                                for _ in transicion.nuevoTopePila:
                                    if Terminal.verificarMayuscula(_):
                                        f.node(str(numeroNodo), label=_)
                                        f.edge(numeroDeNodoqueViene, str(numeroNodo))
                                        listaNumerosNodos.insert(posInsertar, numeroNodo)
                                        numeroNodo = numeroNodo + 1

                                    else:
                                        f.node(str(numeroNodo), label=_)
                                        f.edge(numeroDeNodoqueViene, str(numeroNodo))
                                        numeroNodo = numeroNodo + 1

                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                            else:
                                topePila = pila[len(pila) - 1]
                            break
                elif repitencia > 1:
                    encontre = False
                    for transicion in listaRepitencia:
                        if transicion.nuevoTopePila[0] != "epsilon":
                            if cadena[contador] == transicion.nuevoTopePila[0]:
                                pila.pop()
                                valor = len(transicion.nuevoTopePila)
                                numeroDeNodoqueViene = str(listaNumerosNodos[-1])
                                posInsertar = len(listaNumerosNodos) - 1
                                listaNumerosNodos.pop()
                                for _ in transicion.nuevoTopePila:
                                    if Terminal.verificarMayuscula(_):
                                        f.node(str(numeroNodo), label=_)
                                        f.edge(numeroDeNodoqueViene, str(numeroNodo))
                                        listaNumerosNodos.insert(posInsertar, numeroNodo)
                                        numeroNodo = numeroNodo + 1
                                    else:
                                        f.node(str(numeroNodo), label=_)
                                        f.edge(numeroDeNodoqueViene, str(numeroNodo))
                                        numeroNodo = numeroNodo + 1
                                    pila.append(transicion.nuevoTopePila[valor - 1])
                                    topePila = transicion.nuevoTopePila[valor - 1]
                                    valor = valor - 1
                                encontre = True
                                break

                    if not encontre:
                        for transicion in listaRepitencia:
                            if transicion.nuevoTopePila[0] == "epsilon":
                                pila.pop()
                                topePila = pila[len(pila) - 1]
                                listaNumerosNodos.pop()

                                break

            if comprobarPaso:
                contador = contador + 1

        if pila[0] == "#":
            pila.pop()

        f.render()
        direccion = 'C:/Users/ByronJosué/Documents/PyCharm_Projects/Proyecto2_Lenguajes/byron_Menus/Arbol-sintactico-' + gramatica.automataPila.nombre + ".gv.png"
        abrir = Image.open(direccion)
        abrir.show()
