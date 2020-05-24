import os


class Produccion:
    def __init__(self, noTerminal="instancia", produccion=None):
        if produccion is None:
            produccion = []
        if noTerminal != "instancia" and produccion != "instancia":
            self.noTerminal = noTerminal
            self.produccion = list(produccion)

    @staticmethod
    def producciones(gramatica):
        listaNoTerminales = list(gramatica.noTerminales)
        nuevaP = input("\nIngrese una nueva Produccion:")
        if Produccion.verificarProduccion(gramatica, nuevaP):
            if Produccion.datosValidos(gramatica, nuevaP) == True and Produccion.verificarExistenciaProduccion(
                    gramatica, nuevaP) == False:
                print("\n   Registro de Producciones Realizado con Exito")
                listaNoTerminales = Produccion.enlistarProduccion(gramatica, nuevaP)
                return listaNoTerminales
            else:
                os.system("cls")
                print("\n     Error al Ingresar Producción Vuelva a intentarlo")
                return listaNoTerminales

        else:
            os.system("cls")
            print("\n     Error al Ingresar Producción Vuelva a intentarlo")
            return listaNoTerminales

    @staticmethod
    def verificarProduccion(gramatica, produccion):  # VERIFICA LOS DATOS DE MI PARTE 1 QUE EXISTA MI NO TERMINAL
        from byron_Manejadores.noterminal import NoTerminal
        try:
            separacion = produccion.split(sep='>')
            parte1 = separacion[0].strip()
            parte2 = separacion[1].strip()
        except IndexError:
            return False
        listaNoTerminales = list(gramatica.noTerminales)
        if not NoTerminal.verificarNoTerminal(listaNoTerminales, parte1):
            return True
        else:
            return False

    @staticmethod
    def datosValidos(gramatica,
                     nuevaP):  # solo me verifica la segunda Parte de que mis datos existan y esten registrados
        from byron_Manejadores.noterminal import NoTerminal
        from byron_Manejadores.terminal import Terminal
        listaNoTerminales = list(gramatica.noTerminales)
        listaTerminales = list(gramatica.terminales)
        try:
            separacion = nuevaP.split(sep='>')
            parte1 = separacion[0].strip()
            parte2 = separacion[1].strip()
        except IndexError:
            return False
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
                        encontrado = False
                        if _[0].isupper():
                            if not NoTerminal.verificarNoTerminal(listaNoTerminales, _):
                                encontrado = True
                            if not encontrado:
                                return False
                        else:
                            if not Terminal.verificarTerminal(listaTerminales, _):
                                encontrado = True
                            if not encontrado:
                                return False
                return True
            except IndexError:
                return False
        elif multiple:
            try:
                separacion = parte2.split(sep='|')
                for k in separacion:
                    sinEspacios = k.strip()
                    parte2 = sinEspacios.split(sep=' ')
                    for _ in parte2:
                        if _ != "epsilon" and _ != "":
                            encontrado = False
                            if _[0].isupper():
                                if not NoTerminal.verificarNoTerminal(listaNoTerminales, _):
                                    encontrado = True
                                if not encontrado:
                                    return False
                            else:
                                if not Terminal.verificarTerminal(listaTerminales, _):
                                    encontrado = True
                                if not encontrado:
                                    return False
                return True
            except IndexError:
                return False
        else:
            return True

    @staticmethod
    def enlistarProduccion(gramatica, nuevaP):
        listaNoTerminales = list(gramatica.noTerminales)
        separacion = nuevaP.split(sep='>')
        parte1 = separacion[0].strip()
        parte2 = separacion[1].strip()
        multiple = False
        for i in parte2:
            if i == "|":
                multiple = True
        if not multiple:
            sinEspacios = parte2.strip()
            parte2 = sinEspacios.split(sep=' ')
            parte2Completo = []
            for _ in parte2:
                parte2Completo.append(_)

            for noterminal in listaNoTerminales:
                if noterminal.nombre == parte1:
                    pNew = Produccion(noterminal.nombre, parte2Completo)
                    noterminal.producciones.append(pNew)
                    break
            return listaNoTerminales
        else:  # SI MULTIPLE ES IGUAL A TRUE
            separacion = parte2.split(sep='|')
            for k in separacion:
                sinEspacios = k.strip()
                parte2 = sinEspacios.split(sep=' ')
                parte2Completo = []
                for _ in parte2:
                    parte2Completo.append(_)
                for i in listaNoTerminales:
                    noterminal = i
                    if noterminal.nombre == parte1:
                        pNew = Produccion(noterminal.nombre, parte2Completo)
                        noterminal.producciones.append(pNew)
                        break

            return listaNoTerminales

    @staticmethod
    def operarborrarProduccion(gramatica):
        listaNoTerminales = list(gramatica.noTerminales)

        borrarPro = input("\nIngrese la Produccion que desee borrar:")
        if Produccion.verificarProduccion(gramatica, borrarPro):
            if Produccion.datosValidos(gramatica, borrarPro) == True and Produccion.verificarExistenciaProduccion(
                    gramatica, borrarPro) == True:
                print("\n   Se elimino la Producción con Exito")
                listaNoTerminales = Produccion.borrarProduccion(gramatica, borrarPro)
                return listaNoTerminales
            else:
                os.system("cls")
                print("\n     Error al Ingresar Producción Vuelva a intentarlo")
                return listaNoTerminales
        else:
            os.system("cls")
            print("\n     Error al Ingresar Producción Vuelva a intentarlo")
            return listaNoTerminales

    @staticmethod
    def borrarProduccion(gramatica, borrarPro):
        listaNoTerminales = list(gramatica.noTerminales)
        separacion = borrarPro.split(sep='>')
        parte1 = separacion[0].strip()
        parte2 = separacion[1].strip()
        for i in listaNoTerminales:
            noTerminal = i
            if noTerminal.nombre == parte1:
                listaProducciones = list(noTerminal.producciones)
                sinEspacios = parte2.strip()
                parte2 = sinEspacios.split(sep=' ')
                for produccion in listaProducciones:
                    if len(parte2) == len(produccion.produccion):
                        contador = 0
                        verificar = False
                        for _ in parte2:
                            if produccion.produccion[contador] == _:
                                verificar = True
                            if not verificar:
                                break
                            contador = contador + 1

                        if verificar:
                            listaProducciones.remove(produccion)
                            break

                noTerminal.producciones = listaProducciones
                break
        return listaNoTerminales

    @staticmethod
    def verificarExistenciaProduccion(gramatica, borrarPro):
        listaNoTerminales = list(gramatica.noTerminales)
        separacion = borrarPro.split(sep='>')
        parte1 = separacion[0].strip()
        parte2 = separacion[1].strip()
        for i in listaNoTerminales:
            noTerminal = i
            if noTerminal.nombre == parte1:
                listaProducciones = list(noTerminal.producciones)
                sinEspacios = parte2.strip()
                parte2 = sinEspacios.split(sep=' ')
                for produccion in listaProducciones:
                    if len(parte2) == len(produccion.produccion):
                        contador = 0
                        verificar = False
                        for _ in parte2:
                            if produccion.produccion[contador] == _:
                                verificar = True
                            if not verificar:
                                break
                            contador = contador + 1

                        if verificar:
                            return True
                break
        return False
