import os

def upload_image(instance, filename):
    print 'We are uploading image'
    if os.path.isdir(BASE_DIR+'/Media/images'):
        return os.path.join(BASE_DIR+'/Media/images/'+str(filename))
    else:
        os.makedirs(BASE_DIR+'/Media/images')
        return os.path.join(BASE_DIR+'/Media/images/'+str(filename))
