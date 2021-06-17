'''Reto semana 6
Cola Univesidad extranjera con
ficheros y grafico
Oscar Talero
Version 2.0
Junio 14-2021'''

import funciones as func

eleccion = 'S'
cont = 0
while eleccion == 'S':
    print('*'*23)
    print('* ','MENU DE OPCIONES ',' *')
    print('*'*23,)
    print('1. Consultar e inscribir estudiante')
    print('2. Generar informes')
    print('3. Generar graficos de informes')
    print('4. Salir')
    op = int(input('Ingresa la opcion: '))
    while op < 1 or op > 4:
        print('Debe ingresar una opcion del Menu')
        op = int(input('Ingresa la opcion: '))
    if op == 1:
        opcion = 'S'
        while opcion == 'S':
            estudiante = int(input('Ingrese el codigo del estudiante: '))
            func.validar(estudiante)
            opcion = input('Consultar otro estudiante? '+ ' Si(S) '+' No(N) ')
    if op == 2:
        total,cont = func.informe('inscritos.txt',cont)
    if op == 3:
        if cont == 0:
            print('\n','Debe generar primero los informes','\n')
        else:
            func.graficos(total)
    if op == 4:
        eleccion ='N'