import RPi.GPIO as GPIO

class ControladorApertura(object):
	__instancia = None

	def __new__(cls):
		if ControladorApertura.__instancia is None
			ControladorApertura.__instancia = object.__new__(cls)
		return ControladorApertura.__instancia

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(11,GPIO.OUT)
		#se crea el objeto en el pin 11 con 50 Hz
		self.pwm = GPIO.pwm(11,50)
		self.ciclo_trabajo()
		self.señal()

	def ciclo_trabajo(self):
		#prueba : 1.8 milisegundos --> 0.0018 seg
		self.anchoPulso = 0.0018
		self.ciclo = self.anchoPulso * 50 * 100 # %

	def señal(self):
		pwm.start(self.ciclo)