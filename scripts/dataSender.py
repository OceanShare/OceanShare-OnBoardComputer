#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import glob
import time
import threading
import socket
import urllib
import requests
import sys
import Adafruit_DHT

from socket import socket

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
    humidity, temperatureXT = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
    curLat = 43.695765
    curLong = 7.270008
    temperature = {'water_fahrenheit':temp_f, 'water_celsius':temp_c, 'air_humidity':humidity, 'air_celsius': temperatureXT, 'latitude': curLat, 'longitude': curLong}
    return temperature

def post():
    temperature = read_temp()
    data = temperature
    # TESTING #
    print(data)
    # r = requests.post('https://api.github.com/events', data)
    # r.encoding = 'ISO-8859-1'
    # print(r.url)
    # print(r.text)
    # END TESTING #
    
def post_loop():
    while True:
        post()
        time.sleep(5)
    
post_loop()
