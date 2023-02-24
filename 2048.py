import random

def init_tablero(tam,obstaculos,numero_opc):#MÉTODO PPARA CREAR EL TABLERO,INSERTAR 2 NUMEROS Y OBSTACULOS
    tablero = []
    for i in range(tam):
        tablero.append([0] * tam)

    tablero = insert_num(tablero, 2)
    tablero = obs(tablero, obstaculos,numero_opc)
    return tablero


def preg_ins_num(): #MUESTRA EL TABLERO CON MOVIMIENTO REALIZADO SIN UN NUMERO BLOQUE
    tecla = None
    while tecla != '':
        tecla = str(input("Pulse [ENTER] para mostrar inserción del nuevo bloque"))


def insert_num(tablero, inserciones ): #EN FUNCION DEL MODO INSERTA NUMERO INICIAL
        num = [2, 2, 2, 4]  #PROBABILIDADES EN FUNCION DEL MODO
        cont = 0
        while cont != inserciones:
            x = random.randrange(len(tablero)) #ELIJE POSICION RANDOM
            y = random.randrange(len(tablero))
            if tablero[x][y] == 0:  #SI LA POSICION ES UN ESPACIO
                tablero[x][y] = num[random.randrange(4)] #ELIJE UNO DE LOS 4 NUMEROS ANTERIORES
                cont = cont + 1
        return tablero
def obs(tablero, obstaculos,numero_opc): #ESCRIBE OBSTACULOS EN EL TABLERO
        cont = 0
        while cont != obstaculos: #SI EL CONTADOR ES DISTINTO AL NUMERO INTRODUCIDO  EJECUTA EL BUCLE
            x = int(random.uniform(0, len(tablero))) #POSCION RANDOM
            y = int(random.uniform(0, len(tablero))) #POSCION RANDOM
            if tablero[x][y] == 0:
                if numero_opc == 4:
                    tablero[x][y] = '****' #**** SI ELMODO ES 2048
                if numero_opc == 3:
                    tablero[x][y] = '***' #**** SI ELMODO ES 1024
                if numero_opc == 2:
                    tablero[x][y] = '**' #**** SI ELMODO ES NIVELES
                if numero_opc == 1:
                    tablero[x][y] = '*' #**** SI ELMODO ES LETRAS
                cont = cont + 1 #SUMA 1 AL CONTADOR
        return tablero

def tab1(num): #MODIFICA EL PRINT YA QUE EL MODO ALFABETO FUNCIONA IGUAL QUE EL 2048
    if num == 2: #SUSTITUYE TODOS Y CADA UNO DE LOS VALORES POR SU LETRA CORRESPONDIENTE
        print('A', end='')
    if num == 4:
        print('B', end='')
    if num == 8:
        print('C', end='')
    if num== 16:
        print('D', end ='')
    if num == 32:
        print('E', end='')
    if num == 64:
        print('F', end='')
    if num == 128:
        print('G', end='')
    if num == 256:
        print('H', end ='')
    if num == 512:
        print('I', end='')
    if num == 1024:
        print('J', end='')
    if num == 2048:
        print('F', end='')
    if num == '*' or num == '****' or num == '**' or num == '***':
        print('*', end='')
    if num == 0:
        print(' ',end='')

def tab3(num): #MODIFICA EL PRINT YA QUE EL MODO 1024 FUNCIONA IGUAL QUE EL 2048
    if num == 2: #SUSTITUYE TODOS Y CADA UNO DE LOS VALORES POR SU LETRA CORRESPONDIENTE
        print('1', end='')
    if num == 4:
        print('2', end='')
    if num == 8:
        print('4', end='')
    if num== 16:
        print(' 8', end ='')
    if num == 32:
        print('16', end='')
    if num == 64:
        print('32', end='')
    if num == 128:
        print('64', end='')
    if num == 256:
        print('128', end ='')
    if num == 512:
        print('256', end='')
    if num == 1024:
        print(' 512', end='')
    if num == 2048:
        print('1024', end='')
    if num == '*' or num == '****' or num == '**' or num == '***':
        print('***', end='')
    if num == 0:
        print(' ',end='')

