from django.db import models
from django.db.models import Model, CharField, DateTimeField

# Create your models here.

class Movie(Model):

    title = CharField(max_length=100)
    director = CharField(max_length=100)
    imgurl = CharField(max_length=350)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title