import json
import re

def leer_archivo_json(nombre_archivo : str, clave : str):
    '''
    Lee un archivo .json y devuelve una lista con la informacion ordenada en diccionarios en donde cada diccionario es un elemento
    Recibe como parametros el nombre del archivo a leer y la clave del diccionario que va a leer
    Retorna la lista con la informacion ordenada en diccionarios en donde cada diccionario es un elemento
    '''
    lista = []
    
    with open(nombre_archivo, "r") as archivo:
        
        dict  = json.load(archivo)
        lista = dict[clave]
    
    return lista


def guardar_archivo_csv(nombre_archivo : str, lista : list):
    '''
    Crea o sobreescribe un archivo .csv y guarda los nombres de una lista de diccionarios en el
    Recibe el nombre del archivo que va a crear y guardar, y la lista de diccionarios
    Retorna True en caso de haber podido crear el archivo correctamente o False en caso contrario
    '''
    try:
        with open(nombre_archivo, "w", encoding= "utf-8") as archivo:
            for elemento in lista:
                
                if elemento == lista[-1]:
                    texto_linea = "{0}".format(elemento["nombre"])
                    archivo.write(texto_linea)
                else:
                    texto_linea = "{0},".format(elemento["nombre"])
                    archivo.write(texto_linea)
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


def imprimir_menu_principal ():
    '''
    Imprime el menu principal
    No recibe nada
    No retorna nada
    '''
    print("---Menu de opciones---")
    print("1.Listar superheroes")
    print("2.Ordenar y listar superheroes por altura")
    print("3.Ordenar y listar superheroes por fuerza ")
    print("4.Lista de superheroes que sean mayores o menores del promedio de la clave elegida ")
    print("5.Listar superheroes segun su inteligencia ")
    print("6.Generar CSV con los heroes de las listas generadas en puntos 1 a 4 ")
    print("0. SALIR")
    
    
def parcial():
    
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    
    
    while True:
        
        imprimir_menu_principal()
        
        
        opcion = int(input("Ingrese una opcion: "))
        
        match opcion:
            
            case 1:
                flag1 = True
                pass
            case 2:
                flag2 = True
                pass
            case 3:
                flag3 = True
                pass
            case 4:
                flag4 = True
                pass
            case 5:
                    
                    print("---Submenu---")
                    print("---¿Que archivo desea guardar?---")
                    print("1.Lista de juegos cuyo genero no contenga la palabra 'pelea'")
                    print("2.Lista de juego segun la decada elegida")
                    print("3.Lista de juegos ordenados por emperesa")
                    print("4.Lista de juegos de cada modo ")
                    print("0. SALIR")
                    opcion = int(input("Ingrese una opcion valida: "))
                    while opcion not in [0,1,2,3,4]:
                        
                        opcion = int(input("Ingrese una opcion valida: "))
                        
                    match opcion:
                        case 1:
                                if flag1:
                                    pass
                                    #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_no_pelea.csv", lista1)
                                else:
                                    print("Primero debe generar la lista a guardar")
                        case 2:
                                if flag2:
                                    pass
                                    #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_decada_{}.csv".format(decada), lista2)
                                else:
                                    
                                    print("Primero debe generar la lista a guardar")
                        case 3:
                                if flag3:
                                    pass
                                    #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_ordenados_empresa_{}.csv".format(asc_desc), lista3)
                                else:
                                    print("Primero debe generar la lista a guardar")
                        case 4:
                                if flag4:
                                    pass
                                    #guardar_archivo_csv("C:/Users/Agustín/Dropbox/Mi PC (DESKTOP-DSJDI9V)/Desktop/Ejercicios Progra1/Modelo examen 1/juegos_modo_multijugador_cooperativo.csv", lista4)
                                else:
                                    print("Primero debe generar la lista a guardar")
                        case 0:
                                continue
                        case _:
                                pass
                
            case 0:
                break
            case _:
                pass
        
        input("\nPulse enter para continuar\n")
        
        
parcial()