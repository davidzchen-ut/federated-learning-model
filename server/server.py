from flask import Flask
from flask_mqtt import Mqtt
import json
import numpy as np

from PIL import Image
from io import BytesIO
import base64

from imageio import imread

import pandas as pd
import pickle
import network

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
#app.config['MQTT_USERNAME'] = 'user'
#app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

pictures = {}

photo = ""


clientIds = set(["pi01"])
clientDataBlock = {}

@app.route('/')
def index():
    network.run()
    return "training model"

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):

    for client in clientIds:
        
        mqtt.subscribe('client/' + client)





def add_data_chunk(clientName, chunk):

    global clientDataBlock

    currentImage = clientDataBlock[clientName]["currentImage"]

    clientDataBlock[clientName]["imageData"][currentImage] = clientDataBlock[clientName]["imageData"][currentImage] + chunk


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    global clientDataBlock


    payload = json.loads(message.payload.decode())

    clientName = message.topic.split("/")[1]

    if clientName in clientIds:
        if payload["message"] == "sending_data":
            clientDataBlock[clientName]["numImages"] += 1
            clientDataBlock[clientName]["currentImage"] += 1
            clientDataBlock[clientName]["imageData"].append("")
            clientDataBlock[clientName]["dimensions"].append(payload["dimensions"])

        elif payload["message"] == "done":
            convert_data(clientName)
        elif payload["message"] == "chunk":
            add_data_chunk(clientName, payload["data"])

counter = 0

def convert_data(clientName):

    global counter


    currentImage = clientDataBlock[clientName]["currentImage"]

    dims = clientDataBlock[clientName]["dimensions"][currentImage]

    image_base64 = clientDataBlock[clientName]["imageData"][currentImage].encode()

    img = base64.decodebytes(image_base64)

    buf = np.frombuffer(img, dtype=np.uint8)

    buf = np.reshape(buf, dims)

    clientDataBlock[clientName]["imageData"][currentImage] = buf

    im = Image.fromarray(buf)
    path = "./pictures/img" + str(counter) + ".jpg"
    im.save(path)

    counter += 1


def initialize():
    global clientDataBlock

    for client in clientIds:
        clientDataBlock[client] = {
            "numImages" : 0,
            "currentImage": -1,
            "imageData" : [],
            "dimensions": [] 
        }



if __name__ == '__main__':
    initialize()
    app.run(host='localhost', port=5000)


