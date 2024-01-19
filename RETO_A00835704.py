'''
Emmanuel Naranjo Blanco - A00835704

Reto>>
Programa computacional para apoyar a mejorar habilidades y conocimientos en
lectura, matemáticas y ciencias, que evalúa la prueba PISA de la OCDE.

Fecha de entrega: 23/10/2022

'''

#Librerias
from time import * #permite utilizar la función sleep() para un mejor manejo visual del menú 
import os #permite utilizar funciones para acceder a las carpeta 

#Funciones
#----------------------------------------------------------#
def revision(respuestas,resultado):
#Esta función se encarga de revisar las respuestas brindadas por el usuario con las respuestas correctas del quiz
    nota=0
    i=0
    while i<5:
        if resultado[i]==respuestas[i]: #Las respuestas se almacenan en listas
            nota+=1
        i+=1
    nota=nota*20 #nota=(preg buenas * nota maxima) / cant preguntas
    
    return nota #retorna una nota en base a 100 puntos

#----------------------------------------------------------#
def guardar(nombre,calificacion_M,calificacion_E,calificacion_C):
#Esta función guarda el progeso del alumno en un archivo de texto y registra las prácticas realizadas en cada intento
    archivo=open(nombre+'.txt','r')
    cantidad=0
    
    for linea in archivo: #busca en el archivo del estudiante cada línea de texto
        linea = linea.strip()
        if linea.startswith('Intento '): #si la línea de texto inicia con "Intento" se suma al contador
            cantidad+=1   
    
    #La cantidad de prácticas realizada en un intento se guarda en listas y se guarda en el archivo propio del estudiante
    archivo=open(nombre+'.txt','a')
    
    #si las listas llegan vacías es porque en esa sesión no se practicó ese tema
    if calificacion_M == []:
        calificacion_M.append('No se practicó este tema durante esta sesión')
    if calificacion_E == []:
        calificacion_E.append('No se practicó este tema durante esta sesión')
    if calificacion_C == []:
        calificacion_C.append('No se practicó este tema durante esta sesión')
        
    #se guardan los datos en el archivo
    archivo.write('\nIntento '+str(cantidad+1)+'\n')
    archivo.write('Matematicas: '+str(calificacion_M)+'\n')
    archivo.write('Espanol: '+str(calificacion_E)+'\n')
    archivo.write('Ciencias: '+str(calificacion_C)+'\n')
    
    #se cierra el archivo
    archivo.close()

#----------------------------------------------------------#
def resumen(nombre):
#Función que muestra el resumen del estudiante a lo largo de sus prácticas e intentos realizados
    modo='r'
    file_name=nombre+'.txt'
    archivo=open(file_name,modo)
    contenido=archivo.readlines()
    
    print('\nRESUMEN DE ESTIDIANTE')
    print('- - - -')
    for i in range(len(contenido)):
        print(contenido[i])
    
    print('- - - -')
    #se le indican frases de aliento para que siga estudiando
    print('\nSIGUE PRACTICANDO')
    print('\nVAS MUY BIEN!')
    sleep(2)
    
#----------------------------------------------------------#
def estudiantes(lista_estudiantes):
#Esta función muestra todos los estudiantes que se encuentran practicando en la plataforma
    print('\nEstudiantes actualmente practicando:')
    print('- - - -')
    for nombre in lista_estudiantes: #recibe una lista con los archivos "nombres.txt" de todos los estudiantes registrados
        n=nombre.split('.')#Se divide el elemento cuando encuentra un "." y los guarda en una lista: [nombre,txt]
        print(n[0])#imprime el primer valor de la lista: nombre
    print('- - - -')
    print('No te detengas, sigue trabajando! :)')
    sleep(1.5)
    
