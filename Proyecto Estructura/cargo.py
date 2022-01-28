class Cargo:

    secuencia = 2
    cargos = [{"Código":1,"Cargo":"Analista"},{"Código":2,"Cargo":"Jefe"}]

    def __init__(self,descrip):
        Cargo.secuencia += 1
        self.código = Cargo.secuencia
        self.descripción = descrip
        
    def registro1(self):
        return {"Código":self.código,"Cargo":self.descripción}










