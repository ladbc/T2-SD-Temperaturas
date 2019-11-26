#Autoras
#Jessica Antunes - 619612
#Leticia Amaral da Cunha - 628190

import json
#Este metodo compacta a mensagem
def pack(data: dict):
    message_json = json.dumps(data)
    return message_json
    
# este metodo descompacta a mensagem em um dicionario
def unpack(data: str):
    message_struct = {
        'sala': "",
        'temperatura': "",
    }
    try:
        message_struct = json.loads(data)
    except Exception as erro_msg:
        print("Deu erro ao decompactar?: ", erro_msg)

    return message_struct

def unpack_media(data: str):
    message_struct = {
        'sala': "",
        'hora': "",
        'media': "",
    }
    try:
        message_struct = json.loads(data)
    except Exception as erro_msg:
        print("Deu erro ao decompactar?: ", erro_msg)

    return message_struct