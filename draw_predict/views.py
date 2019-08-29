from django.http import HttpResponse
from pprint import pprint
from django.http import JsonResponse


from fastai.vision import *
# from fastai.vision import load_learner
# from fastai.vision import open_image


import io

import base64

from PIL import Image as PILImage


# from fastai.vision import *
from fastai.metrics import error_rate

from PIL import Image as PILImage
import cv2
import base64

from random import choice



from django.views.decorators.csrf import csrf_exempt





@csrf_exempt
def getclass(request):


    animal_classes = [
                  'ant',
                  'bear',
                  'bee',
                  'bird',
                  'butterfly',
                  'cat',
                  'cow',
                  'dog',
                  'duck',
                  'elephant',
                  'fish',
                  'frog',
                  'giraffe',
                  'horse',
                  'kangaroo',
                  'lion',
                  'monkey',
                  'mouse',
                  'octopus',
                  'pig',
                  'rabbit',
                  'sheep',
                  'snail',
                  'spider',
                  'tiger'
               ]


    response_data = {}
    response_data['class'] = choice(animal_classes)
    return JsonResponse(response_data)

@csrf_exempt
def index(request):
    json_data = json.loads(request.body)


    # print(json_data['prediction'])




    # base_path = pathlib.Path('../')
    data_path = pathlib.Path('data')

    print(data_path.ls())

    defaults.device = torch.device('cpu')

    learn = load_learner(data_path)

    # image_str = request.POST.get('image_str')
    image_str = json_data['image_str']

    def convertBase64(base64_string):
        clean_b64_image = base64_string.replace('\n', '')
        imgdata = base64.b64decode(str(base64_string))
        pil = PILImage.open(io.BytesIO(imgdata))
        #     tensor = pil2tensor(pil, np.float64)
        #     fastai_image = Image(tensor)
        pil.save('temp.jpg')
        image = open_image('temp.jpg')
        return image

    image = convertBase64(image_str)

    pred_class, pred_idx, outputs = learn.predict(image)


    print(pred_class, pred_idx, outputs)


    # prediction = request.POST.get('prediction')
    prediction = json_data['prediction']

    print(prediction)

    response_data = {}
    response_data['status'] = str(pred_class) == prediction
    response_data['category'] = str(pred_class)
    response_data['prediction'] = prediction



    # print(response_data)

    return JsonResponse(response_data)


    # return response_data;

    # return HttpResponse(f"This Image is of a {pred_class}")



  # imgdata = base64.b64decode(str(base64_string))
    # pil = PILImage.open(io.BytesIO(imgdata))
    #
    # pil.save('tmp.jpg')
    # image = open_image('tmp.jpg')
    # defaults.device = torch.device('cpu')
    #
    # learn = load_learner('./data')
    #
    # pred_class, pred_idx, outputs = learn.predict(image)
    #
    # print(pred_class)
    # validator = request.POST.get('validator')
    #
    # if validator == pred_class:
    #     return HttpResponse("Correct! It is a {}!".format(validator))
    # else:
    #     return HttpResponse("You got this wrong bucko, it looks to me like a {}".format(pred_class))