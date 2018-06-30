#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import urllib.request

from urllib.request import urlopen

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
        time.sleep(5)

loop_display()
#post(temperature)
