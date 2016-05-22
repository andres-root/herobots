
from django.db import models


class Preorder(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    robot = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    robotname = models.CharField(max_length=200)
    shirt = models.BooleanField(default=False)
    satellite = models.BooleanField(default=False)
    free = models.BooleanField(default=False)
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
