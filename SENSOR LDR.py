import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pino_a = 17
pino_b = 27
LED = 18

GPIO.setup(LED,GPIO.OUT)

def descarga():
   print("Descarga")
   GPIO.setup(pino_a,GPIO.IN)
   GPIO.setup(pino_b,GPIO.OUT)
   GPIO.output(pino_b,0)
   time.sleep(0.05)
   
def carga():
   print("Carga")
   GPIO.setup(pino_b,GPIO.IN)
   GPIO.setup(pino_a,GPIO.OUT)
   contador = 0
   GPIO.output(pino_a,1)
   while (GPIO.input(pino_b)==0):
       contador = contador + 1
       print ("....")
       
       print("Contagem Carga:", contador)
       time.sleep(3)
       return contador
