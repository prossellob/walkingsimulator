#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, os,time,sys


#Comprobar que el personaje no salga del mapa.
def comprobarlimites():
    global x,y
    if x > mapabase:
        print('Has llegado al limite del mapa.')
        x = mapabase
    if x < -mapabase:
        print('Has llegado al limite del mapa.')
        x = -mapabase
    if y > mapabase:
        print('Has llegado al limite del mapa.')
        y = mapabase
    if y < -mapabase:
        print('Has llegado al limite del mapa.')
        y = -mapabase
#Crea el mapa con las dimensiones que queramos.
def crearmapa(dimensionesmapa):
    coordx,coordy = -dimensionesmapa, -dimensionesmapa
    txt = open('mapa.txt','r+')
    txt.truncate()
    while coordy <= dimensionesmapa:
        while coordx <= dimensionesmapa:
            edif = random.randrange(102) #Probabilidad de cada edificio.
            if edif <= 21:
                edif = 1
            elif edif >= 22 and edif <= 39:
                edif = 2
            elif edif >= 40 and edif <= 52:
                edif = 3
            elif edif >= 53 and edif <= 65:
                edif = 4
            elif edif >= 66 and edif <= 78:
                edif = 5
            elif edif >= 79 and edif <= 101:
                edif = 6
            txt.write(str(coordx) + str(coordy) + '@' + str(edif)+ '\n')
            coordx += 1
        coordy += 1
        coordx = -dimensionesmapa
    txt.close()
#Conjunto de acciones que el personaje puede realizar.
def accion():
    global x,y,alpha,dinero,turnos
    while alpha < 1:
        print("Si no sabes como empezar escribe 'ayuda'. ")
        print('Pulsa enter para saltar los mensajes del juego, este también.')
        alpha += 1
    try:
         input()
    except SyntaxError:
         pass
    os.system('clear')
    print('Simulador v.1  Turnos:' + str(turnos) + '/24      Dinero: ' + str(dinero))
    acc = input('>')
    if acc == 'norte':
        y += 1
        turnos += 1
        posicion()
    elif acc == 'sur':
        y -= 1
        turnos += 1
        posicion()
    elif acc == 'oeste':
        turnos += 1
        x -= 1
        posicion()
    elif acc == 'este':
        turnos += 1
        x += 1
        posicion()
    elif acc == 'ayuda':
        turnos += 1
        ayuda()
    elif acc == 'lugar':
        turnos += 1
        posicion()
    elif acc == 'dinero':
        turnos += 1
        print('Tienes ' + str(dinero) + '$')
    elif acc == 'salir':
        sys.exit(0)
    elif acc == 'guardar':
        guardar()
    else:
        print("Parece que este comando no existe,escribe 'ayuda' para más información.")

#Posición en la que se encuentra el personaje.
def posicion():
    global edificio
    txt = open('mapa.txt','r')
    while True:
        a = txt.readline()
        a = str(a)
        if (str(x)+str(y)) in a:
            edificio = a[-2]
            break
    edificio = int(edificio)
    if edificio == 1:
        print('Encuentras una casa.')
    elif edificio == 2:
        print('Encuentras unos apartamentos.')
    elif edificio == 3:
        print('Encuentras una tienda de comida.')
    elif edificio == 4:
        print('Encuentras un bar.')
    elif edificio == 5:
        print('Encuentras un edificio público.')
    elif edificio == 6:
        print('Encuentras un parque.')
#Listado de todas las acciones que se pueden realizar.
def ayuda():
    print('\n\n\n')
    print(' Parece que necesitas ayuda, aquí puedes leer los comandos básicos.')
    print('Para que un comando funcione tiene que estar escrito en minúsculas.')
    print('\nnorte ----> Moverte hacia el norte.')
    print('sur ----> Moverte hacia el sur.')
    print('oeste ----> Moverte hacia el oeste.')
    print('este ----> Moverte hacia el este.')
    print('lugar ----> Lugar en el que te encuentras.')
    print('salir ----> Salir del juego.')
    try:
        input('Pulsa enter para continuar...')
    except SyntaxError:
        pass

#Encargado de poner todo en marcha.
def empezar():
    os.system('clear')
    print('¡Bienvenido al gran simulador de andar!')
    print('Creado por P.R.B.')
    print(skyline)
    try:
         input('Pulsa enter para continuar...')
    except SyntaxError:
        pass
    time.sleep(1)
    os.system('clear')

    while True:
        accion()
        comprobarlimites()
#Pantalla de inicio.
def inicio():
    global mapabase
    os.system('clear')
    print(city)
    cmd1 = input(seleccion)
    if cmd1 == '1':
        crearmapa(mapabase)
        empezar()
    elif cmd1 == '2':
        cargar()
        empezar()
    elif cmd1 == '3':
        print('Parece que eres nuevo en este juego, así que bienvenido :)')
        print('El juego consiste en andar por la ciudad y nada más por ahora.')
        print('Para moverte mientras juegas escribe: norte,sur,oeste o este.')
        print('Si quieres más información escribe ayuda mientras juegas.')
        try:
            input('Pulsa enter para continuar...')
        except SyntaxError:
            pass
        os.system('clear')
        inicio()
    elif cmd1 == '4':
        sys.exit(0)
#Sistema de guardado de información en datos.txt
def guardar():
    print('Guardando...')
    time.sleep(0.5)
    global x,y,dinero,turnos
    txt = open('datos.txt','r+')
    txt.truncate()
    txt.write(str(x) +'\n')
    txt.write(str(y)+'\n')
    txt.write(str(dinero)+'\n')
    txt.write(str(turnos)+'\n')
    txt.close()
    print('Guardado realizado.')
#Sistema de carga de información desde datos.txt
def cargar():
    global x,y,dinero,turnos
    txt = open('datos.txt','r+')
    x = txt.readline()
    y = txt.readline()
    dinero = txt.readline()
    turnos = txt.readline()
    x,y,dinero,turnos = int(x[-2]),int(y[-2]),int(dinero[-2]),int(turnos[-2])
    txt.close()




alpha = 0 #Variable de cálculo.
mapabase = 3 #Tamaño del mapa.
x,y = 0,0 #Coordenadas del personaje.
edificio = 0 #Valor del edificio en el que te encuentras.
dinero = 0 #Dinero que tiene el personaje.
turnos = 0
seleccion = '''
1) Crear partida nueva.
2) Seguir partida.
3) Tutorial.
4) Salir.
'''
#Ascii Art
skyline = '''
                                  _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      |   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
city = '''               Walking Simulator v.1

                       | |
                       |'|            ._____
               ___    |  |            |.   |' .---"|
       _    .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''


inicio()
