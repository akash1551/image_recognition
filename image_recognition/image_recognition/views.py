from PIL import Image
from pytesseract import image_to_string
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render_to_response, render
from models import Image as ImageToScan

def convert_image_to_string(request):
    images = ImageToScan.objects.all()
    text_list = []
    for image in images:
        print image
        print image_to_string(Image.open(image))
        image_text = image_to_string(Image.open(image))
        text_list.append({'name': str(image).split('Media/')[1], 'content': unicode(image_text)})
    return HttpResponse(json.dumps({"imageText": image_text, "status": True}), content_type="application/json")
