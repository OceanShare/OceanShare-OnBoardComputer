#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import threading
#import urllib.request
#from urllib.request import urlopen

#humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)

#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get reading. Try again!')
#    sys.exit(1)

def lireFichier (emplacement) :
    fichTemp = open(emplacement)
    contenu = fichTemp.read()
    fichTemp.close()
    return contenu

def recupTemp (contenuFich) :
    secondeLigne = contenuFich.split("\n")[1]
    temperatureData = secondeLigne.split(" ")[9]
    temperature = float(temperatureData[2:])
    temperature = temperature / 1000
    return temperature

#def post(temperature) :
    #threading.Timer(1800.0, post).start()
#     print (temperature)
#temperature = urllib.urlencode(temperature)
#    path='http://client.pathtophppage' # a changer
#    req= urllib.request(path, temperature)
#    req.add_header("Content-type", "application/x-www-form-urlencoded")
#    page= urlopen(req).read()

def loop_display() : 
    while True:
        contenuFich = lireFichier("/sys/bus/w1/devices/28-0416a14361ff/w1_slave")   
        temperature = recupTemp (contenuFich)
        print(temperature)
        humidity, temperatureXT = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)

        if humidity is not None and temperatureXT is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperatureXT, humidity))
        else:
            print('Failed to get reading. Try again!')
            sys.exit(1)
        time.sleep(5)

loop_display()
#post(temperature)
