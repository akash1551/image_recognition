import os
from image_recognition.settings import BASE_DIR


def upload_image(instance, filename):
    print 'We are uploading image'
    if os.path.isdir(BASE_DIR+'/Media'):
        return os.path.join(BASE_DIR+'/Media/'+str(filename))
    else:
        os.makedirs(BASE_DIR+'/Media')
        return os.path.join(BASE_DIR+'/Media/'+str(filename))