#----------------------------------------------------------#
def pruebaMate():
#Funcion encargada de evaluar la práctica de matemáticas
    respuestas=['c','b','a','a','c']#respuestas del quiz
    resultado=[]#aquí se guardan las respuestas del alumno
    
    #pregunta 1
    #R/ c
    print('El Monte Fuji solo está abierto al público para escalar del 1 de julio al 27 de agosto de cada año.')
    print('Alrededor de 200 000 personas suben al monte durante ese período.')
    print('En promedio, ¿cuántas personas suben al Monte Fuji cada día?\n')
    
    print('a) 340')
    print('b) 710')
    print('c) 3400')
    print('d) 7100\n')
    
    preg1=input('Digite su respuesta --> ')
    resultado.append(preg1)
    
    #pregunta 2
    #R/ b
    print('En un viaje en bicicleta, Helen recorrió 4 km en los primeros 10 minutos y luego 2 km en los siguientes 5 minutos.')
    print('¿Cuál de las siguientes afirmaciones es correcta?\n')
    
    print('a) La velocidad promedio de Helen fue mayor en los primeros 10 minutos que en los siguientes 5 minutos.')
    print('b) La velocidad promedio de Helen fue la misma en los primeros 10 minutos y en los siguientes 5 minutos')
    print('c) La velocidad promedio de Helen fue menor en los primeros 10 minutos que en los siguientes 5 minutos')
    print('d) No es posible decir nada sobre la velocidad promedio de Helen a partir de la información dada\n')
    
    preg2=input('Digite su respuesta --> ')
    resultado.append(preg2)
    
    #pregunta 3
    #R/ a
    print('Helen recorrió 6 km hasta la casa de su tía. Su velocímetro mostró que fue a un promedio de 18 km/h.')
    print('¿Cuánto tardó?\n')
    
    print('a) Helen tardó 20 minutos en llegar a la casa de su tía.')
    print('b) Helen tardó 30 minutos en llegar a la casa de su tía.')
    print('c) Helen tardó 40 minutos en llegar a la casa de su tía.')
    print('d) No es posible saber cuánto tiempo tardó Helen en llegar a la casa de su tía.\n')
    
    preg3=input('Digite su respuesta --> ')
    resultado.append(preg3)
    
    #pregunta 4
    #R/ a
    print('Resuelva: (5+3)(7-4)(3-8)\n')
    
    print('a) -120')
    print('b) 120')
    print('c) -108')
    print('d) 108\n')
    
    preg4=input('Digite su respuesta --> ')
    resultado.append(preg4)

    #pregunta 5
    #R/ c
    print('Multiplica los siguientes monomios: (3x^3)(4xb)\n')
    
    print('a) 7·x^3·b')
    print('b) 12·x^3·b')
    print('c) 12·x^4·b')
    print('d) 7·x^4·b\n')
    
    preg5=input('Digite su respuesta --> ')
    resultado.append(preg5)
    
    nota=revision(respuestas,resultado)#se registra la nota del estudiante
    
    return nota

#----------------------------------------------------------#
def pruebaEspanhol():
#Funcion encargada de evaluar la práctica de español
    respuestas=['c','d','b','d','c']#respuestas del quiz
    resultado=[]#aquí se guardan las respuestas del alumno

    #pregunta 1
    #R/ c
    print('¿Qué nombre recibe una narración en el que el autor relata lugares, personajes y hechos reales?\n')
    
    print('a) Novela fantástica')
    print('b) Novela romántica')
    print('c) Novela realista')
    print('d) Novela caballeresca\n')
    
    preg1=input('Digite su respuesta --> ')
    resultado.append(preg1)
    
    #pregunta 2
    #R/ d

    print('En el texto narrativo es una forma básica de comunicación humana, cuyas características son:\n')
    
    print('a) Plantear el argumento de una historia desde un punto de vista indeterminado, en un tiempo pasado.')
    print('b) Comunicar una verdad científica a través de un lenguaje apropiado.')
    print('c) Describir las características de diversos personajes imaginarios.')
    print('d) Comunicar una historia en donde existen personajes que realizan acciones en un determinado tiempo y espacio.\n')
    
    preg2=input('Digite su respuesta --> ')
    resultado.append(preg2)
    
    #pregunta 3
    #R/ b
    print('Una utilidad que tienen las gráficas es:\n')
    
    print('a) Informarnos sobre la correcta elaboración y aplicación de una encuesta.')
    print('b) Mostrar de maner visual los resultados obtenidos mediante una encuesta.')
    print('c) Establecer una a una las diferencias entre las respuestas de cada persona de una encuesta.')
    print('d) Mostrar una a una las respuestas específicas de cada entrevistado de la encuesta.\n')
    
    preg3=input('Digite su respuesta --> ')
    resultado.append(preg3)
    
    #pregunta 4
    #R/ d
    print('El teatro o arte dramático tiene como una de sus características principales:\n')
    
    print('a) Narrar oralmente historias sobre acontecimientos diversos.')
    print('b) Presentar un escenario atractivo y novedoso.')
    print('c) Resaltar la personalidad de los actores.')
    print('d) Ser una expresión artística en donde actúan personajes de una historia.\n')
    
    preg4=input('Digite su respuesta --> ')
    resultado.append(preg4)
    
    #pregunta 5
    #R/ c
    print('Entre las características de un texto informativo se encuentran:\n')
    print('I. Dar a conocer objetivamente la realidad.')
    print('II. Ser un escrito muy breve y con un estilo literario.')
    print('III. Utilizar en lenguaje figurativo.')
    print('IV. Tener una estructura organizativa sencilla que contenga: introducción, desarrollo y conclusión.')
    print('Tener párrafos muy extensos y un lenguaje complicado.\n')
    
    print('a) I y II')
    print('b) III y V')
    print('c) I y IV')
    print('d) II y V\n')
    
    preg5=input('Digite su respuesta --> ')
    resultado.append(preg5)
    
    nota=revision(respuestas,resultado)#se registra la nota del estudiante
    
    return nota

