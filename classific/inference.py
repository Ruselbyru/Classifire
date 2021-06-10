import json
import numpy
from keras.models import load_model
from keras.preprocessing import image

def runInference(imageURL):
    #open labels json
    with open('./static/model/imagenet_classes.json') as file:
        labelinfo = file.read()
    #preobrazovanie json (dict)
    labelinfo = json.loads(labelinfo)
    #load model
    model = load_model('./static/model/MobileNetModelImagenet.h5')
    #work with pages
    img_height, img_width = 224, 224
    test_image = '.' + imageURL
    img = image.load_img(test_image, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x / 225
    x = x.reshape(1, img_height, img_width, 3)
    predi = model.predict(x)
    num = str(numpy.argmax(predi[0]))
    prediction = labelinfo [num][1]
    return prediction