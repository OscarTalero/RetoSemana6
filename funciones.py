'''Reto semana 6
Funciones Univesidad extranjera con
ficheros y graficos
Oscar Talero
Version 2.0
Junio 14-2021'''

import datetime
import os
import matplotlib.pyplot as plt

def convertir(archivo):
    '''Funcion abre el archivo y guarda los datos en una lista
    Parametros
    ----------
    archivo : string

    Retorna
    -----------
    Retorna la lista que esta guarda en el archivo
    '''
    with open(archivo,'r') as lista:
        contenido = lista.read()
        lista_archivo = contenido.split('\n')
        return lista_archivo
    

def validar(estudiante):
    '''Funcion que valida si el estudiante esta postulado o inscrito
    Parametros
    ----------
    estudiante : int
    '''
    estudiante = str(estudiante)
    postulados = convertir('codigos_estudiantes.txt')
    if os.path.isfile('/home/oscar/MinTic/semana6/RetoSemana6/inscritos.txt'):
        inscritos = convertir('inscritos.txt')
    else:
        file = open('inscritos.txt','w')
        inscritos = convertir('inscritos.txt')
        file.close()
    if estudiante in postulados:
        print('Estudiante ',estudiante,'SI se encuentra en el archivo de postulados')
    else:
        print('Estudiante',estudiante,' NO se encuentra en el archivo de postulados')
    cont = 1
    print(len(inscritos))
    if len(inscritos) == 1:
        inscribir(estudiante)
    for i in range((len(inscritos)-1)):
        lista = inscritos[i].split(',')
        if estudiante in lista:
            print('Estudiante ',estudiante,'YA INSCRITO')
            cont = 1
            break
        else:
            cont = 0
    if cont == 0:
        print('Estudiante ',estudiante,' NO INSCRITO')
        inscribir(estudiante)


def inscribir(estudiante):
    '''Funcion que inscribe a los estudiantes en un programa 
    de la universidad y los guarda en un archivo
    Parametros
    ----------
    estudiante : int
    '''
    print('Ingrese los datos del estudiante :')
    codigo = estudiante   
    print('Ingrese el codigo: ',codigo)
    identificacion = int(input('Ingrese la identificacion: '))
    nombre = input('Ingrese el nombre: ')
    edad = int(input('Ingresese la edad: '))
    print('Seleccione el programa al que desea inscribirse:' )
    print('1. Ingenieria Civil')
    print('2. Ingenieria de Sistemas')
    print('3. Ingenieria Electronica')
    opcion = int(input(''))
    while opcion < 1 or opcion > 3:
        opcion = int(input('Digite un numero entre 1 y 3'))
    if opcion == 1 :
        programa = 'Ingenieria Civil'
    if opcion == 2 :
        programa = 'Ingenieria de Sistemas' 
    if opcion == 3 :
        programa = 'Ingenieria Electronica'
    fecha = datetime.datetime.today()
    fecha = fecha.strftime('%d %B %Y %H:%M:%S')
    estudiantes = [codigo,identificacion,nombre,edad,programa,fecha]
    with open('inscritos.txt','a') as inscritos:
        inscritos.writelines([str(codigo),',',str(identificacion),',',nombre,',',str(edad),',',programa,',',fecha,'\n'])


def informe(archivo,cont):
    '''Funcion que imprime los informes de los estudiantes
    Parametros
    ----------
    archivo : string
    Retorna
    ----------
    Imprime por pantalla los informes solicitados
    '''
    cont = 1
    total = []
    contar_civil = 0
    contar_sistemas = 0
    contar_electronica = 0
    inscritos = convertir('inscritos.txt')
    for i in range((len(inscritos)-1)):
        lista = inscritos[i].split(',')
        contador = lista.count('Ingenieria Civil')
        contar_civil += contador
        contador = lista.count('Ingenieria de Sistemas')
        contar_sistemas += contador
        contador = lista.count('Ingenieria Electronica')
        contar_electronica += contador
        contador = 0
    print('\n','Total estudiantes inscritos: ',(len(inscritos))-1)
    print('\n','Total inscritos en Ingenieria Civil: ',contar_civil)
    print('Total inscritos en Ingenieria de Sistemas: ',contar_sistemas)
    print('Total inscritos en Ingenieria Electronica: ',contar_electronica)
    print('\n','En promedio se inscribieron ',len(inscritos)/3,'estudiantes','\n')
    total.append(contar_civil)
    total.append(contar_sistemas)
    total.append(contar_electronica)
    return total,cont
    


def graficos(estudiantes):
    programas = ['Ingenieria Civil','Ingenieria de Sistemas','Ingenieria Electronica']
    plt.pie(estudiantes, labels = programas,autopct="%0.1f %%")
    plt.title('CANTIDAD DE ESTUDIANTES POR PROGRAMA')
    plt.show()