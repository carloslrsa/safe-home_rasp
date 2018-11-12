import RPi.GPIO as GPIO
import threading

class PinNumerico(object):
    # region Singleton
    __instancia = None

    def __new__(cls):
        if PinNumerico.__instancia is None:
                PinNumerico.__instancia = object.__new__(cls)
        return PinNumerico.__instancia
        # fin region

    VALORES = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ["*",0,"#"]
    ]

    FILAS         = [18,23,24,25]
    COLUMNAS      = [4,17,22]


   
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        for j in range(len(self.COLUMNAS)):
            GPIO.setup(self.COLUMNAS[j], GPIO.OUT)
            GPIO.output(self.COLUMNAS[j], 1)
        
        for i in range(len(self.FILAS)):
            GPIO.setup(self.FILAS[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self.tiempo_pasado = 0
        self.tiempo_refresco = 2000
        self.lectura = ''
        #threading.Thread(target = self.rutina_leer).start()
    
    def Leer(self):
        return self.lectura

    def obtener_tecla(self):
        for j in range(len(self.COLUMNAS)):
            GPIO.output(self.COLUMNAS[j],0)
            for i in range(len(self.FILAS)):
                if GPIO.input(self.FILAS[i]) == 0:
                    
                    if len(self.lectura) < 4:
                        self.lectura = self.lectura + str(self.VALORES[i][j])
                    
                    self.tiempo_pasado = 0
                    
                    print 'lectura: ' + self.lectura
                    
                    while GPIO.input(self.FILAS[i]) == 0:
                        pass
            GPIO.output(self.COLUMNAS[j], 1)
        
        self.tiempo_pasado = self.tiempo_pasado + .1
        #print self.tiempo_pasado
        if self.tiempo_pasado > self.tiempo_refresco:
            self.tiempo_pasado = 0
            print 'Se limpio la lectura'
            self.lectura = ''
    
    def rutina_leer(self):
        while True:
            self.obtener_tecla()

PinNumerico().rutina_leer()