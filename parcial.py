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
def leer_archivo_json(nombre_archivo : str, clave : str) -> list:
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


def guardar_archivo_csv_estadisticas(nombre_archivo : str, jugador : dict) -> bool:
    '''
    Crea o sobreescribe un archivo .csv y guarda los nombres de una lista de diccionarios en el
    Recibe el nombre del archivo que va a crear y guardar, y la lista de diccionarios
    Retorna True en caso de haber podido crear el archivo correctamente o False en caso contrario
    '''
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
                
                
            for estadistica in jugador["estadisticas"]:         
                archivo.write("{0},".format(estadistica))
                
            archivo.write("\n")  

            for estadistica in jugador["estadisticas"]: 
                
                    archivo.write("{0},".format(jugador["estadisticas"][estadistica]))
        return True
    
    
    except Exception as e:
        print("Error al crear el archivo {}".format(nombre_archivo))
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


def quick_sort_estadistica_key(lista : list, key : str , asc_desc : str):
    '''
    Ordena la lista de diccionarios segun la clave de estadisticas que recibe y el criterio ascendente o descendente
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
            if elemento["estadisticas"][key] > pivot["estadisticas"][key] and (asc_desc == "asc" or asc_desc == "mayor") \
                or elemento["estadisticas"][key] < pivot["estadisticas"][key] and (asc_desc == "desc" or asc_desc == "menor") :
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento) 
                
    
    
    lista_izquierda = quick_sort_estadistica_key(lista_izquierda,key,asc_desc)
    lista_izquierda.append(pivot)
    lista_derecha = quick_sort_estadistica_key(lista_derecha,key,asc_desc)          
    lista_izquierda.extend(lista_derecha)
    
    
    return lista_izquierda


def validar_numero_rango(valor : str, valor_minimo : float, valor_maximo : float) -> bool:
    
    '''
    Valida que una cadena de texto ingresada por el usuario sea un numero y se encuentre dentro de un rango especifico
    Recibe la cadena de texto del usuario, el valor minimo valido y el valor maximo valido (incluidos ambos)
    Retorna True en caso de que la cadena sea un numero dentro del rango valido o false en caso contrario
    '''
    
    if  re.match(r'(\d+(\.\d*)?|\.\d+)$', valor):
        

        numero = float(valor)
    else:
        return False
    
    if numero >= valor_minimo and numero <= valor_maximo:
        return True
    else:
        return False

def validar_numero_menu(opcion : str) -> bool:
    '''
    Valida que el usuario ingrese una opcion valida del menu
    Recibe la cadena de texto que representa la opcion elegida
    Retorna True en caso de que la opcion sea valida o False en caso contrario
    '''
    patron = r"^(0|[1-9]|1[0-9]|20|21|23)$"
    if re.match(patron, opcion):
        return True
    else:
        return False
    
    
def mostrar_nombres_jugadores(lista_jugadores : list) -> bool:
    '''
    Muestra el nombre y posicion de cada uno de los jugadores de la lista de jugadores que forman parte de nuestro set de datos
    Recibe la lista de jugadores a mostrar
    Retorna True en caso de que la lista tenga informacion o falso en caso de que la lista este vacia
    '''
    if lista_jugadores != []:
        
        indice = 1
        for jugador in lista_jugadores:
            print("{0}.Nombre: {1} - Posicion: {2}".format(indice,jugador["nombre"], jugador["posicion"])) 
            indice +=1
        return True
    else:
        return False


def mostrar_estadisticas_un_jugador(lista_jugadores : list, indice_ingresado : int):
    '''
    Muestra las estadisticas de un jugador en especifico elegido mediante un indice
    Recibe la lista de jugadores y el indice ingresado por el usuario
    Retorna True en caso de que la lista no este vacia o false en caso contrario
    '''
    if lista_jugadores != []:
        
        for jugador in lista_jugadores:
            if jugador == lista_jugadores[indice_ingresado - 1]:
                print("\n\nEstadisticas de {0}".format(jugador["nombre"]))
                for clave, valor in jugador["estadisticas"].items():

                        print("{0}: {1}".format(formatear_estadistica(clave), valor))
                    

        return True
    
    else: 
        return False
    
    
def calcular_mostrar_promedio_puntos_por_partido_equipo(lista_jugadores : list):
    '''
    Calcula y muestra a todos los jugadores ordenados segun el promedio de puntos por partido de manera ascendente
    Recibe la lista de jugadores
    Retorna True en caso de que la lista no este vacia o false en caso contrario
    '''
    if lista_jugadores != []:
        lista_copia = lista_jugadores[:]
        
        for estadistica in lista_copia["estadisticas"]:
            if estadistica == "promedio_puntos_por_partido":
                quick_sort_key(lista_copia, estadistica, "asc")
            
        for jugador in lista_copia:
            print("Nombre : {0} - Promedio de puntos por partido: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))    
        
        return True
    else:
        return False
    
def miembro_salon_fama(lista_jugadores : list, jugador: dict) -> bool:
    '''
    Determina y muestra si un jugador es "Miembro del Salon de la Fama del Baloncesto"
    Recibe la lista de jugadores y un diccionario que representa el jugador a evaluar
    Retorna True en caso de que el jugador sea miembro o false en caso contrario, o si la lista esta vacia
    '''
    if lista_jugadores != []:
        
            
                    if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                        print("{0} forma parte del salon de la fama".format(jugador["nombre"]))
                        return True
                    if "Miembro del Salon de la Fama del Baloncesto" not in jugador["logros"]:
                        print("{0} no forma parte del salon de la fama".format(jugador["nombre"]))
                        return False
                    
    else:
        return False


def calcular_mostrar_jugador_mas_estadistica(lista_jugadores : list, key : str) -> dict:
    '''
    Calcula y muestra el jugador con el valor numerico mas alto en una estadistica especifica
    Recibe la lista de jugadores y la clave de la estadistica a evaluar
    Retorna el jugador con la estadistica mas alta o False en caso de que la lista este vacia
    '''
    if lista_jugadores != []:
        
        lista_copia = lista_jugadores[:]
        jugador_mas_key = lista_jugadores[0]
        
        for jugador in lista_copia:
            if jugador_mas_key["estadisticas"][key] < jugador["estadisticas"][key]:
                jugador_mas_key = jugador
                
                
        print("El jugador con mas {0} es {1} con {2} {3}".format(formatear_estadistica(key).lower(),jugador_mas_key["nombre"], jugador_mas_key["estadisticas"][key], formatear_estadistica(key).lower()))
        return jugador_mas_key
                
    else:
        return False
    


def calcular_mostrar_jugador_mas_logros(lista_jugadores : list) -> dict:
    '''
    Calcula y muestra al jugador que posee mas logros, teniendo en cuenta los logros unicos y los acumulables
    Recibe la lisat de jugadores
    Retorna al jugador con mas logros o False en caso de que la lista este vacia 
    '''
    
    if lista_jugadores != []:
        logros_jugadores = []
        lista_copia = lista_jugadores[:]
        acumulador_logros = 0
        
        for jugador in lista_copia:
            for logro in jugador["logros"]:
                if re.search(r"[0-9]{4}", logro): 
                    acumulador_logros += len(re.findall(r"[0-9]{4}", logro)) 
                elif "Miembro" in logro:
                    acumulador_logros += 1
                
                 
                if re.match(r"[0-9]{1,3}", logro): 
                    acumulador_logros += int(re.findall(r"[0-9]{1,3}", logro)[0]) 
                
            
            
            logros_jugadores.append(acumulador_logros)
            

            acumulador_logros = 0
        
        
        for indice in range(len(logros_jugadores)):
            if indice == 0 or float(logros_jugadores[maximo_indice]) < float(logros_jugadores[indice]):
                maximo_indice = indice
                numero_maximo = logros_jugadores[maximo_indice]
        

        indice_jugador_mas_logros = logros_jugadores.index(numero_maximo) 
        jugador_mas_logros = lista_jugadores[indice_jugador_mas_logros]
        print("El jugador con mas logros es {0} con {1} logros".format(jugador_mas_logros["nombre"], numero_maximo))
        return jugador_mas_logros
        
        
    else:
        return False
    

def jugadores_mas_key_usuario(lista_jugadores : list, valor : float, key : str):
    '''
    Calcula y muestra aquellos jugadores que en una estadistica especifica tenga un valor mayor que el ingresado por el usuario
    Recibe la lista de jugadores, el valor ingresado por el usuario y la clave de la estadistica a evaluar
    Retorna True en caso de que la lista no este vacia o False en caso contrario
    '''
    if lista_jugadores != []:

        lista_copia = lista_jugadores[:]
        estadistica = formatear_estadistica(key)
        print("Los jugadores con una mayor cantidad de {0} a {1}:".format(estadistica.lower(), valor))
        for jugador in lista_copia:
            if valor <= jugador["estadisticas"][key]:
                if key == "porcentaje_tiros_de_campo":
                    print("{0} - {1} {2} - Posicion: {3}" .format(jugador["nombre"], estadistica, jugador["estadisticas"][key], jugador["posicion"]))
                else:
                    print("{0} - {1} {2}".format(jugador["nombre"], estadistica, jugador["estadisticas"][key]))
        return True
    else:
        return False


def calcular_mostrar_jugador_mas_temporadas_jugadas(lista_jugadores : list) -> dict:
    '''
    Calcula y muestra al jugador que tiene mas temporadas jugadas de la lista de jugadores
    Recibe la lista de jugadores
    Retorna al jugador con mas temporadas jugadas o False en caso de que la lista este vacia 
    '''

    if lista_jugadores != []:

        lista_copia = lista_jugadores[:]
        jugador_mas_temporadas = lista_copia[0]
        for jugador in lista_copia:
            if jugador["estadisticas"]["temporadas"] > jugador_mas_temporadas["estadisticas"]["temporadas"]:
                jugador_mas_temporadas = jugador

        print("{0} es el jugador con mas temporadas jugadas, con un total de {1} temporadas".format(jugador["nombre"], jugador["estadisticas"]["temporadas"]))
        return jugador_mas_temporadas
    else: 
        return False
    

def calcular_mostrar_promedio_puntos_por_partido_equipo_sin_menor(lista_jugadores : list):
    '''
    Calcula y muestra el promedio de puntos por partido de todo el equipo junto sin contar al jugador con menor valor
    Recbie la lista de jugadores
    Retorna el promedio obtenido o False en caso de que la lista este vacia
    '''
    
    
    if lista_jugadores != []:
        lista_copia = lista_jugadores[:]
        jugador_menos_puntos = lista_copia[0]

        suma = 0

        for jugador in lista_copia:
            if jugador["estadisticas"]["promedio_puntos_por_partido"] < jugador_menos_puntos["estadisticas"]["promedio_puntos_por_partido"]:
                jugador_menos_puntos = jugador

        for jugador in lista_copia:
            if jugador == jugador_menos_puntos:
                continue
            suma += jugador["estadisticas"]["promedio_puntos_por_partido"]

        promedio = (suma / (len(lista_copia)-1))
        promedio = round(promedio, 2)
        print("El promedio de puntos por partido sin el que menos puntos hizo es de {0} puntos".format(promedio))

        return promedio

                
    else:
        return False
    

def mostrar_logros_un_jugador(lista_jugadores : list, jugador : dict) -> bool:
    
    '''
    Muestra los logros de un jugador en especifico
    Recibe la lista de jugadores y un diccionario que representa al jugador
    Retorna True en caso de que la lista no este vacia o False en caso contrario
    '''
    
    if lista_jugadores != []:
        
        print("Logros de {0}:".format(jugador["nombre"]))
        for logro in jugador["logros"]:
            print("-",logro)
       
        return True
    else:
        return False
    
def validar_nombre(lista_jugadores : list, nombre_ingresado : str) -> list:
    '''
    Valida que un nombre ingresado por el usuario coincida en al menos 4 caracteres seguidos con uno perteneciente a un jugador y agrega a una lista aquellos que lo hagan
    Recibe la lista de jugadores y una cadena de texto del nombre ingresado por el usuario 
    Retorna la lista con aquellos nombres que coincidan al menos 4 caracteres seguidos o False en caso de que la lista este vacia
    '''
    
    if lista_jugadores != []:
        lista_copia = lista_jugadores[:]
        lista_resultado = []
        for jugador in lista_copia:
            nombre_completo = jugador["nombre"].lower()
            if re.search(r"(?i){0:4}".format(re.escape(nombre_ingresado).lower()), nombre_completo):
                lista_resultado.append(jugador)
            
        if lista_resultado == []:
            print("No se encontro ninguna coincidencia")
                
        return lista_resultado
        
    else:
        return False
    
    
    
def formatear_estadistica(estadistica : str) -> str:
    '''
    Formatea las estadisticas, quitandoles el guión bajo y poniendo en mayuscula la primer letra
    Recibe la cadena de texto de la estadistica a formatear
    Retorna la cadena ya formateada
    '''
    estadistica = estadistica.replace("_", " ").capitalize()


    return estadistica


def calcular_max_estadistica_key(lista_jugadores : list, key : str) -> float:
    '''
    Calcula el valor maximo de una estadistica en especifico
    Recibe la lista de jugadores y la clave de la estadistica a evaluar 
    Retorna un numero flotante que representa el valor maximo encontrado de esa estadistica
    '''
    if lista_jugadores != []:
        
        maximo = lista_jugadores[0]["estadisticas"][key]
        for jugador in lista_jugadores:
            if jugador["estadisticas"][key] > maximo:
                maximo = jugador["estadisticas"][key] 
                
        return float(maximo)       
        
    else: 
        return False
    

def calcular_mostrar__guardar_ranking_jugadores(lista_jugadores : list):
    '''
    Calcula, muestra y guarda en un archivo.csv el ranking de cada jugador en los criterios puntos, rebotes, asistencias y robos
    Recibe la lista de jugadores 
    No retorna nada
    '''
    posicion_puntos = ranking_jugadores(quick_sort_estadistica_key(lista_jugadores, "puntos_totales", "desc"))
    posicion_rebotes = ranking_jugadores(quick_sort_estadistica_key(lista_jugadores, "rebotes_totales", "desc"))
    posicion_asistencias = ranking_jugadores(quick_sort_estadistica_key(lista_jugadores, "asistencias_totales", "desc"))
    posicion_robos = ranking_jugadores(quick_sort_estadistica_key(lista_jugadores, "robos_totales", "desc"))
    lista_diccionarios = []
    encabezado = imprimir_encabezado_23()
    guardar_archivo_csv_rankings_encabezado(r"C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/parcial_1/pp_lab1_sande_agustin/archivos_csv/rankings.csv", encabezado)
    for jugador in lista_jugadores:
        dict = {}
        dict["nombre"] = jugador["nombre"]
        dict["ranking"] = posicion_puntos[jugador["nombre"]] + posicion_rebotes[jugador["nombre"]] + posicion_asistencias[jugador["nombre"]] + posicion_robos[jugador["nombre"]]
        print("{0:18} {1:10} {2:10} {3:10} {4:10}".format(jugador["nombre"], posicion_puntos[jugador["nombre"]], posicion_rebotes[jugador["nombre"]], posicion_asistencias[jugador["nombre"]], posicion_robos[jugador["nombre"]]))
        guardar_archivo_csv_rankings(r"C:\Users\Agustín\Dropbox\Mi PC (DESKTOP-DSJDI9V)\Desktop\Ejercicios Progra1\parcial_1\pp_lab1_sande_agustin\archivos_csv\rankings.csv", "{0:18} {1:10} {2:10} {3:10} {4:10}".format(jugador["nombre"], posicion_puntos[jugador["nombre"]], posicion_rebotes[jugador["nombre"]], posicion_asistencias[jugador["nombre"]], posicion_robos[jugador["nombre"]]))
        lista_diccionarios.append(dict)
    
    return lista_diccionarios
        
        
        
def guardar_archivo_csv_rankings_encabezado(nombre_archivo : str, contenido : str):
    '''
    Crea o sobreescribe en el archivo .csv el encabezado de los criterios que va a guardar los rankings
    Recibe el nombre del archivo que va a crear o sobreescribir y el contenido que va a escribir
    Retorna True en caso de haber podido crear el archivo o False en caso contrario 
    '''
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
            archivo.write(contenido)        
            archivo.write("\n")   
        return True
    
    
    except Exception as e:
        print("Error al crear el archivo {}".format(nombre_archivo))
        return False


def guardar_archivo_csv_rankings(nombre_archivo : str, contenido : str):
    '''
    Anexa en el archivo .csv los rankings de cada jugador junto con su nombre
    Recibe el nombre del archivo al que va a anexar informacion y el contenido que va a escribir
    Retorna True en caso de haber podido anexar la informacion o False en caso contrario 
    '''
    try:
        with open(nombre_archivo, "a", encoding= "utf-8") as archivo:
            archivo.write(contenido)        
            archivo.write("\n")   
        return True
    
    
    except Exception as e:
        print("Error al crear el archivo {}".format(nombre_archivo))
        return False        

def imprimir_encabezado_23() -> str:
    '''
    Imprime el encabezado de los criterios del punto 23
    No recibe nada 
    Retorna la cadena de texto del encabezado
    '''
    encabezado = "Jugador          -        Puntos - Rebotes - Asistencias - Robos "
    print(encabezado)
    return encabezado
    
    
def ranking_jugadores(lista_ordenada):
    '''
    Crea un diccionario en donde guarda el nombre y la posicion en el ranking de cierto jugador de una lista ya ordenada previamente
    Recibe la lista ya ordenada
    Retorna el diccionario con el nombre de cada jugador como clave y la posicion en el ranking como valor
    '''
    posicion_ranking = {}
    
    for i, jugador in enumerate(lista_ordenada):
            nombre = jugador["nombre"]
            posicion_ranking[nombre] = i + 1    
    
    return posicion_ranking


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
    print("21. Submenu Ejercicio extra")
    print("23. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: Puntos - Rebotes - Asistencias - Robos. Y exportar a CSV")
    
    print("0. SALIR")
    
def imprimir_submenu_extra():
    
    print("1.Determinar la cantidad de jugadores que hay por cada posición.")
    print("2.Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente")
    print("3.Determinar qué jugador tiene las mejores estadísticas en cada valor.")
    print("4.Determinar qué jugador tiene las mejores estadísticas de todos.")


def cantidad_jugadores_posicion(lista_jugadores : list):
    
    if lista_jugadores != []:
        
        posiciones = {}
        
        for jugador in lista_jugadores:
            if jugador["posicion"] not in posiciones:
                
                posiciones[jugador["posicion"]] = 1 
            else:
                posiciones[jugador["posicion"]] += 1
        
        return posiciones
    else:
        return False

def imprimir_cantidad_jugadores_posicion(posiciones : dict) :
    
    for posicion in posiciones:
        print("{0}:{1}".format(posicion, posiciones[posicion]))
        


def cantidad_all_star(lista_jugadores : list):
    
    if lista_jugadores != []:
        lista_copia = lista_jugadores[:]
        
        lista = []
        for jugador in lista_copia:
            dict = {}
            cantidad_allstar = 0
            for logro in jugador["logros"]:
                tiene_allstar = re.findall(r"([0-9]|1[0-9]) veces All-Star", logro)
                if tiene_allstar:
                    cantidad_allstar = int(tiene_allstar[0])

            dict["nombre"] = jugador["nombre"]
            dict["cantidad_all_star"] = int(cantidad_allstar)
            lista.append(dict)
            
        
        lista = quick_sort_key(lista, "cantidad_all_star", "desc")
        for jugador in lista:
            print("{0} ({1} veces All-Star)".format(jugador["nombre"], jugador["cantidad_all_star"]))
        
    else:
        return False
    
    
    
    
      
      
def calcular_jugador_max_estadistica_key(lista_jugadores : list, key : str) -> float:
    '''
    Calcula el jugador con el valor maximo de una estadistica en especifico
    Recibe la lista de jugadores y la clave de la estadistica a evaluar 
    Retorna un numero flotante que representa el valor maximo encontrado de esa estadistica
    '''
    if lista_jugadores != []:
        
        jugador_maximo = lista_jugadores[0]
        for jugador in lista_jugadores:
            if jugador["estadisticas"][key] > jugador_maximo["estadisticas"][key]:
                jugador_maximo = jugador 
                
        return jugador_maximo      
        
    else: 
        return False
    
    
def mostrar_jugador_max_estadistica_key(lista_jugadores : list):
    for estadistica in lista_jugadores[0]["estadisticas"].keys():
                            
        jugador_max = calcular_jugador_max_estadistica_key(lista_jugadores, estadistica)
                            
        print("Mayor cantidad de {0} : {1} ({2})".format(estadistica.replace("_", " ").lower(), jugador_max["nombre"], jugador_max["estadisticas"][estadistica] ))

        
        
    
def parcial():
    
    lista_jugadores = leer_archivo_json(r"C:\Users\Agustín\Dropbox\Mi PC (DESKTOP-DSJDI9V)\Desktop\Ejercicios Progra1\parcial_1\pp_lab1_sande_agustin\data_parcial.json", "jugadores")
     
    flag2 = False
    
    
    while True:
        
        imprimir_menu_principal()
        
        opcion = input("Ingrese una opcion: ")
        while not validar_numero_menu(opcion):
            opcion = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-21 o 23): ")

        match opcion:
            
            case "1":
                mostrar_nombres_jugadores(lista_jugadores)
                
                
            case "2":
                mostrar_nombres_jugadores(lista_jugadores)
                indice_ingresado = 0
                indice_ingresado = input("Ingrese por favor el indice del jugador del que desea ver sus estadisticas: ")
                while not (validar_numero_rango(indice_ingresado, 1,12)):
                    indice_ingresado = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-12): ")
                if mostrar_estadisticas_un_jugador(lista_jugadores, int(indice_ingresado)):
                    flag2 = True
                    
                
            case "3":
                if flag2: 
                    nombre_archivo = "C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/parcial_1/pp_lab1_sande_agustin/archivos_csv/estadisticas_{0}.csv".format(lista_jugadores[int(indice_ingresado) - 1]["nombre"])
                    if guardar_archivo_csv_estadisticas(nombre_archivo , lista_jugadores[int(indice_ingresado) - 1]):
                        
                        print("El archivo se guardo correctamente en {0}".format(nombre_archivo))
                else:   
                        print("Error al generar el archivo.")
                        print("Pruebe primero a generar la lista que desea guardar en el punto 2.")
                        
                
            case "4":
                
                mostrar_nombres_jugadores(lista_jugadores)
                
                nombre_jugador = input("\n-Ingrese el nombre del jugador que desea ver sus logros: ")
                while(len(nombre_jugador ) <4):
                    nombre_jugador = input("El nombre ingresado es demasiado corto, por favor ingrese al menos 4 caracteres: ")
                jugadores = validar_nombre(lista_jugadores, nombre_jugador)
                for jugador in jugadores:
                    mostrar_logros_un_jugador(lista_jugadores, jugador)

            case "5": 
                lista_ordenada_nombre_asc = quick_sort_key(lista_jugadores, "nombre", "asc")
                calcular_mostrar_promedio_puntos_por_partido_equipo(lista_ordenada_nombre_asc)
            case "6":
                mostrar_nombres_jugadores(lista_jugadores)
                
                nombre_jugador = input("\n-Ingrese el nombre del jugador que desea ver si forma parte del salon de la fama: ")
                while(len(nombre_jugador ) <4):
                    nombre_jugador = input("El nombre ingresado es demasiado corto, por favor ingrese al menos 4 caracteres: ")
                jugadores = validar_nombre(lista_jugadores, nombre_jugador)
                for jugador in jugadores:
                    
                    miembro_salon_fama(lista_jugadores, jugador)
            case "7":
                
                calcular_mostrar_jugador_mas_estadistica(lista_jugadores, "rebotes_totales")
            case "8":
                
                calcular_mostrar_jugador_mas_estadistica(lista_jugadores, "porcentaje_tiros_de_campo")
            case "9":
                
                calcular_mostrar_jugador_mas_estadistica(lista_jugadores, "asistencias_totales")
            case "10":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "promedio_puntos_por_partido")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo))
                
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                
                lista_ordenada_key = quick_sort_estadistica_key(lista_jugadores, "promedio_puntos_por_partido", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "promedio_puntos_por_partido")
            case "11":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "promedio_rebotes_por_partido")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo))
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                lista_ordenada_key = quick_sort_estadistica_key(lista_jugadores, "promedio_rebotes_por_partido", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "promedio_rebotes_por_partido")
            case "12":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "promedio_asistencias_por_partido")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo))
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                lista_ordenada_key = quick_sort_estadistica_key(lista_jugadores, "promedio_asistencias_por_partido", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "promedio_asistencias_por_partido")
            case "13":
                
                calcular_mostrar_jugador_mas_estadistica(lista_jugadores, "robos_totales")
            case "14":
                
                calcular_mostrar_jugador_mas_estadistica(lista_jugadores, "bloqueos_totales")
            case "15":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "porcentaje_tiros_libres")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo))
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                lista_ordenada_key = quick_sort_estadistica_key(lista_jugadores, "porcentaje_tiros_libres", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "porcentaje_tiros_libres")
            case "16":
                
                calcular_mostrar_promedio_puntos_por_partido_equipo_sin_menor(lista_jugadores)
            case "17":
                
                calcular_mostrar_jugador_mas_logros(lista_jugadores)
                
            case "18":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "porcentaje_tiros_triples")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo))
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                lista_ordenada_key = quick_sort_estadistica_key(lista_jugadores, "porcentaje_tiros_triples", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "porcentaje_tiros_triples")
            case "19":
                
                calcular_mostrar_jugador_mas_temporadas_jugadas(lista_jugadores)
            case "20":
                
                maximo = calcular_max_estadistica_key(lista_jugadores, "porcentaje_tiros_de_campo")
                valor = input("Ingrese un numero entre 0 y {0} por favor: ".format(maximo)) 
                while not (validar_numero_rango(valor, 1, maximo)):
                    valor = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (0-{0}): ".format(maximo))
                lista_ordenada_key = quick_sort_key(lista_jugadores, "posicion", "desc")
                jugadores_mas_key_usuario(lista_ordenada_key, float(valor), "porcentaje_tiros_de_campo")
            case "21":
                imprimir_submenu_extra()
                
                opcionSubmenu = input("Ingrese una opcion: ")
                while not validar_numero_menu(opcion):
                    opcionSubmenu = input("Numero ingresado no valido!\nIngrese una opcion valida por favor (1-4): ")
                    
                match opcionSubmenu:
                    case "1":
                        
                        imprimir_cantidad_jugadores_posicion(cantidad_jugadores_posicion(lista_jugadores))
                    case "2":
                        cantidad_all_star(lista_jugadores)
                    case "3":
                        mostrar_jugador_max_estadistica_key(lista_jugadores)
                    case "4":
                        a = calcular_mostrar__guardar_ranking_jugadores(lista_jugadores)
                        lista = quick_sort_key(a, "ranking", "asc")
                        print("El jugador con el mejor ranking en conjunto es {0}".format(lista[0]["nombre"]))
            case "23":
                
                calcular_mostrar__guardar_ranking_jugadores(lista_jugadores)
                
            case "0":
                break
            case _:
                pass
        
        input("\nPulse enter para continuar\n")



parcial()