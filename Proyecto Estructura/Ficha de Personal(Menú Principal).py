from cargo import Cargo
from submenu import SubMenu
from departam import Departamento
from empleado import Empleado
from Validacion import Validar
import os


sub = SubMenu()
lista = ["1).Cargo ","2).Departamento","3).Empleados","4).Salir"]
alternativa = ""  
while alternativa != "4":
    os.system("cls")
    alternativa = sub.menuprincipal(lista,"Menú Ficha Personal") 
    if alternativa == "1":
        alternativa1 = ""
        while alternativa1 != "3":
            os.system("cls")
            alternativa1 = sub.menu(["1) Ingreso","2) Consulta","3) Salir"],"MANTENIMIENTO DE CARGOS")
            os.system("cls")
            if alternativa1 == "1":
                print("*"*15,"INGRESO DE CARGOS","*"*15)
                while True:
                    nombrec = input("Ingresar nombre de Cargo: ")
                    os.system("cls")
                    if len(nombrec) > 1 and len(nombrec) <= 20:
                        print("-"*2,"Cargo Válido","-"*2)
                        break
                    else:
                        print("-"*2,"Cargo no Existente","-"*2)
                        
                car = Cargo(nombrec)
                nombrec = car.registro1()
                Cargo.cargos.append(nombrec)
                
                input("Presione una tecla para continuar...")

            elif alternativa1 == "2":
                print("*"*20,"LISTADO DE CARGOS","*"*20)
                print(" "*3,"Código"," "*8,"Cargo")
                for car in Cargo.cargos:
                    cod = car["Código"]
                    ca = car["Cargo"]
                    print(" "*5,cod," "*10,ca)
                print("*"*59)
                input("Presione una tecla para continuar...")
            elif alternativa1 == "3":
                print("Salir de menú")

    if alternativa == "2":
        alternativa1 = ""
        while alternativa1 != "3":
            os.system("cls")
            alternativa1 = sub.menu(["1).Ingreso", "2).Consulta", "3).Salir"],"MANTENIMIENTO DE DEPARTAMENTOS")
            os.system("cls")
            if alternativa1 == "1":
                print("*"*15,"INGRESO DE DEPARTAMENTOS","*"*15)
                while True:
                    nombred = input("Ingresar nombre de Departamento: ")
                    os.system("cls")
                    if len(nombred) >= 5 and len(nombred) <= 20:
                        print("-"*2,"Departamento Válido","-"*2)
                        break
                    else: 
                        print("-"*2,"Departamento no Existente","-"*2)
                dep = Departamento(nombred)
                nombred = dep.registro2()
                Departamento.departamentos.append(nombred)
                
                input("Presiona una tecla para continuar...")                
                
            elif alternativa1 == "2":
                print("*"*15,"LISTADO DE DEPARTAMENTOS","*"*15)
                print(" "*3,"Código"," "*8,"Descripción")
                for dep in Departamento.departamentos:
                    cod = dep["Código"]
                    des = dep["Descripción"]
                    print(" "*5,cod," "*11,des)
                print("*"*57)
                input("Presione una tecla para continuar...")

    if alternativa == "3":
        alternativa1 = ""
        while alternativa1 != "3":
            os.system("cls")
            alternativa1 = sub.menu(["1) Ingreso", "2) Consulta", "3) Salir"], "MANTENIMIENTO DE EMPLEADOS")
            os.system("cls")
            if alternativa1 == "1":
                os.system("cls")
                print("*"*20,"INGRESO DE EMPLEADOS","*"*20)
                
                while True:
                    nombre = input("Ingresar nombre de Empleado: ")
                    if len(nombre) >= 3 and len(nombre) <= 20:
                        print("-"*2,"Nombre Válido","-"*2)
                        break
                    else:
                        print("-"*2,"Nombre Incorrecto","-"*2)
                   
                while True:
                    cédula = input("Ingresar número de cédula: ")
                    ced = Validar.ValidarCédula(cédula)
                    if  ced == True:
                        if len(cédula) == 10:
                            print("-"*2,"Cédula Correcta","-"*2)   
                            break
                        else:
                            print("-"*2,"Cantidad de Dígitos Incorrecta","-"*2)
                    else:
                        print("-"*2,"Volver a ingresar solo dígitos numéricos[máximo 10 dígitos]...","-"*2)
                
                while True:
                    cargo =  input("Ingrese nombre de Cargo: ")
                    ca = Validar.ValidarCargo(cargo)
                    if cargo == ca:
                        print("-"*2,"El cargo existe","-"*2)
                        break
                    else:
                        print("-"*2,"El cargo no existe, volver a ingresar...","-"*2)

                while True:
                    departamento = input("Ingrese nombre de Departamento: ")
                    dp = Validar.ValidarDepartamento(departamento)
                    if departamento == dp:
                        print("-"*2,"El departamento existe","-"*2)
                        break
                    else:
                        print("-"*2,"El departamente no existe, volver a ingresar...","-"*2) 

                while True:   
                    sueldo = input("Ingresar sueldo: ")
                    sueldo1 = Validar.ValidarSueldo(sueldo)
                    if sueldo1 == True:
                        sueldo = float(sueldo)
                        if sueldo > 0:
                            print("-"*2,"Sueldo Válido","-"*2)
                            break       
                    else:
                        print("-"*2,"Sueldo Incorrecto","-"*2)
                    
                
                metod = Empleado(nombre,cédula,cargo,departamento,sueldo)
                empleado = metod.registro3()
                Empleado.empleados.append(empleado)
                       
                input("Presione una tecla para continuar...")

            elif alternativa1 == "2":
                print("*"*38,"LISTADO DE EMPLEADOS","*"*40)
                print(" "*2,"Código"," "*6,"Nombre"," "*12,"Cédula"," "*8,"Cargo"," "*9,"Departamento", " "*7,"Sueldo")
                for metod in Empleado.empleados:
                    cod = metod["Código"]
                    nom = metod ["Nombre"]
                    ced = metod ["Cédula"]
                    car = metod["Cargo"]
                    dep = metod["Departamento"]
                    suel = metod ["Sueldo"]
                    print(" "*4,cod," "*9,nom," "*(16-len(nom)),ced," "*(15-len(ced)),car," "*(15-len(car)),dep," "*(19-len(dep)),suel)
                print("*"*100)
                input("Presione una tecla para continuar...")

            elif alternativa1 =="3":
                print("Salir de menú")

os.system("cls")
print("Gracias por visitarnos.")

