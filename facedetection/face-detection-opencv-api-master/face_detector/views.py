from django.shortcuts import render

### Initializing the imports
import numpy as np
import urllib
import json
import cv2
import os
import cv2
from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse
# define the path to the face detector which would be an xml file that comes installed with haarcascades
# find it here -> https://github.com/opencv/opencv/tree/master/data/haarcascades
# download and save it in your project repository
# define the face detector now

face_detector = "haarcascade_frontalface_default.xml"

# start off with defining a function to detect the URL requested which has the image for facial recognition
@csrf_exempt

def requested_url(request):
    #default value set to be false

    default = {"safely executed": False} #because no detection yet

    ## between GET or POST, we go with Post request and check for https

    if request.method == "POST":
        if request.FILES.get("image", None) is not None:

            image_to_read = read_image(stream = request.FILES["image"])


        else: # URL is provided by the user
            url_provided = request.POST.get("url", None)


            if url_provided is None:
                default["error_value"] = "There is no URL Provided"

                return JsonResponse(default)

            image_to_read = read_image(url = url_provided)


        image_to_read = cv2.cvtColor(image_to_read, cv2.COLOR_BGR2GRAY)

        detector_value = cv2.CascadeClassifier(face_detector)
            #passing the face detector path
            # make sure to pass the complete path to the .xml file


        values = detector_value.detectMultiScale(image_to_read,
                                                 scaleFactor=1.1,
                                                 minNeighbors = 5,
                                                 minSize=(30,30),
                                                 flags = cv2.CASCADE_SCALE_IMAGE)

        ###dimensions for boxes that will pop up around the face
        values=[(int(a), int(b), int(a+c), int(b+d)) for (a,b,c,d) in values]

        default.update({"#of_faces": len(values),
                        "faces":values,
                        "safely_executed": True })

    return JsonResponse(default)

def read_image(path=None, stream=None, url=None):

    ##### primarily URL but if the path is None
    ## load the image from your local repository

    if path is not None:
        image = cv2.imread(path)

    else:
        if url is not None:

            response = urllib.request.urlopen(url)

            data_temp = response.read()

        elif stream is not None:
            #implying image is now streaming
            data_temp = stream.read()

        image = np.asarray(bytearray(data_temp), dtype="uint8")

        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image











