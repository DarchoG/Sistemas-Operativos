import random

class Lote:

    def __init__(self, Numero, Lote):

        self.Lote = Lote
        self.ID = Numero
        self.tiempoEstimado = random.randint(5, 18)
        self.tiempoEjecutado = 0
        self.primerOperando = random.randint(1, 10000)
        self.segundoOperando = random.randint(1, 10000)
        self.Operacion = self.obtenerOperando(random.randint(1, 5))
        self.Resultado = self.realizarOperacion(self.primerOperando, self.segundoOperando, self.Operacion)    

    def obtenerOperando(self, Numero):

        if(Numero == 1):
            
            return "+"
        
        elif(Numero == 2):

            return "-"
        
        elif(Numero == 3):

            return "*"
        
        elif(Numero == 4):

            return "/"
        
        elif(Numero == 5):

            return "%"
        
    def realizarOperacion(self, primerOperando, segundoOperando, Operador):

        if(Operador == "+"):

            return primerOperando + segundoOperando

        elif(Operador == "-"):

            return primerOperando - segundoOperando    
        
        elif(Operador == "*"):

            return primerOperando * segundoOperando
        
        elif(Operador == "/"):

            return primerOperando // segundoOperando
        
        elif(Operador == "%"):

            return primerOperando % segundoOperando
        
    def obtenerLote(self):

        return self.Lote    
        
    def obtenerID(self):

        return self.ID    
        
    def obtenerTiempoEstimado(self):

        return self.tiempoEstimado

    def obtenerTiempoEjecutado(self):

        return self.tiempoEjecutado    

    def obtenerPrimerOperando(self):

        return self.primerOperando
    
    def obtenerSegundoOperando(self):

        return self.segundoOperando
    
    def obtenerOperacion(self):

        return self.Operacion
    
    def obtenerResultado(self):

        return self.Resultado
    
    def asignarID(self, Cantidad):

        self.ID = Cantidad

    def asignarResultado(self, Parametro):

        self.Resultado = Parametro        

    def asignarTiempoEjecutado(self, Cantidad):

        self.tiempoEjecutado = Cantidad

    def obtenerEjecuccion(self):

        Temporal = []

        Temporal.append(self.obtenerLote())
        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())

        return Temporal        

    def obtenerTodo(self):

        Temporal = []

        Temporal.append(self.obtenerLote())
        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())
        Temporal.append(self.obtenerResultado())

        return Temporal
