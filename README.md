I was inspired by this tutorial: https://projects.raspberrypi.org/en/projects/get-started-pico-w/2

This micro python script runs a script that connects the Pico W to the internet. It then runs a web server on it which can be accessed if you navigate to:

http://ip address where ip address is replaced with 192.168.etcetc 

This is the IP address of my pico when connected to the internet, but you can also use the program itself to find out what your pico ip address is: 

(Copied from website)

import network
import socket
from time import sleep
import machine

ssid= name of wifi network
password = name of wifi password

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
try:
    connect()
except KeyboardInterrupt:
    machine.reset()


If you successfully access the web server, you will be greeted with Hello World !!! Congrats
