#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import time
import json
import zmq
from main import unpack_media

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.bind("tcp://*:5556")
array_media = []

tempo = 10
while True:
  tempo = tempo-1
  socket.setsockopt_string(zmq.SUBSCRIBE, 'medias')
  response = socket.recv_string()
  json_media = unpack_media(response[7:])
  array_media.append(["sala ", json_media['sala'], "media ", json_media['media'], "hora ", json_media['hora']])
  
  if(tempo == 0):
    pergunta = input("Deseja gerar o txt? s/n: \n")
    if(pergunta == "s"):
      File_object = open(r"medias.txt","w+")
      for line in array_media:
        File_object.write(str(line))
      File_object.close()
      break;
    else:
      tempo = 10
