#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import time
import zmq
import json
import threading
from main import unpack
from random import randrange


context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

sala = int(input("Qual a sala para fazer a média?: \n"))

array_recebidos = []

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














  