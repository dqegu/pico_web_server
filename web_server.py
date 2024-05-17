import network
import socket
from time import sleep
import machine

password = #add address of home network
ssid = #add password of home network

STATIC_IP = #replace with ip address of pi pico

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected to Wi-Fi')


    wlan.ifconfig((STATIC_IP, '255.255.255.0', '192.168.1.1', '8.8.8.8'))

    ip, _, _, _ = wlan.ifconfig()
    print(f'IP Address: {ip}')

def start_web_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((STATIC_IP, 80)) 
    s.listen(5)
    print('Web server started')

    while True:
        conn, addr = s.accept()
        print(f'Connection from {addr}')
        conn.sendall(b'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello, World!</h1></body></html>')
        conn.close()

try:
    connect()
    start_web_server()
except KeyboardInterrupt:
    machine.reset()
