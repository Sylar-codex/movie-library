from django.conf import settings
from django.db import models
from django.conf import settings

class Movies(models.Model) :
    users = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True ,on_delete=models.CASCADE)
    movie_name= models.CharField(max_length=200)
    status = models.CharField(max_length=60)

    def __str__(self) :
        return self.movie_name