def tab2(num): #MODIFICA EL PRINT YA QUE EL MODO NIIVELES FUNCIONA IGUAL QUE EL 2048
    if num == 2: #SUSTITUYE TODOS Y CADA UNO DE LOS VALORES POR SU VALOR CORRESPONDIENTE
        print('0', end='')
    if num == 4:
        print('1', end='')
    if num == 8:
        print('2', end='')
    if num == 16:
        print(' 3', end='')
    if num == 32:
        print(' 4', end='')
    if num == 64:
        print(' 5', end='')
    if num == 128:
        print(' 6', end='')
    if num == 256:
        print(' 7', end='')
    if num == 512:
        print(' 8', end='')
    if num == 1024:
        print(' 9', end='')
    if num == 1024:
        print(' 10', end='')
    if num == '*' or num == '****' or num == '**' or num == '***':
        print('**', end='')
    if num == 0:
        print(' ',end='')

def tab4(num): #MODIFICA EL PRINT YA QUE EL MODO NIIVELES FUNCIONA IGUAL QUE EL 2048
    if num == '*' or num == '****' or num == '**' or num == '***':
       num='****'
    return num

def tab(tablero,numero_opc): #CREA EL TABLERO EN FUNCION DEL MODO
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if numero_opc == 4: #MODO 2048
                print("+----", end='')
            if numero_opc == 3: #MODO 1024
                print("+---", end='')
            if numero_opc == 2: #MODO NIVELES
                print("+--", end='')
            if numero_opc == 1: #MODO ALFABETO
                print("+-", end='')
        print('+')
        for j in range(len(tablero)):
            print('|', end='') #IMPRIME LAS RAYAS QUE SEPARAN LAS CASILLAS
            for k in range(int(numero_opc) - len(str(tablero[i][j]))): #RESERVA EL ESPACIO EN LAS CASILLAS
                if tablero[i][j] != '*' and tablero[i][j] != '**' and tablero[i][j] != '***' and tablero[i][j] != '****':
                    print(' ', end='')
            if numero_opc == 1: #SI EL MODO ES EL ALFABETO MODIFICA EL PRINT Y LE DA INTERFAZ CON LETRAS
                tab1(tablero[i][j])
            if numero_opc == 2: #SI EL MODO ES EL NIVELES MODIFICA EL PRINT Y LE DA INTERFAZ CON NUMEROS DISTINTOS AL 2048
                tab2(tablero[i][j])
            if numero_opc == 3: #SI EL MODO ES EL 1024 MODIFICA EL PRINT Y LE DA INTERFAZ CON NUMEROS DISTINTOS AL 2048
                tab3(tablero[i][j])
            if numero_opc == 4: #SI ES EL 2048 NO MODIFICA LA INTERFAZ
                if tablero[i][j] == '*' or tablero[i][j] == '**' or tablero[i][j] == '***':
                    tablero[i][j] = '****'
                print(' ' if tablero[i][j] == 0 else tablero[i][j], end='')
        print('|')
    for i in range(len(tablero)):
        if numero_opc == 4: #MODO 2048
            print('+----', end='')
        if numero_opc == 3: #MODO 1024
            print('+---', end='')
        if numero_opc == 2: #MODO NIVELES
            print('+--', end='')
        if numero_opc == 1: #MODO ALFABETO
            print('+-', end='')
    print('+')

def trasponer(tablero): #DA LA VUELTA AL TABLERO
    tablero_aux = [] #CREA UNA LISTA VACIA
    for i in range(len(tablero[0])): #RECORRE LA FILA Y CAMBIA POR COLUMNAS
        tablero_aux.append([])
        for j in range(len(tablero)): #RECORRE LA COLUMNA Y LO CAMBIA POR FILAS
            tablero_aux[i].append(tablero[j][i])
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            tablero[i][j] = tablero_aux[i][j] #EL TABLERO TOMA EL VALOR DEL TABLERO TRASPUESTO
    return tablero

def juntarI(miFila): #ARRASTRA LOS VALORES
    filaJuntada = [] #CREA LISTA VACIA
    for i in range(len(miFila)): #RECORRE LA FILA
        if miFila[i] != 0: #SI ES DISTINTO DE UN ESPACIO
            filaJuntada.append(miFila[i]) #AÑADE EL VALOR A FILAJUNTADA
    while len(filaJuntada) != len(miFila): #SI LA LONGITUD ES DISTINTA A LA DE LA FILA
        filaJuntada.append(0) #AÑADE UN ESPACIO
    return filaJuntada

