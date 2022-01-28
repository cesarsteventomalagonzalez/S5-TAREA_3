from cargo import Cargo
from departam import Departamento



class Validar:


    def ValidarCargo(cd):
        car = 0
        for i in range(0,len(Cargo.cargos)):
            cargo2 = Cargo.cargos[i]
            if cargo2["Cargo"] == cd: 
                car = cargo2["Cargo"]
                break
        return car


    def ValidarDepartamento(dep):
        dp = 0
        for i in range(0,len(Departamento.departamentos)):
            depar2 = Departamento.departamentos[i]
            if depar2["Descripción"] == dep: 
                dp = depar2["Descripción"]
                break
        return dp


    def ValidarCédula(ced):
        ced1 = ced.isdigit()
        if ced1 == True:
            return True
        else:
            return False
       
        

    def ValidarSueldo(sueldo):    
        try:
            sueldo = int(sueldo)
            return False
        except:
            try:
                sueldo = float(sueldo)
                return True
            except:
                sueldo = str(sueldo)
                return False
                

      
        
       