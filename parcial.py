import json
import re

'''
FORMA DEL DATASET
"jugadores": [
    {
      "nombre": "Michael Jordan",
      "posicion": "Escolta",
      "estadisticas": {
        "temporadas": 15,
        "puntos_totales": 32292,
        "promedio_puntos_por_partido": 30.1,
        "rebotes_totales": 6672,
        "promedio_rebotes_por_partido": 6.2,
        "asistencias_totales": 5633,
        "promedio_asistencias_por_partido": 5.3,
        "robos_totales": 2514,
        "bloqueos_totales": 893,
        "porcentaje_tiros_de_campo": 49.7,
        "porcentaje_tiros_libres": 83.5,
        "porcentaje_tiros_triples": 32.7
      },
      "logros": [
        "6 veces campeón de la NBA",
        "6 veces MVP de la NBA",
        "14 veces All-Star",
        "10 veces líder en anotaciones de la NBA",
        "5 veces MVP de las Finales de la NBA",
        "Defensor del Año en la NBA en 1988",
        "Miembro del Salon de la Fama del Baloncesto"
      ]
'''
def leer_archivo_json(nombre_archivo : str, clave : str):
    '''
    Lee un archivo .json y devuelve una lista con la informacion ordenada en diccionarios en donde cada diccionario es un elemento
    Recibe como parametros el nombre del archivo a leer y la clave del diccionario que va a leer
    Retorna la lista con la informacion ordenada en diccionarios en donde cada diccionario es un elemento
    '''
    lista = []
    
    with open(nombre_archivo, "r", encoding= "utf-8") as archivo:
        
        dict  = json.load(archivo)
        lista = dict[clave]
    
    return lista


def guardar_archivo_csv_estadisticas(nombre_archivo : str, jugador : dict):
    '''
    Crea o sobreescribe un archivo .csv y guarda los nombres de una lista de diccionarios en el
    Recibe el nombre del archivo que va a crear y guardar, y la lista de diccionarios
    Retorna True en caso de haber podido crear el archivo correctamente o False en caso contrario
    '''
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
                texto_linea = ""
                lista_valores = estadisticas_un_jugador(jugador)
                for valor in lista_valores:
                    
                        
                    texto_linea += "{0}\n".format(valor)
                    if valor == lista_valores[2]:
                        for estadisticas in lista_valores[2]:
                            texto_linea += "{0}\n".format(lista_valores[2][estadisticas])
                    if valor == lista_valores[3] :
                        for logros in lista_valores[3]:
                            texto_linea += "{0}\n".format(lista_valores[3][logros])
                archivo.write(texto_linea)
        return True
    
    
    except Exception as e:
        print("Error al crear el archivo {}".format(nombre_archivo))
        return False

def estadisticas_un_jugador(jugador : dict):
    
    if lista_jugadores != []:
        
        lista_resultado = []
        
        for valor in jugador.values():
            
            lista_resultado.append(valor)
        
        
        print(lista_resultado)
        return lista_resultado
        
        
        
    else:
        return False
def quick_sort_key(lista : list, key : str, asc_desc : str):
    '''
    Ordena una lista de diccionarios que recibe segun una clave y el criterio ascendente o descendente
    Recibe la lista de diccionarios a ordenar, la clave que va a utilizar para ordenar y el criterio asc o desc
    Retorna una lista ordenada con los criterios elegidos
    '''        
    lista_derecha = []
    lista_izquierda = []
    
    if (len(lista) <= 1):
        return lista
    else:
        pivot = lista[0]
        for elemento in lista[1:]:
            if elemento[key] > pivot[key] and (asc_desc == "asc" or asc_desc == "mayor") \
                or elemento[key] < pivot[key] and (asc_desc == "desc" or asc_desc == "menor") :
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento) 
                
    
    
    lista_izquierda = quick_sort_key(lista_izquierda,key,asc_desc)
    lista_izquierda.append(pivot)
    lista_derecha = quick_sort_key(lista_derecha,key,asc_desc)          
    lista_izquierda.extend(lista_derecha)
    
    
    return lista_izquierda

def validar_numero_rango(valor : str, valor_minimo : int, valor_maximo : int):
    # Validar si el valor ingresado es un número
    
    # if not re.match(r'^\d+$', valor):
    #     return False

    numero = int(valor)
    # Verificar si el número está dentro del rango permitido
    if numero >= valor_minimo and numero <= valor_maximo:
        return True
    else:
        return False
    
    
