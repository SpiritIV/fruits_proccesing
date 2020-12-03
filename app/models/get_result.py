from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np

fruit_model = load_model('')

def send_result(path):
    classes = ['Banana', 'Cocos', 'Mandarine', 'Orange', 'Peach', 'Pineapple','Strawberry']
    img = load_img(path, target_size=(100, 100))
    images_as_array=[]
    images_as_array.append(img_to_array(img))
    X_img = np.array(images_as_array)
    result = fruit_model.predict(X_img)
    result = result[0]
    return classes[result.argmax(axis=0)]