# we are making a file ml_server.py to make our servers... essentially we are using this cell as a python file
# and it will get saved to ml_server.py file

import json
import tensorflow as tf
import numpy as np
import random

from flask import Flask, request

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')

feature_model = tf.keras.models.Model(
    model.inputs,
    [layer.output for layer in model.layers]
)

_, (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_test = x_test / 255.

def get_prediction():
    index = np.random.choice(x_test.shape[0])
    image = x_test[index, :, :]
    image_arr = np.reshape(image, (1, 784))
    return feature_model.predict(image_arr), image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        preds, image = get_prediction()
        final_preds = [p.tolist() for p in preds]
#         encoding info as strings
        return json.dumps({
            'prediction': final_preds,
            'image': image.tolist()
        })
    return 'Welcome to the model server!'


if __name__ == '__main__':
    app.run()
