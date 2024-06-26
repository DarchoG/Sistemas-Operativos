import random

class Proceso:

    def __init__(self, Numero, tiempoInicio, Quantum):

        self.ID = Numero

        self.tiempoEstimado = random.randint(5, 18)
        self.tiempoEjecutado = 0
        self.tiempoLlegada = 0
        self.tiempoFinalizacion = 0
        self.tiempoRetorno = 0
        self.tiempoRespuesta = None
        self.tiempoEspera = 0
        self.tiempoServicio = 0
        self.Resultado = None

        self.tiempoInicio = tiempoInicio
        self.tiempoQuantum = 0
        self.Quantum = Quantum

        self.tiempoBloqueado = 0

        self.primerOperando = random.randint(1, 10000)
        self.segundoOperando = random.randint(1, 10000)
        self.Operacion = self.obtenerOperando(random.randint(1, 5))
        self.realizarOperacion()      

    def calcularTiempoRetorno(self):

        self.tiempoRetorno = self.tiempoFinalizacion - self.tiempoLlegada

    def calcularRespuesta(self, Parametro):

        self.tiempoRespuesta = Parametro - self.tiempoLlegada 

    def calcularTiempoEspera(self):

        self.tiempoEspera = self.tiempoRetorno - self.tiempoEjecutado    

    def calcularTiempoServicio(self):

        self.tiempoServicio = self.tiempoEjecutado - self.tiempoServicio           

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
        
    def realizarOperacion(self):

        if(self.Operacion == "+"):

            self.Resultado = self.primerOperando + self.segundoOperando

        elif(self.Operacion == "-"):

            self.Resultado = self.primerOperando - self.segundoOperando    
        
        elif(self.Operacion == "*"):

            self.Resultado = self.primerOperando * self.segundoOperando
        
        elif(self.Operacion == "/"):

            self.Resultado = self.primerOperando // self.segundoOperando
        
        elif(self.Operacion == "%"):

            self.Resultado = self.primerOperando % self.segundoOperando
    
    def obtenerID(self):

        return self.ID    
        
    def obtenerTiempoEstimado(self):

        return self.tiempoEstimado

    def obtenerTiempoEjecutado(self):

        return self.tiempoEjecutado  

    def obtenerTiempoLlegada(self):

        return self.tiempoLlegada
    
    def obtenerTiempoFinalizacion(self):

        return self.tiempoFinalizacion   

    def obtenerTiempoRetorno(self):

        return self.tiempoRetorno

    def obtenerTiempoRespuesta(self):

        return self.tiempoRespuesta  

    def obtenerTiempoEspera(self):

        return self.tiempoEspera
    
    def obtenerTiempoServicio(self):

        return self.tiempoServicio   

    def obtenerPrimerOperando(self):

        return self.primerOperando
    
    def obtenerSegundoOperando(self):

        return self.segundoOperando
    
    def obtenerOperacion(self):

        return self.Operacion
    
    def obtenerResultado(self):

        return self.Resultado
    
    def obtenerTiempoBloqueado(self):

        return self.tiempoBloqueado
    
    def obtenerTiempoInicio(self):

        return self.tiempoInicio
    
    def obtenerTiempoQuantum(self):

        return self.tiempoQuantum
    
    def obtenerQuantum(self):

        return self.Quantum
    
    def asignarID(self, Parametro):

        self.ID = Parametro

    def asignarResultado(self, Parametro):

        self.Resultado = Parametro        

    def asignarTiempoEjecutado(self, Parametro):

        self.tiempoEjecutado = Parametro

    def asignarTiempoLlegada(self, Parametro):

        self.tiempoLlegada = Parametro

    def asignarTiempoFinalizacion(self, Parametro):

        self.tiempoFinalizacion = Parametro

    def asignarTiempoRetorno(self, Parametro):

        self.tiempoRetorno = Parametro

    def asignarTiempoRespuesta(self, Parametro):

        self.tiempoRespuesta = Parametro

    def asignarTiempoEspera(self, Parametro):

        self.tiempoEspera = Parametro

    def asignarTiempoServicio(self, Parametro):

        self.tiempoServicio = Parametro

    def asignarTiempoBloqueado(self, Parametro):

        self.tiempoBloqueado = Parametro

    def asignarTiempoQuantum(self, Parametro):

        self.tiempoQuantum = Parametro    

    def asignarQuantum(self, Parametro):

        self.Quantum = Parametro   

    def obtenerNuevo(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado()) 

        return Temporal
    
    def obtenerListo(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())

        return Temporal      

    def obtenerEjecuccion(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerTiempoQuantum())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())

        return Temporal      

    def obtenerBloqueado(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoBloqueado())

        return Temporal 

    def obtenerTerminados(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())
        Temporal.append(self.obtenerResultado())

        return Temporal        

    def obtenerTodo(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())
        Temporal.append(self.obtenerResultado())
        Temporal.append(self.obtenerTiempoLlegada())
        Temporal.append(self.obtenerTiempoFinalizacion())
        Temporal.append(self.obtenerTiempoRetorno())
        Temporal.append(self.obtenerTiempoRespuesta())
        Temporal.append(self.obtenerTiempoEspera())
        Temporal.append(self.obtenerTiempoServicio())

        return Temporal
    
    def obtenerBCP(self):

        Temporal = []

        Temporal.append(self.obtenerID())
        Temporal.append(self.obtenerTiempoEstimado())
        Temporal.append(self.obtenerTiempoEjecutado())
        Temporal.append(self.obtenerPrimerOperando()) 
        Temporal.append(self.obtenerOperacion())
        Temporal.append(self.obtenerSegundoOperando())
        Temporal.append(self.obtenerResultado())
        Temporal.append(self.obtenerTiempoLlegada())
        Temporal.append(self.obtenerTiempoFinalizacion())
        Temporal.append(self.obtenerTiempoRetorno())
        Temporal.append(self.obtenerTiempoRespuesta())
        Temporal.append(self.obtenerTiempoEspera())
        Temporal.append(self.obtenerTiempoServicio())

        if(self.obtenerTiempoBloqueado() == 0): # Calcular el tiempo de bloqueo restante en caso de tenerlo

            Temporal.append(None)

        else:

            Temporal.append(8 - self.obtenerTiempoBloqueado())

        tiempoRestante = self.obtenerTiempoEstimado() - self.obtenerTiempoEjecutado()

        if(tiempoRestante > 0):

           Temporal.append(tiempoRestante)

        else:
        
            Temporal.append(None)

        return Temporal 
