#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import time
import zmq
import json
from main import unpack, pack
from random import randrange
from datetime import datetime

def recebe_valores():
  while True:
    socket.setsockopt_string(zmq.SUBSCRIBE, str(sala))
    response = socket.recv_string()

    json_resposta = unpack(response.split(' ', 1)[1])
    print(json_resposta["temperatura"])
    
    if len(array_recebidos) > 10:
      array_recebidos.pop(9)
      array_recebidos.append(json_resposta["temperatura"])
    else:
      array_recebidos.append(json_resposta["temperatura"])

    somatoria = 0
    for i in range(len(array_recebidos)): 
      somatoria += int(array_recebidos[i])

    media = (somatoria/len(array_recebidos))

    print("media = " + str(media))
    publica_medias(media)

def publica_medias(media):
  #logica para publicar no topico medias
  hora = datetime.now()
  tupla = pack({'sala': sala, 'hora': str(hora), 'media': media})
  socket_pub.send_string("{topico} {tupla}".format(topico = 'medias', tupla = tupla))
  time.sleep(1)


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

context_pub = zmq.Context()
socket_pub = context_pub.socket(zmq.PUB)
socket_pub.connect("tcp://localhost:5556")

sala = int(input("Qual a sala para fazer a média?: \n"))

array_recebidos = []
recebe_valores()
