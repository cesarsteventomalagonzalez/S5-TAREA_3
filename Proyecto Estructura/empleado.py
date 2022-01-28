class Empleado: 
    secuencia = 1
    empleados =[{"Código":1,"Nombre":"Dan","Cédula":"0914192182","Cargo":"Analista","Departamento":"Contabilidad","Sueldo":"550.50"}]

    def __init__(self,nombre,cédula,cargo,departamento,sueldo):
        Empleado.secuencia += 1
        self.código = Empleado.secuencia
        self.nombre = nombre
        self.cédula = cédula 
        self.cargo = cargo   
        self.departamento = departamento
        self.sueldo = sueldo
    
    def registro3(self):
        return {"Código":self.código,"Nombre":self.nombre,"Cédula":self.cédula,"Cargo":self.cargo,"Departamento":self.departamento,"Sueldo":self.sueldo}