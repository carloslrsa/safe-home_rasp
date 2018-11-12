import RPi.GPIO as GPIO

class Cerradura(object):

	def __new__(cls):

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        #se crea el objeto en el pin 11 con 50 Hz
        self.pwm = GPIO.PWM(11,50)
        self.Abrir()
        self.senal()

    def Abrir(self):
        #prueba : 1.4 milisegundos --> 0.0018 seg
        self.anchoPulso = 0.0014
        self.ciclo = self.anchoPulso * 50 * 100 # %

    def senal(self):
        self.pwm.start(self.ciclo)
        self.senal()

	def Abrir(self):