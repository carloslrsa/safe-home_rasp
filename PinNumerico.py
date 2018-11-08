import RPi.GPIO as GPIO

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