def mostrar_nombres_jugadores(lista_jugadores : list):
    
    if lista_jugadores != []:
        indice = 1
        for jugador in lista_jugadores:
            print("{0}.Nombre: {1} - Posicion: {2}".format(indice,jugador["nombre"], jugador["posicion"])) 
            indice +=1
        
    else:
        return False


def mostrar_estadisticas_un_jugador(lista_jugadores : list, indice_ingresado : int):
    if lista_jugadores != []:
        
        

        
        for jugador in lista_jugadores:
            if jugador == lista_jugadores[indice_ingresado - 1]:
                print("\n\nLogros de {0}".format(jugador["nombre"]))
                for logro in jugador["logros"]:
                    print("-",logro)
                    

        return True
    
    else: 
        return False
    
    
    

def imprimir_menu_principal ():
    '''
    Imprime el menu principal
    No recibe nada
    No retorna nada
    '''
    print("---Menu de opciones---")
    print("1.Mostrar la lista de todos los jugadores")
    print("2.Mostrar estadisticas de un jugador elegido por el usuario")
    print("3.Generar archivo CSV de jugador seleccionado en el punto 2 ")
    print("4.Mostrar logros de un jugador ")
    print("5.Mostrar lista de jugadores con promedio de puntos por partido ordenados ")
    print("6.Buscar si un jugador ingresado por el usuario forma parte del Salon de la Fama del Baloncesto")
    print("7.Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8.Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9.Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
    print("11. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
    print("12. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18. Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20. Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.")
    print("21. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: Puntos - Rebotes - Asistencias - Robos")
    print("0. SALIR")
    
lista_jugadores = leer_archivo_json(r"C:\Users\Agustín\Dropbox\Mi PC (DESKTOP-DSJDI9V)\Desktop\Ejercicios Progra1\parcial_1\pp_lab1_sande_agustin\data_parcial.json", "jugadores")    
def parcial():
    
    flag2 = False
    
    
    while True:
        
        imprimir_menu_principal()
        
        
        opcion = int(input("Ingrese una opcion: "))
        
        match opcion:
            
            case 1:
                mostrar_nombres_jugadores(lista_jugadores)
                
                
            case 2:
                mostrar_nombres_jugadores(lista_jugadores)
                indice_ingresado = 0
                indice_ingresado = int(input("Ingrese por favor el indice del jugador del que desea ver sus estadisticas: "))
                while not (validar_numero_rango(indice_ingresado, 1,12)):
                    indice_ingresado = int(input("Ingrese por favor el indice del jugador del que desea ver sus estadisticas: "))
                if mostrar_estadisticas_un_jugador(lista_jugadores, indice_ingresado):
                    flag2 = True
                    
                
            case 3:
                if flag2: guardar_archivo_csv_estadisticas("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/parcial_1/pp_lab1_sande_agustin/archivos_csv/estadisticas_{0}.csv".format(lista_jugadores[indice_ingresado - 1]["nombre"]), lista_jugadores[indice_ingresado - 1])
                
            case 4:
                
                pass
            # case 5:
                    
            #         print("---Submenu---")
            #         print("---¿Que archivo desea guardar?---")
            #         print("1.Lista de juegos cuyo genero no contenga la palabra 'pelea'")
            #         print("2.Lista de juego segun la decada elegida")
            #         print("3.Lista de juegos ordenados por emperesa")
            #         print("4.Lista de juegos de cada modo ")
            #         print("0. SALIR")
            #         opcion = int(input("Ingrese una opcion valida: "))
            #         while opcion not in [0,1,2,3,4]:
                        
            #             opcion = int(input("Ingrese una opcion valida: "))
                        
            #         match opcion:
            #             case 1:
            #                     if flag1:
            #                         pass
            #                         #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_no_pelea.csv", lista1)
            #                     else:
            #                         print("Primero debe generar la lista a guardar")
            #             case 2:
            #                     if flag2:
            #                         pass
            #                         #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_decada_{}.csv".format(decada), lista2)
            #                     else:
                                    
            #                         print("Primero debe generar la lista a guardar")
            #             case 3:
            #                     if flag3:
            #                         pass
            #                         #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_ordenados_empresa_{}.csv".format(asc_desc), lista3)
            #                     else:
            #                         print("Primero debe generar la lista a guardar")
            #             case 4:
            #                     if flag4:
            #                         pass
            #                         #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_modo_multijugador_cooperativo.csv", lista4)
            #                     else:
            #                         print("Primero debe generar la lista a guardar")
            #             case 0:
            #                     continue
            #             case _:
            #                     pass
                
            case 0:
                break
            case _:
                pass
        
        input("\nPulse enter para continuar\n")
        
        
parcial()