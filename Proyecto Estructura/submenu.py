class SubMenu:
    def __init__(self):
        pass

    def menuprincipal(self, opciones, título):
        print(título)
        for i in opciones:
            print(i)
        alt2 = input("Elija una opcion[1...{}]: ".format(len(opciones)))
        return alt2
    
    def menu(self, opciones, título):
        print("*"*15,título,"*"*15)
        for i in opciones:
            print(i)
        alt = input("Elija una opción[1...{}]: ".format(len(opciones)))
        return alt

    
    
    
   
        
                   
                   
          
                    

    

        
     


