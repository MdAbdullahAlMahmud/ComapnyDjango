from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.TextField(max_length=100, blank=False)
    subject = models.TextField(max_length=700, blank=False)
    message = models.CharField(max_length=700, blank=False)


    def __str__(self):
        return self.name