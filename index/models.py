from django.db import models

# Create your models here.

class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about_res/', blank = False)


    def __str__(self):
        return self.title

class slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider_res/', blank = False)


    def __str__(self):
        return self.title

class  Portfolio(models.Model):
    
    tag = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='portfolio_res/', blank = False)

    def __str__(self):
        return title