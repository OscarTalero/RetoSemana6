'''Reto semana 5
Cola Univesidad extranjera
Oscar Talero
Version 1.0
Junio 5-2021'''

from collections import deque
import funciones as func

lista_postulados = [11,22,33]
cola = deque()
op = 'S'
while op == 'S':
    estudiante = int(input('Ingrese el codigo del estudiante: '))
    resultado = func.validar(lista_postulados,estudiante,cola)
    op = input('Consultar otro estudiante? '+ ' Si(S) '+' No(N) ')
print('Total estudiantes inscritos: ',len(resultado))
func.informe(resultado)
print('En promedio se inscribieron ',len(resultado)/3, ' estudiantes por programa')