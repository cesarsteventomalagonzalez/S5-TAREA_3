##Nombre: TOMALA GONZALEZ CESAR STEVEN.
#TAREA DE EJERCICIOS DESARROLLAR EJERCICIOS DE LÓGICA EN PYTHON.
#Carrera de ingenieria en Software.

class operaciones:

    def tipo_dato(self):
        
        print("¿De qué tipo son los siguientes datos?")
        print("150/5 es un dato: {} ".format(type(150/5)))
        print( "-"*15)
        print("7/2 es un dato: {}".format(type(7/2)))
        print( "-"*15)
        print("7//2 es un dato: {}".format(type(7//2)))
        print( "-"*15)
        print("7%2 es un dato: {}".format(type(7%2)))
        print( "-"*15)
        print("a es un dato: {}".format(type("a")))
        print( "-"*15)
        print("tiza + . es un dato: {} ".format(type("tiza" + ".")))
        print( "-"*15)
        print("hola [1+1] es un dato: {} ".format(type("hola"[1+1])))
        print( "-"*15)
        print("len(hola) es un dato: {} ".format(type(len("hola"))))
        print( "-"*15)
        print(" int(145) es un dato: {} ".format(type(int("145"))))
        print( "-"*15)
        print("float('145') es un dato: {} ".format(type(float("145"))))
        print( "-"*15)
        print("float(145) es un dato: {} ".format(type(float(145))))
        print( "-"*15)
        print("str(32) es un valor: {} ".format(type(str(32))))
        print( "-"*15)
        print(" 1+2!=3 es un dato: {} ".format(type(1+2!=3)))
        print( "-"*15)
        print(" 177%2==0 es un dato: {} ".format(type(177%2==0)))
        print( "-"*15)
        print("len('nube')<=20 es un dato: {} ".format(type(len("nube")<=20)))
    
    def cada_operación (self):

        print("¿Qué guardan las variables luego de cada operación?")
        a=160/10
        print("n=160/10 tiene un valor de = {} ".format(a))
        print( "-"*25)
        b=167//10
        print("n=167//10 tiene valor de = {} ".format(b))
        print( "-"*25)
        print("letra = a ")
        letra = "a"
        print(letra)
        print( "-"*25)
        saludo="hola"+letra
        print("La impresión de saludo='hola'+'letra es igual a: {} ".format(saludo))
        print( "-"*25)
        print("C=saludo[0]")
        C=saludo[0]
        print(C)
        print( "-"*25)
        print("C=saludo[1+3]")
        C=saludo[1+3]
        print(C)
        print( "-"*25)
        print("L = len(saludo)")
        L = len(saludo)
        print(L)
        print( "-"*25)
        print("C=saludo[len(saludo)-1]")
        C=saludo[len(saludo)-1]
        print(C)
        print( "-"*25)
        print("menor='a'<'b'")
        menor = "a" < "b"
        print(menor)
        print( "-"*25)
        print("D=1!=1")
        D=1!=1
        print(D)
        print("-"*25)
        print("N ='cinta'>='canto'")
        N = "cinta" >= "canto"
        print(N)
        print("-"*25)
        print("c='z'+'a'+'paz[0]'")
        c="z"+"a"+"paz"[0]
        print(c)
        print("-"*25)
        print("x=c[0]=='z'")
        x = c[0] == "z"
        print(x)
    
    def error_sintaxis(self):

        print("11-(4%2+10)")
        print(11-(4%2+10))
        print("-"*25)
        print("'30' + 2")
        print("Error, no se puede agregar un int a str")
        print("'30' + '2'")
        print("30"+"2")
        print("-"*25)
        print("'hola'[len('hola')]")
        print("Error, se encuentra fuera del rango")
        print("-"*25)
        print("len(124)")
        print("No se puede contar un valor entero")
        print("-"*25)
        print("El valor de len('fin') es: {}".format(len("fin")))
        print("'hola'[len('fin')]")
        print("hola"[len("fin")])
        print("-"*25)
        print("'hola'[11-(4%2+10)]")
        print("hola"[11-(4%2+10)])
        print("-"*25)
        print("int('4')")
        print(int(4))
        print("-"*25)
        print("int(4)")
        print(int(4))
        print("-"*25)
        print("int('z')")
        print("Un letra no puede tener un valor entero")
        print("-"*25)
        print("int('4.'")
        print("Al ser '.' un caracter, no puede tomar valores numéricos")
        print("-"*25)
        print("4<'f'")
        print("No se puede realizar la comparación debido a que es entre un int y un str")
        print("-"*25)
        print("'palabra'='rama'")
        print("Error, se está queriendo asignar un valor a un string")
        print("-"*25)
        print("'palabra'=='rama'")
        print("palabra"=="rama")

    def trueOrfalse (self):
        print("¿Qué resutlado (True/False) dan las siguientes operaciones")
        print("not True: {} ".format(not True))
        print("-"*25)
        ñ = not(1+2!=3)
        print("not(1+3!=3): {} ".format(ñ))
        print("-"*25)
        x=(len("jugar")>5) and (len("jugar")<10) 
        print("x=(len('jugar')>5) and (len('jugar')<10): {} ".format(x))
        print("-"*25)
        y = "alto"[2]=="t" and x
        print("'alto'[2]=='t' and x: {} ".format(y))
        print("-"*25)
        d = 842913%10!=3 and len("café")==3
        print("842913%10!=3 and len('café')==3 : {} ".format(d))
        print("-"*25)
        g = 0!=0 or 'a'<'y'
        print("0!=0 or 'a'<'y': {} ".format(g))
        print("-"*25)
        f = True or int('50')>=50
        print("True or int('50')>=50 : {} ".format(f))
        print("-"*25)
        edad = 20 
        k = not (x) or edad%2 == 0
        print("edad = 20, not (x) or edad%2 == 0 es: {} ".format(k))
        print("-"*25)
        es_cliente = False
        l = not (es_cliente and not (edad<18))
        print("es_cliente = False, not (es_cliente and not (edad<18) : {} ".format(l))

    def corregir_error(self):

        print("¿Qué errores tienen estas proposiciones? ¿Cómo deben corregirse?")
        a = "número >= 0 and número =< 100"
        print("El número no puede ser menor que 0 ni mayor que 100\n La sintaxis incorrecta es: número < 0 and número > 100\n Pero la forma correcta es: {} ".format(a))
        print("-"*25)
        print("La edad debe estar entre 10 y 20\n Sintaxis incorrecta: edad>10 and <20\n La sintaxis adecuada es: edad > 10 and edad < 20 ")
        print("-"*25)
        print("La longitud de la cadena no debe ser superior a 10 caracteres.\n La manera incorrecta es: len(cadena)<10\n La adecuada es: len(cadena)<=10")

    def expresar_operación(self):

        print("El número es múltiplo de 4 y también es negativo")
        n= int(input("Ingrese un número para conocer si es múltiplo de 4: "))
        multi = n % 4 
        if multi == 0:
            print("Es un múltiplo de 4")
            if n < 0:
                print("Es negativo")
            else: 
                print("No es negativo")
        else:
            print("No es un múltiplo") 
        print("-"*25)
        print("Decidiste comprar un auto usado, pero debe cumplir ciertas condiciones: El kilometraje debe ser menor a 30000 y el modelo debe estar entre 2015 y 2017")
        kilometraje = int(input("Kilometraje del automovil: "))
        año = int(input("Año del modelo del carro: "))
        if kilometraje < 30000 and (año > 2015 and año < 2017):
            print("Cumple con las condiciones para la compra")
        else: 
            print("No cumple con las expectativas")
        print("-"*25)
        print("Una agrupación académica tiene ciertos requisitos para cualquier estudiante que desea ingresar:\n Debe tener más del '30%' de sus estudiantes completos y no debe ser miembro de otra agrupación académica en la misma universidad")
        print("total > 30 and not(miembro_agrupación) ")
        print("-"*25)
        print("Una persona pasa frío si es invierno y además, no tiene calefacción ni está abrigada")
        print("invier and not tiene_calefacción and not está_abrigada")
        print("invier and not (tiene_calefacicón or está_abrigada)")

    def Cadena(self):

        print("¿Cuál es el resultado?")
        cadena = "sí, profe, es cierto... yo me comí la tarea"
        op1 = cadena[10]
        print("El resultado es: '{}'".format(op1))
        op2 = cadena[-1]
        print("El resultado es: '{}'".format(op2))
        op3 = cadena[0:9]
        print("El resultado es: '{}'".format(op3))
        op4 = cadena[::3]
        print("El resultado es: '{}'\n".format(op4))
        
        print("¿Cómo obtener?")
        print("a) La cadena al revés") 
        print("La cadena al revés es: '{}'".format(cadena[::-1]))
        print("b) La subcadena 'profe'")
        print("La subcadena 'profe': '{}'".format(cadena[4:9]))

    def Operaciones(self):
        print("Dada la variable s ='   hola, ¿cómo estás?' con 3 espacios al inicio, ¿qué se obtiene en cada una de las siguientes operaciones?\n")

        s = "   hola, ¿cómo estás?"
        op1 = s[::-1]
        print("El resultado de es: '{}'".format(op1))
        #s[len(s)]
        print("La longitud de la cadena (s[len(s)] = 21) es mayor al índice de la cadena (índice = 20), por lo tanto, me arrojará un error")
        op2= s[len(s)-1]
        print("El resultado es: '{}'".format(op2))
        op3 = s.count("o")
        print("El resultado es: '{}'".format(op3))
        op4 = s.count("Hola")
        print("El resultado es: '{}'".format(op4))
        op5 = s[-4:]
        print("El resultado es: '{}'".format(op5))
        op6 = s[15:]
        print("El resultado es: '{}'".format(op6))
        op7 = s.find("o")
        print("El resultado es: '{}'".format(op7))
        op8 = s.strip()
        print("El resultado es: '{}'".format(op8))
        op9 = s.upper()
        print("El resultado es: '{}'".format(op9))
        op9 == s
        print("El resultado es: '{}'".format(op9==s))
        op10 = s[14:].upper()
        print("El resultado es: '{}'".format(op10))
        op11 = len(s) % 2 != 0
        print("El resultado es: '{}'".format(op11))
        op12 = s.replace(" ", "*")
        print("El resultado es: '{}'".format(op12))
        op13 = s.replace("z", "Z")
        print("El resultado es: '{}'".format(op13))

    def Preguntas(self):
        print("Dada la variable X de tipo string, ¿cómo se puede hallar el índice del último caracter?")
        X = "La paz nunca fue una opción"
        print("El índice del último caracter es: '{}'".format(X.index("n",19)), "--> Primer método")
        print("El índice del último caracter es: '{}'".format(X.find("n",19,27)),"--> Segundo método\n")
        
        print("Dada la variable cadena = 'hola', ¿qué retorna cadena.find('2')?")
        cadena = "hola"
        print("Retorna: {}".format(cadena.find('2')),"\n")

        print("¿Qué retorna 'a' in 'dátiles'?")
        print("Retorna:",'a' in 'dátiles', "\n")

        print("¿Qué valor retorna la posición del primer espacio en 'me gusta programar'")
        y = "me gusta programar"
        print("El índice del primer espacio es: {}".format(y.index(" ")),"\n")

        print("¿Qué valor retorna la cantidad de espacios de la cadena 'me gusta programar'?")
        m = "me gusta programar"
        print("La cantidad de espacios en la cadena es de: {}".format(m.count(" ")),"\n")

        print("¿Por qué da error cadena[0] = 'H'?")
        respuesta = "Porque el dato string contenido en la variable cadena es inmutable, es decir, no puede ser cambiado."
        print(respuesta, "\n")

        print("¿Qué almacena la siguiente variable? nueva = 'C' + cadena[1:]")
        nueva = "C" + cadena[1:]
        print("Almacena: '{}'".format(nueva), "\n")

        print("¿Cómo reemplazar las vocales acentuadas por vocales no acentuadas en la cadena X?")
        z = "La sandía está dulce"
        k = z.replace("í","i").replace("á","a")
        print("{}".format(k),"\n")

        print("¿Qué comparación podría hacerse para averiguar si la longitud de la cadena es par?")
        cadena = input("Escriba una frase: ")
        if len(cadena) % 2 == 0:
            print("La longitud de la cadena es par.")
        else:
            print("La longitud de la cadena es impar.",)

        
        print("\n¿De qué forma se puede obtener la cantidad de vocales de la cadena X?")
        X = "La paz nunca fue una opción"
        n = X.replace("ó", "o")
        suma = n.count("a") + n.count("e") + n.count("i") + n.count("o") + n.count("u")
        print("La cantidad de vocales en la cadena es: {}".format(suma))


    def problemas_instrucciones(self):
        print("¿Qué problemas tienen las siguientes instrucciones? ¿Cómo lo solucionarías?")
        print("A = input(nombre, '¿Cuál es tu canción favorita?)'\nCorrección: A = input('¿Cuál es tu canción favorita?:')\n")  
        print("precio = input('Precio:')\ntotal = precio+(precio*0.10)\nCorreción: 'precio= float(input('Precio:')\n total = precio+(precio*0.10)\n")
        print("edad = int(input('edad:'), manera incorrecta: print(tu edad es, edad)\nCorrección: print('Tu edad es: ',edad")
        print("edad=int(input('Edad'), forma incorrecta: print('Veamos si tu edad es 18...', edad=18)\nCorrección: print('Veamos si tu edad es 18...', edad==18)")
        
    def usuario(self):
        #Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada N.
        # A continuación, se debe mostrar en pantalla el texto 'Ahora estás en la mátrix, []', donde '[usuario]' se reemplazará el nombre que el usuario haya ingresado
        N = input("¿Cuál es tu nombre?: ")
        print("Ahora estás en la mátrix, {}. ".format(N),"\n")

    def monto_final(self):
        print("Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un '6.2%' en concepto de servicio y un '10%' de propina.\nImprimir en pantalla el monto final a pagar")
        c = float(input("¿Cuánto costó la comida?: $"))
        servicio = c * 0.062
        propina = c * 0.1
        costo = c + servicio + propina 
        print("El precio a pagar es: ${} ".format(costo))

    def nacimiento(self):
        #Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica(en total, tres variables diferentes). 
        #Finalmente, mostrar la fecha en formato  'dd/mm/aaaa'")
        día = int(input("Día en que nació: "))
        mes = int(input("Mes en el que nació (En números): "))
        año = int(input("Año en que nació: "))
        print("Su fecha de nacimiento es: {}/{}/{}".format(día,mes,año))

    def motociclistas(self):
        kilometros_puede_recorrer = int(input("¿Cuántos kilómetros recorre con 1 litro de combustible?: "))
        capacidad_tanque = float(input("¿Qué capacidad en litros tiene el tanque de la moto?: "))
        distancia_a_recorrer = float(input("¿Cuántos kilómetros recorrerá en total?: "))

        litros_nec = distancia_a_recorrer/kilometros_puede_recorrer

        tanques_nec = litros_nec/capacidad_tanque
        tanques_necround = round(tanques_nec, 2)

        print("La cantidad de tanques necesarios con capacidad de {} son: {} ".format(capacidad_tanque,tanques_necround),"litros")


        #Un empresario que se dedica al espectáculo necesita un programa que le ayude a hacer ciertos cálculos 
        #cada vez que organiza un concierto en un estadio deportivo.
        
        #Lo primero que necesita saber es qué capacidad de público tendrá cada concierto, para saber cuántas entradas o 
        #boletos tienen que imprimirse.

        #Para eso, cuando contrata un estadio deportivo, pregunta cuántos metros cuadrados tiene. Él sabe que por metro cuadrado 
        #caben 4 personas. También sabe que siempre hay un espacio con gradas y que normalmente éstas ocupan un 20% de los metros 
        #cuadrados totales. En cada estadio las gradas pueden ser diferentes, así que el empresario consulta cuánta gente cabe en ellas.

        #Cuando contrata a la banda que dará el concierto, ésta le indica qué porcentaje del espacio disponible necesitan ellos para 
        #montar su escenario.

        #Con estos datos, debe calcularse cuánta gente va a caber en el estadio para un concierto determinado. El empresario, cada vez que 
        #use el programa, va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrató, la cantidad de gente que cabe en 
        #las gradas y el porcentaje de espacio ocupado por el escenario.

        #Luego, él quiere saber cuánto dinero ingresaría si vende todas las entradas disponibles, sabiendo que el 30% de las entradas vendidas 
        #serán "a precio especial" y el resto son "a precio común". El empresario ingresa el precio de cada tipo de entrada cuando usa el programa.

    def Empresario(self):
         
        espacio_estadio = float(input("Tamaño del estadio deportivo: "))
        espacio_estadio_en_metros_cuadrados = espacio_estadio**2
        espacio_estadio_en_metros_cuadradosround = round(espacio_estadio_en_metros_cuadrados, 2) 
        print("El espacio total del estadio es de: {}".format(espacio_estadio_en_metros_cuadradosround),"metros cuadrados\n")

        espacio_gradas = espacio_estadio_en_metros_cuadradosround * 0.20
        espacio_gradasround = round(espacio_gradas, 2)
        print("El espacio que ocupa las gradas es de: {}".format(espacio_gradasround),"metros cuadrados")
        público_en_gradas = int(input("La cantidad de personas que caben en las gradas es de: "))
        
        print("\n")
        porcentaje_espacio_escenario = int(input("Ingrese el espacio ocupado por el escenario: ")) 
        espacio_escenario_banda = espacio_estadio_en_metros_cuadradosround * (porcentaje_espacio_escenario/100)
        print("El espacio que necesita la banda para montar el escenario es de: {}".format(espacio_escenario_banda),"metros cuadrados\n")
    
        espacio_disponible = espacio_estadio_en_metros_cuadradosround - espacio_gradasround - espacio_escenario_banda
        capacidad_público = ((espacio_disponible) * 4) + público_en_gradas
        capacidad_públicoround = round(capacidad_público, 2)
        print("Para un concierto, en el estadio caben: {}".format(capacidad_públicoround),"personas")
        cantidad_boletos = capacidad_público
        print("Cantidad de boletos: {}".format(cantidad_boletos)) 

        
        precio_especial = float(input("Ingresar precio especial de boleto: $"))
        precio_común = float(input("Ingresar precio de boleto: $"))
        ingresos_totales = (cantidad_boletos * 0.30)* precio_especial + (cantidad_boletos * 0.70) * precio_común
        print("El total de ingresos es de: ${}".format(ingresos_totales))



        #Escribir un programa que, dado un número entero, muestre su valor absoluto

    def absoluto(self):
        entero = int(input("Ingresar un numero entero: "))
        if entero > 0:
            print("El|{}|".format(entero),"es: {}".format(entero))
        elif entero == 0:
            print("El |{}|".format(entero),"es: {}".format(entero))
        else:
            entero = entero * -1
            print("El |{}| ".format(entero),"es: {}".format(entero))


        #Solicitar al usuario los nombres de dos personas los cuales se almacenarán en dos variables
        #A continuación, imprimir "coincidencia" si los nombres de ambas personas comienzan con la misma letra o si terminan
        #con la misma letra. Si no es así, imprimir "no hay coincidencia".

    def coincidencia(self):
        nombre1 = input("Ingresar un nombre: ")
        nombre2 = input("Ingresar un segundo nombre: ")  
        if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
            print("Coincidencia")
        else:
            print("No hay coincidencia")
    
    #Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo,
    #candidato B por el partido verde, candidato C por el partido azul. 

    def candidatos(self):
        usuario = input("Ingresar una letra A, B O C: ")
        if usuario == "A":
            print("{}: Usted ha votado por el partido rojo".format(usuario))
        elif usuario == "B":
            print("{}: Usted ha votado por el partido verde".format(usuario))
        elif usuario == "C":
            print("{}: Usted ha votado por el partido azul ".format(usuario))
        else:
            print("Opción errónea")
    
    #Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "es vocal".
    #Se debe validar que el usuario ingrese solo un caracter.Si ingresa un string de mas de un caracter, informarle que no
    #se puede proceder al dato

    def caracter(self):
        letra = input("Ingresar una letra:")
        vocales = "aeiou"
        if len(letra) != 1:
            print("No se puede proceder al dato")
        elif letra in vocales:
            print("Es una vocal")

    #Hacer un programa que permita si un año es bisiesto. 
    #Para que un año sea bisiesto debe ser divisible por 4 y no dibe ser divisible por 100
    #excepto que tambien sea divisible por 400. 

    def año(self):
        bisiesto = int(input("Ingrese un año: "))
        if ((bisiesto % 4 == 0) and (bisiesto%100 != 0) or (bisiesto % 400 == 0)):
            print("El año es bisiesto: {} ".format(bisiesto))
        else:
            print("No es un año bisiesto: {} ".format(bisiesto))


    def fechaformato(self):
        fecha = input("Fecha (formato 'dia, DD/MM'): ")
        fecha = fecha.lower()
        diasemana = fecha[0:fecha.find(',')]
        dianro = int(fecha[fecha.find(' ')+1:fecha.find('/')])
        mesnro = int(fecha[fecha.find('/')+1:])

        if dianro > 31 or mesnro >12:
            print("Fecha incorrecta")
        else:
            if diasemana in "lunes, martes, miércoles":
                respuesta = input("¿Se tomaron exámenes? S/N: ")
                if respuesta.lower() == "s":
                        aprobados = int(input("Cantidad de aprobados: "))
                        reprobados = int(input("Cantidad de reprobados: "))
                        print("Porcentaje de aprobados: ", (aprobados*100)/(aprobados+reprobados),"%")
            elif diasemana == "jueves":
                asistencia = int(input("Porcentaje de asistencia: "))
                if asistencia > 50:
                    print("Asistió la mayoría")
                else:
                    print("No asistió la mayoría")
            elif diasemana == "viernes":
                if dianro == 1 and (mesnro == 1 or mesnro == 7):
                    print("Comienzo de nuevo ciclo")
                    alumnos = int(input("Cantidad de alumnos: "))
                    arancel = float(input("Arancel: $"))
                    print("Ingreso total: $", alumnos*arancel)
            else:
                print("Fecha incorrecta")
        print("Fin del programa") 

    # EJERCICIOS CON FOR:

    # llegar al doble  de un numero ingresado.

    def doble_del_numero (self):
        n = int(input('ingrese un numero: '))
        for x in range (n, n*2):
            print(x)
            
    # la suma total de la cantidad de numeros ingresada.

    def suma (self):
        c=int(input("ingrese la cantidad de numeros: "))
        total = 0
        for variable in range (c):
            numero = int(input("ingrese el numero que desee sumar: "))
            total = total + numero 
        print ("total de la suma es: ", total )
    
    #reconocer las vocales de una frase.

    def frase (self):
        frase= input("ingrese una frase: ")
        cantidad = 0
        for x in frase:
            if x in 'a,e,i,o,u':
                cantidad += 1
        print("numero de vocales en la frase es: ", cantidad)
    
    #Escribir un programa que muestre la sumatoria de todoslos numeros entre el o y el 100

    def sumatoria (self):
        total = 0
        for i in range(101):
            if i%3==0:
                total +=i
        print ('la suma total del rango es: ', total)

    # Dado un numero entero positivo, mostrar su factrorial, el factorial de un numero se obtiene muyltiplicando todo los numeros enteros positivos que hay entre el  y ese numero
    # el factorial de 0 es 1

    def factorial (self):
        num= int(input('ingrese un numero: '))
        f=1 
        if num != 0:
            for i in range(1,num+1):
                f=f*i
        print(' el factorial calculado es : ',f)
   
    #Crear un algoritmo que muestre los primeros 10 numeros de la sucesion de fibonacci. La sucesion comienza con los 
    #numeros o y 1 y , a partir de estos cada elemento es la suma de los numeros anteriores en la secuencia: 
  
    def fibonacci (self):  
        n1 = 0
        n2 = 1
        print(n1)
        print(n2)
        for i in range (8):
            n3= n1+n2
            print(n3)
            n1=n2
            n2=n3
    
    # Escribir un programa que permita al usuario ingresar 6 numeros entero,
    #que puedan ser positivos o negativos. Al finalizar, mostrar la sumatoria de los 
    #numeros negativos y el promedio de los positivos.
    
    def operar (self):
        suma_negativa = 0
        suma_positiva = 0
        cantidad_positivos = 0 
        for i in range (6):
            num = int(input('ingrese un numero: '))
            if num >=0:
                cantidad_positivos+=1
                suma_positiva+=num
            else:
                suma_negativa+=num
        print('sumatoria de negativos: ', suma_negativa)
        if cantidad_positivos !=0:
            print('promedio de positivos: ', suma_positiva/cantidad_positivos)
        else:
            print('no se ingresaron numeros positivos: ')

    #Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno,
    #donde un integrante de cada equipo es el "jefe" y los otros 5 son sus"oficiales".La regla más importante del juego es que sólo se comunicarán mediante un canal común.
    # por lo que deben buscar la forma de ocultar el contenido de sus mensajes Uno de los equipos decide utilizar un método antiguo de encriplación llamado 
    #"la cifra del césar que consiste en correr cada letra del mensaje-considerando la posición de cada una en el alfabeto-una determinada cantidad de lugares. Ejemplo: si ei cornmiento es de 2 lugares, la palabra"ATAQUE" se transforma en "CVOS'
        
    def incripta (self):
        corrimiento = int(input("Corrimiento: "))
        alfabeto = "abcdefghijklmnñopqrstuvwxyz"

        for i in range(5):
            mensaje= input("Mensaje a encriptar: ") 
            encriptado=""
            for caracter in mensaje:
                if caracter.lower() in alfabeto:
                    indice=alfabeto.find(caracter.lower())
                    indice= (indice+corrimiento) % 27
                    encriptado+=alfabeto[indice]
                else:
                    encriptado+=caracter        
            print("***Mensaje encriptado: ", encriptado)

    # EJERCICIOS CON WHILE:
     
    #Ver cantidad de numeros positivos.

    def positivo (self):
        positivos = 0
        n = int(input('numero (0 para terminar la ejcucion): '))
        while n!=0:
            if n>0:
                positivos+=1
            n= int(input('numero (0 para terminar la ejcucion): '))
        print("cantidad de positivos:", positivos)  

    # calcular el mayor de los numeros positivo s ingresados.
    def mayor (self):
        mayor = -1
        n = int(input("numero"))
        while n>=0:
            if n>mayor:
                mayor = n
            n = int(input('numero positivo: '))
        print('mayor numero ingresado es: ', mayor)

   # Descomponer la suma de una cantidad ingresada.
   
    def sumar (self):
        suma = 0
        n = int(input('numero positivos: '))
        while n!=0:
            digito = n%10
            suma += digito 
            n = n // 10
        print('suma de los digitos: ', suma )
    
    # Realizar un algoritmo donde pueda contar los numeros pares ingresados.

    def par (self):
        pares =0
        n=int(input("Número (-1	para terminar el programa): ")) 
        while n!=-1:
            if n%2 ==0:
                pares+=1
            suma = 0
            while n!= 0:
                digito=n%10
                suma+=digito
                n=n//10
            print("Suma	de sus	digitos:",suma)
            n=int(input("Número (-1	para terminar el programa): ")) 
        print("Se ingresaron", pares,"números pares")
    
    #Crear un programa que permita al usuario procesar los montos de las compras 
    #de un cliente ( se desconoce la cantidad de datos que se cargara), contando el ingreso de datos
    #cuando el usuario ingrese el monto 0.
    #Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese nuevo monto.
    
    def monto (self):
        total = 0
        monto = float(input("monto de un venta: $"))
        while monto !=0:
            if monto <=0:
                print("monto no valido")
            else:
                total += monto 
                monto = float(input("monto de una venta: $"))
        if total>1000:
            total = total -(total*0.1)
        print("monto total a pagar: $", total)
     #Crear un programa que solicite el ingreso de numeros enteros 
     #positivos,hasta que el usuario ingrese el 0. por cada numero informar 
     #cuantos digitos pares y impares tiene.

    def par_impar (self):
        total_pares=0
        total_impares=0
        numero= int(input("ingrese un numero: "))
        while numero!=0:
            pares = 0
            impares = 0
            while numero !=0:
                ultimoDigito=numero % 10
                if ultimoDigito % 2==0:
                    pares+=1
                    total_pares+=1
                else:
                    impares+=1
                    total_impares+=1
                numero =numero//10
            print("el numero ingresado tiene", pares,"digitos pares y ", impares, "gigitos impares")
            numero= int(input("ingrese un numero: "))
        print("total de digitos pares: ", total_pares)
        print("total de digitos impares: ", total_impares)
    
    #Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string“*" (asterisco).
    #Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra ("/") se considera que termina una línea.
    #Por cada línea completa, informar cuántos dígitos numéricos (del O al 9) aparecieron en total (en todos los titulos de libros que componen esa linea).
    # Finalmente, informar cuántas lineas completas se ingresaron.

    def libros (self):
        digitosEnLaLinea=0
        cantLineas=0
        titulo=input("Titulo del libro: ")
        while titulo!="*":
            if titulo == "/":
                cantLineas+=1
                print("Línea completa.Aparecen",digitosEnLaLinea,"dígitos")
                digitosEnLaLinea=0
            else:
                for	caracter in titulo:
                    if caracter in "0123456789":
                        digitosEnLaLinea+=1
            titulo=input("Titulo del libro: ")
        print("Fin. Se leyeron", cantLineas,"lineas")


    ##Escribir un programa que, dado un numero entero, muestre su valor absoluto
    def absoluto(self):
        entero = int(input("Ingresar un numero entero: "))
        if entero > 0:
            valor = entero
            print("El valor absoluto de {}".format(entero), "es : {} ".format(valor))
        elif entero == 0:
            cero = entero
            print("El valor es absoluto de  {} ".format(entero), "es :{}".format(cero))
        else:
            menos = entero * -1
            print("El valor absoluto de {} " .format(entero), "es: {} " .format(menos))

    #Solicitar al usuario los nombres de dos personas los cuales se almacenaran en dos variables
    #A continucacion imprimir "coincidencia" se los nombres de ambas personas comienzan con la misma letra o si terminan
    #con la misma letra. Si no es asi, imprimir "no hay coincidencia".

    def coincidencia(self):
        nombre1 = input("Ingresar un nombre: ")
        nombre2 = input("Ingresar un segundo nombre: ")  
        if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
            print("coincidencia")
        else:
            print("no hay coincidencia")
    
    #Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:candidato A por el partido rojo
    #candidato B por el partido verde, candidato C por el partido azul. 
    def candidatos(self):
        usuario = input("Ingresar una letra A,B O C: ")
        if usuario == "A":
            print("{} usted a votado por el partido rojo".format(usuario))
        elif usuario == "B":
            print("{} usted a votado por el partido verde".format(usuario))
        elif usuario == "C":
            print("{} usted a votado por el partido azul ".format(usuario))
        else:
            print("Opcion erroneo")
    
    #Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "es vocal".
    #Se debe validar que el usuario ingrese solo un caracter.Si ingresa un string de mas de un caracter, informarle que no
    #se puede proceder al dato
    def caracter(self):
        letra = input("Ingresar una letra:")
        vocales = "aeiou"
        if len(letra) != 1:
            print("No se puede proceder el dato")
        elif letra in vocales:
            print("Es una vocal")

    #Hacer un programa que permita si un año es bisiesto. 
    #Para que un año sea bisiesto debe ser divisible por 4 y no dibe ser divisible por 100
    #excepto que tambien sea divisible por 400. 
    def año(self):
        bisiesto = int(input("Ingrese un año: "))
        if ((bisiesto % 4 == 0) and (bisiesto%100 != 0) or (bisiesto % 400 == 0)):
            print("El año es bisiesto: {} ".format(bisiesto))
        else:
            print("No es un año bisiesto: {} ".format(bisiesto))
    
    # Escribir un programa que especifique el ingresoo de una cantidad indeterminada de numeros
    # mayores que 1, finalizando cuando reciba un cero.
    # Imprimir la cantidad total de numeros primos ingresados.
    def primos(self):
        a = 0
        numero = int (input("Ingrese un numero:"))
        while numero!=0:
            primo = True
            for i in range (2, numero):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                a = a + 1
                numero = int(input("Ingresar otro numero:"))
        print("cantidad total de numeros primos es ", a)

    #Escribir un programa que permita al usuario ingresar dos años y luego
    #imprimir todos los años en ese rango que sean bisiesto y multiplos de 10
    def bisiesto(self):
        añoinicial = int(input("Ingresar un año:"))
        añofinal = int(input("Ingresar un año final:"))
        for año in range (añoinicial, añofinal+1):
            if año %10 == 0:
                if ((año % 4 == 0) and (año %100 != 0) or (año%400 == 0)):
                        print(año)


    #Determine cual es la salida en patanlla si ingresa los valores x = 6, y =7
    #¿que sucede si los nombres de los parametros dentro de la funcion se
    #cambia, y ahora se utilizan los nombres a,b en lugar de los nombres x,y?
    def salida(self):
        def coordenadaZ(a,b):
            a = a + 10
            b = b + 15
            return a + b 
     #!Programa principal
        x = int(input("Coordenada eje x: "))
        y = int(input("Coordenada eje y: "))
        for i in range (3):
            z = coordenadaZ(x,y)
            x = x + 1 
            y = y + 1
        print (x,"   .    ",y)
    #! Respuesta: Cambiar el nombre de los parametros no afecta en nada en el problema, ya que el valor que va retornar
    #! no se esta usando en el programa principal.

    #El siguiente programa deberia imprimir el numero 2 si se le ingresan como valores
    # x=5 , y=1 pero en su lugar imprime 5¿que hay que corregir?
    def numero(self):
        def maximo (a,b):
            if a>b:
                return a
            else:
                return b
        def minimo(a,b):
            if a<b:
                return a
            else:
                return b
        #!Programa principal
        x = int(input("Un numero:   "))
        y = int(input("Otro numero:    "))
        print(maximo(x-3, minimo(x+2,y-5)))
    #! Respuesta: Lo que se deberia es respetar los argumento, porque el codigo que estaba en el video esta mal no esta cumpliendo con 
    #! el parametro que especifica cada funcion.

    #Escribir una funcion que, dado un numero de DNI, retorne true si el numero es valido y 
    #false si no lo es.
    #Para que un numero de DNI sea valido debe tener entre 7 y 8 digitos.
    def funcion(self):
        dni = int(input("Ingrese un numero:"))
        c = 0
        while dni != 0:
            c = c + 1
            dni = dni // 10  
            if c == 7 or c == 8:
                print("El numero es valido:")
            else:
                print("El numero no es valido:")
    
    #Escribir una funcion que, dado un string, retorne la longitud de la ultima palabra. Se considera
    #que la palabra estan separadas por uno o mas espacios. Tambien podria haber espacios al principio o al final del string
    # pasado por parametros.
    def palabra(self):
        frase = input("Inngresar una frase:")
        longitud = len(frase) 
        if longitud == 0:
            return 0
        e = 0
        for i in range(longitud):
            if frase[i] != " ":
                e = e + 1
            else:
                if frase [i] == " " and i <(longitud-1) and frase[i+1]!= " ":
                    e = 0
        print("La longitud de la palabra es:{}".format(e))
    
    #Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club 
    #Para eso ingresara nombre completo mediante el ingreso de un nombre vacio.
    
    def nombre(self):
        def DNI(dni):
            c = 0
            while dni != 0:
                c = c + 1
                dni = dni // 10  
            return c == 7 or c == 8
        def lenUltimaPalabra(cadena):
            longitud = len(cadena) 
            if longitud == 0:
                return 0
            e = 0
            for i in range(longitud):
                if cadena[i] != " ":
                    e = e + 1
                else:
                    if cadena [i] == " " and i <(longitud-1) and cadena[i+1]!= " ":
                        e = 0
            return e
        def primerosTresDigitos(numero):
            while numero >= 1000:
                numero = numero  / 10
            return int (numero)

        def obteneridentificador(nombre,dni):
            nombre = nombre.strip()
            i = nombre[0:nombre.find(" ")]
            i = i +str(lenUltimaPalabra(nombre))
            i = i +str(primerosTresDigitos(dni))
            return i 

        nombre= input("Ingresar un nombre para el socio: ")
        while nombre !="":
            dni = int(input("Ingresar el dni del socio:"))
            while not  (DNI(dni)):
                print("El numero es invalido") 
                dni = int(input("dni del socio: "))
            registro = obteneridentificador(nombre,dni)
            print("El identificador del socio es: ", registro)
            nombre = input("nombre del socio")

    def listaYtuplas(self):
    
        num=[]
        nro=int (input ("Número: "))
        while nro!=0:
            num.append (nro)
            nro=int (input ("Número: "))

        eliminar=int (input ("Número a eliminar: "))
        if eliminar in num:
            num.remove (eliminar)
        else:
            print ("Ese número no esta entre los ingresados")   
        def sum (lista):
            suma = 0
            for n in lista:
                suma+=n
            return suma    
        print ("Sumatoria de los números:", sum (num))
        def num_Menores (lista,limite):
    
            nueva=[]
            for n in lista:
                if n<limite:
                    nueva.append (n)
            return nueva 
        limite=int (input ("Filtrar números menores a: "))
        for n in num_Menores (num, limite):
            print (n)   
        def freq(lista):
            nueva=[]
            for n in lista:
                if(n,lista.count(n)) not in nueva:
                    nueva.append((n, lista.count(n)))
            return nueva        
        print ("Frecuencias:")
        for tupla in freq (num):
            print (tupla[0], "aparece", tupla[1], "veces")
    
    def Alumnos(self):
        def Nombres(Alumnos):
            nombre=input("nombre: ")
            while nombre!="x":
                Alumnos.add(nombre)
                nombre=input("nombre: ")
            return Alumnos    
        primaria=set ()
        secundaria=set ()
        print ("alumnos de primaria")
        primaria= Nombres(primaria)
        print ("alumnos de secundaria")
        secundaria= Nombres(secundaria)

        print("nombres de todos los alumnos:")
        for nombre in primaria|secundaria:
            print (nombre)
        print("nombres comunes:")
        for nombre in primaria&secundaria:
            print(nombre)    
        print("nombre de primaria que no se repiten en secundaria:")
        for nombre in primaria-secundaria:
            print (nombre)

    def direcciones(self):
        venta=[("Nuria Costa",5,12780.78,"Calle las Flores 355"),("Jorge Russo",7,699,"Mirasol 218"),("Nuria Costa",7,532.90,"Calle las Flores 355"),("Julian Rodriguez",12,5715.99,"La Mancha 761"),("Jorge Russo",15,958,"Mirasol 218")]
        domicilios=set()
        for i in venta:
            domicilios.add(venta[3])
        print(domicilios)

    def diccionarios13(self):
        contadores={}
        for i in range(3):
            cadena=input("cadena de caracteres: ")
            for caracter in cadena:
                if caracter not in contadores.keys():
                        contadores[caracter]=1
                else:
                        contadores[caracter]+=1
        for caracter,cantidad in contadores.items():
            print (caracter,":",cantidad)  


    #11.1 Ejercicios resueltos de listas y tuplas  
    def listaYtuplas(self):
    
        num=[]
        nro=int (input ("Número: "))
        while nro!=0:
            num.append (nro)
            nro=int (input ("Número: "))

        eliminar=int (input ("Número a eliminar: "))
        if eliminar in num:
            num.remove (eliminar)
        else:
            print ("Ese número no esta entre los ingresados")   
        def sum (lista):
            suma = 0
            for n in lista:
                suma+=n
            return suma    
        print ("Sumatoria de los números:", sum (num))

        def num_Menores (lista,limite):
    
            nueva=[]
            for n in lista:
                if n<limite:
                    nueva.append (n)
            return nueva 
        limite=int (input ("Filtrar números menores a: "))
        for n in num_Menores (num, limite):
            print (n)   
        def freq(lista):
            nueva=[]
            for n in lista:
                if(n,lista.count(n)) not in nueva:
                    nueva.append((n, lista.count(n)))
            return nueva        
        print ("Frecuencias:")
        for tupla in freq (num):
            print (tupla[0], "aparece", tupla[1], "veces")
    
    #12.1 Ejercicios resueltos de conjuntos

    def Alumnos(self):
        def Nombres(Alumnos):
            nombre=input("nombre: ")
            while nombre!="x":
                Alumnos.add(nombre)
                nombre=input("nombre: ")
            return Alumnos    
        primaria=set ()
        secundaria=set ()
        print ("alumnos de primaria")
        primaria= Nombres(primaria)
        print ("alumnos de secundaria")
        secundaria= Nombres(secundaria)

        print("nombres de todos los alumnos:")
        for nombre in primaria|secundaria:                         
            print (nombre)
        print("nombres comunes:")
        for nombre in primaria&secundaria:
            print(nombre)    
        print("nombre de primaria que no se repiten en secundaria:")
        for nombre in primaria-secundaria:
            print (nombre)

    def direcciones(self):
        venta=[("Nuria Costa",5,12780.78,"Calle las Flores 355"),("Jorge Russo",7,699,"Mirasol 218"),("Nuria Costa",7,532.90,"Calle las Flores 355"),("Julian Rodriguez",12,5715.99,"La Mancha 761"),("Jorge Russo",15,958,"Mirasol 218")]
        domicilios=set()
        for venta in venta:
            domicilios.add(venta[3])
        print(domicilios)

    #13.1 Ejercicios resueltos con diccionarios 
    def diccionarios13(self):
        contadores={}
        for i in range(3):
            cadena=input("cadena de caracteres: ")
            for caracter in cadena:
                if caracter not in contadores.keys():
                        contadores[caracter]=1
                else:
                        contadores[caracter]+=1
        for caracter,cantidad in contadores.items():
            print (caracter,":",cantidad)  
    

    #11.2

    def eje1(self):   
        """Video 11.2 Ejercicios de listas con tuplas"""  
        pasajeros=[]
        ciudades=[]

        while True:
            print("1. Agregar pasajeros")
            print("2. Agregar ciudades")
            print("3. Buscar ciudad de destino mediante el C.I.")
            print("4. Cantidad de pasajeros que viajan a una ciudad")
            print("5. Salir del programa")
            opcion = int(input("Accion a ejecutar: "))
            if opcion==1:
                print("AGREGAR PASAJEROS")
                def agregarpasajeros(pasajeros):
                    nombre=input("nombre = x para terminar: ")
                    while nombre!="x":
                        ci=int(input("C.I: "))
                        destino=input("ciudad de destino: ")
                        pasajeros.append((nombre, ci, destino))
                        nombre=input("nombre =x para terminar: ")
                    return pasajeros
                pasajeros=agregarpasajeros(pasajeros)
            elif opcion==2:
                print("AGREGAR CIUDADES")
                def agregarciudades(ciudades):
                    ciudad=input("ciudad =x para terminar: ")
                    while ciudad!="x":
                        pais=input("pais: ")
                        ciudades.append((ciudad, pais))
                        ciudad=input("ciudad =x para terminar: ")
                    return ciudades
                ciudades=agregarciudades(ciudades)
            elif opcion==3:
                ci= int(input("C.I: "))
                def buscarciudad(pasajeros, ci):
                    for viaje in pasajeros:
                        if viaje [1]==ci:
                            return viaje[2]
                        return ""
                print("el pasajero viaja a",buscarciudad(pasajeros, ci))
            elif opcion==4:
                ciudad=input("ciudad: ")
                def cantidadpasajerosciudad(pasajeros, ciudad):
                    cantidad=0
                    for viaje in pasajeros:
                        if viaje[2]==ciudad:
                            cantidad+=1
                    return cantidad
                print("viajan",cantidadpasajerosciudad(pasajeros, ciudad),"pasajeros")
            elif opcion==7:
                break
            else:
                print("opcion invalida")
    #13.2
    def eje2(salf):
        
        """Crea un programa para gestionar datos de los socios de un club, permitiendo:

        *Cargar informacion de los socios en un diccionario para acceder por numero de socio.
        los datos a almacenar son: Numero, Nombre y apellido, fecha de ingreso(ddmmaaaa), cuota
        al dia(s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
        socio nº1= Amanda Núñez,ingreso:17/03/2009, cuota al dia.
        socio nº2= Bárbara Molina,ingreso:17/03/2009, cuota al dia.
        socio nº3= Laurato Campos,ingreso:17/03/2009, cuota al dia.

        *informar cantidad de socios del club.

        *solicitar al usuario el numero de socio y registrar que ha pagados las cuotas adecuadas.

        *modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar
        que en realidad ingresaron el 14/03/2018.

        *soliciar el nombre y apellido de un socio y darle de baja (eliminarlo del listado).

        *Imprimir el listado de socios completo."""



        socios_activos = {1:["Amanda Nuñez","17032009",True], 2:["Barbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

        print("***Cargar socios***")
        def cargarsocios(socios):
            numero=int(input("Numero de socio(0 para cerrar): "))
            while numero!=0:
                nombre=input("Nombre y Apellido: ")
                fecha=input("Fecha de ingreso(fecha completa sin separacion ): ")
                cuota=input("¿cuota al dia? (s para si, n para no) s/n: ")
                pago=cuota.lower()=="s"
                socios[numero]=[nombre,fecha,pago]
                numero=int(input("Numero de socio(0 para cerrar): "))
            return socios
        socios_activos=cargarsocios(socios_activos)

        print("El club tiene",len(socios_activos),"socios")

        print("***Registrar pago de cuotas***")
        numero=int(input("Numero de socios: "))
        socios_activos[numero][2]=True

        print("***Modificando fecha de ingreso...")
        def modificarfecha(socios, fecha_anterior, fecha_nueva):
            for datos in socios.values():
                if datos[1]==fecha_anterior:
                    datos[1]=fecha_nueva
            return socios
        socios_activos=modificarfecha(socios_activos, "13032018", "14032018")

        print("***Eliminar socio:")
        nombre=input("Nombre y Apellido: ")
        def numerosocio(socios,nombre):
            for numero,datos in socios.items():
                if datos[0].lower()==nombre.lower():
                    return numero
            return 0
        numero=numerosocio(socios_activos,nombre)
        del socios_activos[numero]

        def formatofecha(fecha):
            return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirlistado(socios):
            for numero,datos in socios.items():
                print("-Numero: ", numero)
                print("-Nombre: ", datos[0])
                print("-Fecha de ingreso: ",formatofecha(datos[1]))
                if datos[2]:
                    print("-Cuota al dia")
                else:
                    print("-En deuda")
                print("-------------")
            return None    
        imprimirlistado(socios_activos)

res=operaciones()