def fusionarI(miFila): #MEZCLA IZQ
    global puntuacion_final #PUNTUACION
    for i in range(len(miFila)):
        if len(miFila) > 1:
            if miFila[i - 1] == miFila[i]: #SI EL VALOR DE LA CASILLA ES EL MISMO
                miFila[i - 1] *= 2 #MULTIPLICA POR 2
                if miFila[i-1] == 4:
                    puntuacion_final += 2   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 8:
                    puntuacion_final += 3   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 16:
                    puntuacion_final += 4   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 32:
                    puntuacion_final += 5   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 64:
                    puntuacion_final += 6   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 128:
                    puntuacion_final += 7   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 256:
                    puntuacion_final += 8   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 512:
                    puntuacion_final += 9   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 1024:
                    puntuacion_final += 10   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                if miFila[i-1] == 2048:
                    puntuacion_final += 11   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
                miFila[i] = 0 #ALA CASILLA QUE SE FUSIONA LE DA VALOR ESPACIO
    return miFila

def juntarD(miFila): #MEZCLA DRCH
    filaJuntada = [] #LISTA VACIA
    for i in range(len(miFila) - 1, -1, -1):
        if miFila[i] != 0: #DISTINTO DE UN ESPACIO
            filaJuntada.insert(0, miFila[i]) #AÑADE EL VALOR A FILAJUNTADA
    while len(filaJuntada) != len(miFila): #SI LA LONGITUD ES DISTINTA
        filaJuntada.insert(0, 0) #AÑADE UN 0
    return filaJuntada

def fusionarD(miFila): #MEZCLA DRCH
    global puntuacion_final #PUNTUACION
    for i in range(len(miFila) - 1, 0, -1):
        if miFila[i] == miFila[i - 1]: #SI EL VALOR ES =
            miFila[i - 1] *= 2 #SUMA 1
            miFila[i] *= 2
            if miFila[i - 1] == 4:
                puntuacion_final += 2  # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 8:
                puntuacion_final += 3   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 16:
                puntuacion_final += 4   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 32:
                puntuacion_final += 5   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 64:
                puntuacion_final += 6   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 128:
                puntuacion_final += 7   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 256:
                puntuacion_final += 8   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 512:
                puntuacion_final += 9   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 1024:
                puntuacion_final += 10   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            if miFila[i - 1] == 2048:
                puntuacion_final += 11   # SUMA EL VALOR DEL NIVEL A LA PUNTUACION
            miFila[i - 1] = 0  #AL VALOR DE LA CASILLA LE PONEE 0
    return miFila

def mov_izq(tablero,numero_opc): #MOVIMIENTO IZQ
    for i in range(len(tablero)): # RECORRE EL TABLERO
        miFila = tablero[i] # FILA DEL TABLERO EN LA QUE ESTAS
        asterisco = len(miFila)# ESTABLECE EL TOPE AL FINAL
        fila_final = []*(len(miFila))# LISTA VACIA DE IGUAL LONGITUD QUE LA FILA
        for j in range(len(miFila)-1, -1, -1):  # RECORRE LA FILA POR EL FINAL
            if miFila[j] == '****' or miFila[j] == '***' or miFila[j] == '**' or miFila[j] == '*' or j == 0:# COMPRUEBA EL VALOR DE LA CASILLA SI ES IGUAL QUE ESO, VUELVE AL PRINCIP
                fila_parcial = juntarI(fusionarI(juntarI(miFila[j:asterisco]))) # DIVIDE LA FILA EN FUNCION D LOS * ENCONTRADOS Y FUSIONA LOS NUMEROS
                for k in range(len(fila_parcial)-1, -1, -1):
                    fila_final.insert(0,fila_parcial[k])#INSERTA AL FINAL DE FILA_FINAL, CADA UNA DE LAS FILAS PARCIALES
                asterisco = j#LO COLOCA A LA IZQ DEL OBSTACULO
        tablero[i] = fila_final #ES IGUAL A LA FILA
    return tablero

def mov_dcha(tablero,numero_opc):#INICIA EL MOVIMIENTO DERECHA
    for i in range(len(tablero)): #RECORRE TABLERO
        asterisco = 0
        miFila = tablero[i]# FILA DEL TABLERO EN LA QUE ESTAS
        fila_final = []# LISTA VACIA
        for j in range(len(miFila)):#RECORRE LA FILA
            if miFila[j] == '****' or miFila[j] == '***' or miFila[j] == '**' or miFila[j] == '*' or j == len(miFila) - 1:#COMPRUEBA EL VALOR DE LA CASILLA
                fila_parcial = juntarD(fusionarD(juntarD(miFila[asterisco:j + 1])))#DIVIDE LA FILA EN FUNCION D LOS * ENCONTRADOS Y FUSIONA LOS NUMEROS
                fila_final += fila_parcial #SUMA FILAS PARCIALES QUE A DIVIDIDO PARA HALLAR LA FINAL
                asterisco = j + 1
        tablero[i] = fila_final
    return tablero


