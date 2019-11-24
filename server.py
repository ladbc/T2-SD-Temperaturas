#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import time
import zmq
import json
from main import pack
from random import randrange, gauss

salas = int(input("Qual a quantia de salas?: \n"))

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

temperaturas = []

for i in range(int(salas)):
    temperaturas.append(randrange(0, 40))
    print(temperaturas[i])

while True:
    for i in range(int(salas)):
      tupla = pack({'sala': i, 'temperatura': gauss(temperaturas[i], 0.8)})
      print(tupla)
      socket.send_string("{topico} {tupla}".format(topico = str(i+1), tupla = tupla))
    time.sleep(1)
