#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import time
import json
import zmq
from main import unpack

print("Subindo cliente")

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

while True:
  socket.setsockopt_string(zmq.SUBSCRIBE, "medias")
  response = socket.recv_string()
  print(response)