def mov_abajo(tablero,numero_opc): #MOVIMIENTO ABAJO
    trasponer(tablero) #DA LA VUELTA AL TABLERO
    for i in range(len(tablero)):
        asterisco = 0
        miFila = tablero[i] # FILA DEL TABLERO EN LA QUE ESTAS
        fila_final = [] # LISTA VACIA
        for j in range(len(miFila)): #RECORRE LA FILA
            if miFila[j] == '****' or miFila[j] == '***' or miFila[j] == '**' or miFila[j] == '*' or j == len(miFila) - 1: #COMPRUEBA EL VALOR DE LA CASILLA
                fila_parcial = juntarD(fusionarD(juntarD(miFila[asterisco:j + 1]))) #DIVIDE LA FILA EN FUNCION D LOS * ENCONTRADOS Y FUSIONA LOS NUMEROS
                fila_final += fila_parcial #SUMA FILAS PARCIALES QUE A DIVIDIDO PARA HALLAR LA FINAL
                asterisco = j + 1
        tablero[i] = fila_final #TABLERO ES IGUAL A LA SUMA DE TODAS LAS FILAS
    return trasponer(tablero)


def mov_arriba(tablero,numero_opc): #MOVIMIENTO ARRIBA
    trasponer(tablero) #DA LA VUELTA AL TABLERO
    for i in range(len(tablero)):
        miFila = tablero[i] #FILA DEL TABLERO EN LA QUE ESTAS
        asterisco = len(miFila)  # ESTABLECE EL TOPE AL FINAL
        fila_final = [] * (len(miFila))  # LISTA VACIA DE IGUAL LONGITUD QUE LA FILA
        for j in range(len(miFila) - 1, -1, -1): # RECORRE LA FILA POR EL FINAL
            if miFila[j] == '****' or miFila[j] == '***' or miFila[j] == '**' or miFila[j] == '*' or j == 0:  # COMPRUEBA EL VALOR DE LA CASILLA SI ES IGUAL QUE ESO, VUELVE AL PRINCIP
                fila_parcial = juntarI(fusionarI(juntarI(miFila[j:asterisco]))) # DIVIDE LA FILA EN FUNCION D LOS * ENCONTRADOS Y FUSIONA LOS NUMEROS
                for k in range(len(fila_parcial) - 1, -1, -1):
                    fila_final.insert(0, fila_parcial[k]) #LO COLOCA A LA IZQ DEL OBSTACULO
                asterisco = j
        tablero[i] = fila_final #TABLERO ES IGUAL A LA SUMA DE TODAS LAS FILAS
    return trasponer(tablero)

def comprobacionVictoria(tablero,numero_opc): #COMPRUEBA SI HA GANADO
    for fila in tablero:
        for elemento in fila:
            if elemento == 2048:  #SI EN EL TABLERO, ESTA EN ALGUNA CASILLA EL VALOR 2048,J O 10,DEPENDIENDO DEL MODO,ENTONCES GANAS
                return True
    return False


def guardar(tam, cont_jugada, puntuacion_final,numero_opc):
    archivo = input("Nombre del archivo: ") #INSERTAR NOMBRE ARCHIVO
    a = open(archivo, "w")
    a.write(str(cont_jugada) + "\n" + str(puntuacion_final) + "\n" + str(numero_opc)) #ESCRIBE EL VALOR DE PUNTUACION Y MOVIMIENTOS

    for i in range(tam): #RECORRE EL TABLERO
        a.write("\n") #SALTO DE LINEA
        for j in range(tam): #REOCRRE COLUMNAS
            if tablero[i][j] == 0: #SI ES UN ESPACIO
                a.write(".") # ESCRIBE UN PUNTO
            else:
                a.write(str(tablero[i][j])) #ESCRIBE EL TABLERO
    a.close()