#----------------------------------------------------------#
def pruebaCiencias():
#Funcion encargada de evaluar la práctica de ciencias    
    respuestas=['d','c','a','d','a']#respuestas del quiz
    resultado=[]#aquí se guardan las respuestas del alumno
   
    #pregunta 1
    #R/ d
    print('La mayoría de las aves se reúnen en un área y después migran en grandes grupos.')
    print('¿Cuál considera que es la explicación científica de este comportamiento?\n')
    
    print('a) Volar en grandes grupos permite que aves de otras especies se sumen.')
    print('b) Las aves que migraban solas o en pequeños grupos podían encontrar mejor alimento.')
    print('c) Volar en grandes grupos les permite encontrar mejores lugares para anidar.')
    print('d) Las aves que migraban solas o en grupos pequeños tenían menos probabilidades de sobrevivir y reproducirse.\n')
    
    preg1=input('Digite su respuesta --> ')
    resultado.append(preg1)
    
    #pregunta 2
    #R/ c
    print('Las rocas del espacio que entran en la atmósfera terrestre se llaman "meteoroides". En su recorrido se calientan y brillan.')
    print('Se pueden consumir antes de tocar la superficie, pero cuando la tocan, generan un agujero llamado cráter.')
    print('Mientras un meteoroide se acerca a la Tierra y su atmósfera, se acelera. ¿Por qué pasa eso?\n')
    
    print('a) Lo atrae la rotación de la Tierra.')
    print('b) Lo empuja la luz del Sol.')
    print('c) Lo atrae la masa de la Tierra.')
    print('d) Lo expulsa el vacío del Espacio.\n')
    
    preg2=input('Digite su respuesta --> ')
    resultado.append(preg2)
    
    #pregunta 3
    #R/ a
    print('¿Qué es la inercia?\n')
    
    print('a) Cuando un cuerpo se mantiene en el estado que se encuentra.')
    print('b) Cuerpos en movimiento.')
    print('c) Cuerpo en movimiento indefinidamentea.')
    print('d) Cuerpo que se desplaza.\n')
    
    preg3=input('Digite su respuesta --> ')
    resultado.append(preg3)

    #pregunta 4
    #R/ d
    print('Forma parte de la sangre en un 70% y ayuda a eliminar los desechos,además de regular la temperatura de nuestro cuerpo.\n')
    
    print('a) Azúcar.')
    print('b) Grasa.')
    print('c) Lípidos.')
    print('d) Agua.\n')
    
    preg4=input('Digite su respuesta --> ')
    resultado.append(preg4)
    
    #pregunta 5
    #R/ a
    print('Son organismos que no requieren consumir alimentos por lo que se les llama productores,')
    print('ya que transforman la energía del sol en energía química que se almacena en forma de carhohidratos.\n')
    
    print('a) Plantas y algas.')
    print('b) Hongos y bacterias.')
    print('c) Herbívoros.')
    print('d) Hongos.\n')
    
    preg5=input('Digite su respuesta --> ')
    resultado.append(preg5)
    
    nota=revision(respuestas,resultado)#se registra la nota del estudiante 
    
    return nota

#----------------------------------------------------------#
#El siguiente código busca en la carpeta actual donde está guardado el programa .py y guarda los elementos en una lista llamada contenido
lista_estudiantes=[]
contenido = os.listdir()
for fichero in contenido:#se busca en cada elemento de la lista
    if os.path.isfile(os.path.join(fichero)) and fichero.endswith('.txt'):#condicional que determina si el elemento es un archivo de tipo .txt
        lista_estudiantes.append(fichero)#lista que guarda todos los documentos .txt encontrados en la carpeta, estos serías los archivos de cada estudiante
        
