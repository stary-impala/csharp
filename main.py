import socket
import RPi.GPIO as g
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('192.168.1.104', 8005))
g.setmode(g.BCM)
g.setup(9,g.OUT) #Левый поворот
g.setup(11,g.OUT) #Правый поворот
g.setup(13,g.OUT) #Задний фонарь
g.setup(17,g.OUT) #Правое колесо
g.setup(19,g.OUT)# Передний фонарь
g.setup(26,g.OUT) #Левое колесо

print('Сервер запущен. Ожидание подключений...')

while True:
    data, addres = sock.recvfrom(1024)
    print(data.decode('utf-8'))
    if data.decode('utf-8') == "Go":
        g.output(26, True)
        g.output(17, True)
        g.output(19, True)
        g.output(13,False)
    elif data.decode('utf-8') == "Left":
        g.output(17, True)
        g.output(9, True)
        g.output(13, False)
    elif data.decode('utf-8') == "Right":
        g.output(26, True)
        g.output(11, True)
        g.output(13, False)
    elif data.decode('utf-8') == "Stop":
        g.output(17, False)
        g.output(9, False)
        g.output(13, True)
        g.output(26, False)
        g.output(11, False)
    sock.sendto(("").encode('utf-8'), addres)
