import os, re, json
from django.db import models
from django.contrib.auth.models import User
from time import time
from settings import BASE_DIR

from helper_functions import upload_image


class Image(models.Model):
    image = models.FileField(upload_to=upload_image, null=True, blank=True)