#----------------------------------------------------------#

#Menú principal
while True:
    #Variables donde se guardan las notas de cada tema de la sesión actual
    calificacion_M=[]
    calificacion_E=[]
    calificacion_C=[]

    print('\n* BIENVENIDO ESTUDIANTE *\n')#saludo
    print ('a. Registro de estudiante\n')#agrega estudiante al sistema
    print ('b. Sigue aprendiendo')#si ya el estudiante está registrado puede ingresar a las prácticas
    print ("c. Estudiantes estudiando")#muestra todos los estudiantes registrados
    print ("d. Tu Resumen")#Muestra el resumen del estudiante, sus intentos y calificaciones por tema
    print('e. Salir\n')#salir del menú

    opcion = input('Opcion -> ')

#----------------------------------------------------------#
    if opcion == 'a':
        print('Datos de estudiante\n ')
        nombre=input('Nombre: ')
        edad=float(input('Digite su edad en años: '))
        instituto=input('Indique el instituto de procedencia: ')

        modo='w'
        file_name=nombre+'.txt'
        archivo=open(file_name,modo)

        #crear archivo con datos del nuevo estudiante
        archivo.write('-Práctica para la prueba PISA en los temas de Matemática, Español y Ciencias-\n')
        archivo.write('-- -- --\n')
        archivo.write('Estudiante: '+nombre+'\n')
        archivo.write('Edad: '+str(edad)+'\n')
        archivo.write('Institucion: '+str(instituto)+'\n')
        archivo.close()
        lista_estudiantes.append(nombre+'.txt')#agrega en la lista actual de todos los estudiantes registrados 

        print('\n>>> Registrado correctamente')
        sleep(1)

#----------------------------------------------------------#
    elif opcion == 'b':
        nombre=input('Digite su nombre: ')
        if nombre+'.txt' in lista_estudiantes:#si el estudiante ya está registrado ingresa a las pruebas
            #menú secundario
            while True:
                #Desplegar opciones:
                print ("\n**************************\n")
                print ("Práctica por tema de la Prueba PISA")
                print ("\n**************************\n")
                print ("a. Práctica de Matemáticas")
                print ("b. Práctica de Español")
                print ("c. Práctica de Ciencias\n")
                
                
                print ("d. Guardar y salir")#Guarda los datos de la sesión y regresa al menú principal
    
                opcion = input('Opcion -> ')
                
                if opcion in ['a','b','c','d']:
                
                    if opcion == 'a':

                        resultado=pruebaMate()
                        print('\nSu resultado en esta prueba fue >> ',resultado)
                        calificacion_M.append(resultado)#se guarda en lista de calificaciones para este intento

                    elif opcion == 'b':
                        resultado=pruebaEspanhol()
                        print('\nSu resultado en esta prueba fue >> ',resultado)
                        calificacion_E.append(resultado)#se guarda en lista de calificaciones para este intento
                            
                        
                    elif opcion == 'c':
                        resultado=pruebaCiencias()
                        print('\nSu resultado en esta prueba fue >> ',resultado)
                        calificacion_C.append(resultado)#se guarda en lista de calificaciones para este intento
                    
                    
                    elif opcion == 'd':
                        guardar(nombre,calificacion_M,calificacion_E,calificacion_C)
                        break
        
        
        else:
            print('\nEstudiante aun no escrito en el sistema. Favor de registrarse.')
            sleep(1)
            
#----------------------------------------------------------#    
    elif opcion == 'c':
        estudiantes(lista_estudiantes)

#----------------------------------------------------------#    
    elif opcion == 'd':
        nombre=input('Digite su nombre: ')
        if nombre+'.txt' in lista_estudiantes:#si el estudiante ya está registrado ingresa a las pruebas
            resumen(nombre)
            sleep(1.5)
        else:
            print('\nEstudiante aun no escrito en el sistema. Favor de registrarse.')
            sleep(1)
                        
#----------------------------------------------------------#
    elif opcion == 'e':
        print('\n\nGracias por usar nuestros servicios, que tenga un excelente día!')
        break        
       
    else:#si la opcion ingresada no es correcta
        print('* Opcion inválida, intente de nuevo. *')
        sleep(1)
     
        
        