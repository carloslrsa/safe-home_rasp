import RPi.GPIO as GPIO
<<<<<<< HEAD
import threading

class PinNumerico(object):
    # region Singleton
    __instancia = None

    def __new__(cls):
    if PinNumerico.__instancia is None:
            PinNumerico.__instancia = object.__new__(cls)
    return PinNumerico.__instancia
    # fin region

    self.VALORES = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ["*",0,"#"]
    ]

    self.FILAS         = [18,23,24,25]
    self.COLUMNAS      = [4,17,22]

    self.tiempo_pasado = 0
    self.tiempo_refresco = 100
    self.lectura = ''
   
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        threading.Thread(target = self.rutina_leer).start()
    
    def Leer(self):
        return self.lectura

    def obtener_tecla(self):    
        for j in range(len(self.COLUMNAS)):
            GPIO.setup(self.COLUMNAS[j], GPIO.OUT)
            GPIO.output(self.COLUMNAS[j], GPIO.LOW)
        
        for i in range(len(self.FILAS)):
            GPIO.setup(self.FILAS[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        valorFila = -1
        for i in range(len(self.FILAS)):
            lecturaTmp = GPIO.input(self.FILAS[i])
            if lecturaTmp == 0:
                valorFila = i
                
        if valorFila <0 or valorFila >3:
            self.exit()
            return
        
        for j in range(len(self.COLUMNAS)):
                GPIO.setup(self.COLUMNAS[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        GPIO.setup(self.FILAS[valorFila], GPIO.OUT)
        GPIO.output(self.FILAS[valorFila], GPIO.HIGH)

        valorColumna = -1
        for j in range(len(self.COLUMNAS)):
            lecturaTmp = GPIO.input(self.COLUMNAS[j])
            if lecturaTmp == 1:
                valorColumna=j
                

        if valorColumna <0 or valorColumna >2:
            self.exit()
            return

        self.exit()
        return self.KEYPAD[valorFila][valorColumna]
        
    def exit(self):
        for i in range(len(self.FILAS)):
                GPIO.setup(self.FILAS[i], GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def rutina_leer(self):
        while True:
            digito = None
            while digito == None:
                digito = self.obtener_tecla()

                self.tiempo_pasado = self.tiempo_pasado + 1

                if(self.tiempo_pasado == self.tiempo_refresco):
                    self.tiempo_pasado = 0
                    self.lectura = ''

            lectura = lectura + str(digito)
            tiempo_pasado = 0

            print (lectura)

=======

class PinNumerico():
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
        ]
    
    filas = [18,23,24,25]
    columnas = [4,17,22]
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
    def input(self):
        for j in range(len(self.columnas)):
            GPIO.setup(self.columnas[i], GPIO.OUT)
            GPIO.output(self.columnas[i], GPIO.LOW)
        for i in range(len(self.filas)):
            GPIO.setup(self.filas[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)
        
        valorFila = 0
>>>>>>> 8962681d2351c301c2943dcfcade7f5c963f8b28
