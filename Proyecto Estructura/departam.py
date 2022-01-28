class Departamento:

    secuencia = 0
    departamentos = []

    def __init__(self, descrip):
        Departamento.secuencia += 1
        self.código = Departamento.secuencia
        self.descripción = descrip
        

    def registro2(self):
        return {"Código":self.código,"Descripción":self.descripción}
        




    


    