def leer():
    archivo = input("Nombre del archivo: ")
    a = open(archivo, "r")
    copia = a.read().splitlines()
    cont_jugada = int(copia[0])  #EN LAL INEA 0, LOS MOVIMIENTOS
    puntuacion_final = int(copia[1]) #EN LA LINEA 1, LA PUNTUCION
    numero_opc = int(copia[2]) #LINA 2 LA OPCION
    tam = int(len(copia[3])) #LINEA 3 EL TBLERO
    obs = 0
    tablero = [] #LISTA VACIA

    for i in copia[3:]: #EN LA LINEA 3 ENPIEZA A ESCRIBIR EL TABLERO
        fila = []
        for j in i:
            if j == '.': #SI HAY UN PUNTO
                fila.append(int(0)) #ESCRIBE UN ESPACIO
            else: #SI ES DISTINTO
                fila.append(j)  # AÑADE EL VALOR
                if j == '*': # Y SI ES DISTINTO DE ESPACIO, ES UN * ENTONCES PONE UN ESPACIO
                    obs += 1
        tablero.append(fila) #EL TABLERO ES LA SUMA DE LS FILAS
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] != 0 and tablero[i][j] != '*' and tablero[i][j] != '**' and tablero[i][j] != '***' and tablero[i][j] != '****':
                tablero[i][j] = int(tablero[i][j])
    return tablero, puntuacion_final, tam, cont_jugada, numero_opc, copia

def jugada(tablero,numero_opc):
    salida = 0
    jug = str(input(" ENTER para hacer un movimiento | [M]odo, [G]uardar, [F]in")) #IMPRIME EL MENU DE MOVIMIENTOS
    if jug == '': #SE ENCARGA DE ESCOGER AL AZAR UN MOVIMIENTO
        n_azar = random.randrange(4)
        if n_azar == 0: # SI LA JUGADA ES MOVER A LA IZQUIERDA
            tablero = mov_izq(tablero,numero_opc) # LLAMA AL MOVIMIMIENTO MOVER IZQUIERDA, Y ASI CON CADA JUGADA

        if n_azar == 1:
            tablero = mov_dcha(tablero,numero_opc)

        if n_azar == 2:
            tablero =mov_arriba(tablero,numero_opc)

        if n_azar == 3:
            tablero = mov_abajo(tablero,numero_opc)

    if jug == 'M':
        numero_opc = int(input('Indique opción: '))

    if jug == 'G':
        guardar(tam, cont_jugada, puntuacion_final, numero_opc)

    if jug == 'F':
        salida = 1
    return tablero, numero_opc,salida
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
while True:
    print(50 * '-')
    print('-Práctica de Paradigmas de Programación 2019-2020-')
    print(50 * '-')
    print()
    print('1. CREAR NUEVO TABLERO')
    print('2. LEER TABLERO DE FICHERO')
    print('3. SALIR')
    print()
    num = int(input('¿ 1 , 2 , 3 ? '))
    #PIDE LAS CONDICIONES DE IMPRESION DEL TABLERO
    if num == 1:
        numero_opc = int(input('Indique opción de juego, Letras(1),Niveles(2),1024(3) o 2048(4): '))

        tam = int(input('Tamaño del tablero: '))
        obstaculos = int(input('Obstaculos en el tablero: '))
        tablero = init_tablero(tam, obstaculos, numero_opc)
        cont_jugada = 0
        puntuacion_final = 0

        while True:
            tab(tablero, numero_opc)
            tablero, numero_opc,salida = jugada(tablero, numero_opc)
            if salida != 1:
                cont_jugada += 1
                print('MOVIMIENTOS: ', cont_jugada, 'PUNTUACION: ', puntuacion_final) #IMPRIME EL NÚMERO DE MOVIMIENTOS Y PUNTUCIÓN
                tab(tablero, numero_opc)#IMPRIME TABLERO
                preg_ins_num()
                insert_num(tablero, 1)
                if (comprobacionVictoria(tablero,numero_opc)):#COMPRUEBA SI VICTORIA
                    print("Has ganado!")
                    break
            else:
                print("------------------------------------Usted ha salido del juego-----------------------------------------")
                break

    if num == 2: #SI  ES UN 2 ABRE EEL MENU DE LEER UN ARCHIVO
        tablero, puntuacion_final, tam, cont_jugada, numero_opc, copia = leer()
        tab(tablero, numero_opc)

    if num == 3:#3 FINALIZA EL JUEGO
        print("------------------------------------Usted ha salido del juego-----------------------------------------")
        break