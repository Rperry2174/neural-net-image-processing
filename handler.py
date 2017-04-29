
import os
import sys
import json
import ConfigParser


HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(HERE, "image_tools"))

print("loading started")
print("loading started", HERE)
import numpy as np

import scipy.special
import scipy.misc

import urllib, cStringIO
from PIL import Image
print("loading done")


# URL = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAw0lEQVRIS83WYQvEIAiA4aT+/x8uaNxBMIaXrxrH9nVrj5a6yZxzlj9eQkARwSFZ8ZugB1tR7VAMWpF/sBVcGCQvuO81ef5nhmTx82DJGhUkC7UqIuveAeIeeDwYzjAC3tsnXKUemGT3bR0yaSyYYkdAupUr6HSGnuzSGXqxFBjBwmAUC4EZzA16K1Kdt7QPT2A4Q+9Xv7VWeu/qvNj2oRdaQq21jDF8oIaR3wxzDO7OMFuRqaKxIqf307OUQseG9+vBC4Anw63ivM72AAAAAElFTkSuQmCC'


# file = cStringIO.StringIO(urllib.urlopen(URL).read())

# # print ("loading ... ", image_file_name)
# img_array = scipy.misc.imread(file, flatten=True)

# print("image array befroe reshape", img_array);


# # reshape from 28x28 to list of 784 values, invert values
# img_data  = 255.0 - img_array.reshape(784)

# # then scale data to range from 0.01 to 1.0
# img_data = (img_data / 255.0 * 1)
# img_data = img_data.tolist();

def get_param_from_url(event, param_name):
    """
    Helper function to retrieve query parameters from a Lambda call. Parameters are passed through the
    event object as a dictionary.

    :param event: the event as input in the Lambda function
    :param param_name: the name of the parameter in the query string
    :return: the parameter value
    """
    params = event['queryStringParameters']
    return params[param_name]


def process_image(URL):
    file = cStringIO.StringIO(urllib.urlopen(URL).read())
    img_array = scipy.misc.imread(file, flatten=True)

    # reshape from 28x28 to list of 784 values, invert values
    img_data  = 255.0 - img_array.reshape(784)

    # then scale data to range from 0.01 to 1.0
    img_data = (img_data / 255.0 * 1)
    img_data = img_data.tolist()
    return img_data


def process(event, context):

    # param = get_param_from_url(event, 'urlLink')
    param = event["urlLink"]

    # processedImage = process_image('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAw0lEQVRIS83WYQvEIAiA4aT+/x8uaNxBMIaXrxrH9nVrj5a6yZxzlj9eQkARwSFZ8ZugB1tR7VAMWpF/sBVcGCQvuO81ef5nhmTx82DJGhUkC7UqIuveAeIeeDwYzjAC3tsnXKUemGT3bR0yaSyYYkdAupUr6HSGnuzSGXqxFBjBwmAUC4EZzA16K1Kdt7QPT2A4Q+9Xv7VWeu/qvNj2oRdaQq21jDF8oIaR3wxzDO7OMFuRqaKxIqf307OUQseG9+vBC4Anw63ivM72AAAAAElFTkSuQmCC')
    processedImage = process_image(param)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event,
        # "event[queryStringParameters]": event['queryStringParameters'],
        "processedImage": processedImage,
        "param": param
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
