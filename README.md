RetoSemana5
Descripción del Reto

Al departamento se le pasa una lista con todos los códigos de identificación de los estudiantes
que se han postulado a prácticas en el periodo 2021-2 (2021 - Segundo semestre). A pesar de que 
se habían programado citas por día y hora, se han presentado problemas al tratar de comunicarse
con cada uno, por tal motivo se ha decido atender por orden de llegada al DPA(Departamento de 
prácticas académicas).

A continuación, se presenta el quinto reto:

Asignación de Turno al Estudiante.

Esta funcionalidad tiene como objetivo asignar un numero de turno para ser registrado en
el DPA. La logística que se tiene es la siguiente, los turnos se asignan por orden de llegada
y se deben registrar los datos personales del estudiante.

Se debe implementar una función que permita:

Recibir como parámetros la lista de postulados (enviada por el departamento de prácticas académica
de la universidad) de todos los estudiantes a ser inscritos en alguno de los programas que se 
tienen abiertos y el número de identificación del estudiante que se postula.

Se debe validar que:

El documento del estudiante que se presenta para cursar la materia de prácticas académicas en el
periodo 2021-2, este en la lista enviada por el departamento de prácticas.

Que el estudiante no se haya inscrito ya

Asignarle un turno al estudiante de manera consecutiva de acuerdo con el orden de llegada y
guardarlo en una cola FIFO

Inscrito al Departamento de Prácticas

Esta función llama al estudiante respectivo de acuerdo con su posición en la cola y registra
los siguientes datos, de cada uno de los registrados:

Identificación
Nombre
Edad
Inscrito a prácticas (Ingeniería civil, Ingeniería de sistemas, Ingeniería electrónica)
Fecha y hora del registro
Reporte de Inscritos a prácticas académicas

Una vez terminado el registro se debe presentar un informe con:

Total Inscritos a prácticas
Total inscritos por tipo de programa
Promedio de inscritos por programa
