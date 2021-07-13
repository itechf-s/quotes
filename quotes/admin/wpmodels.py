from django.db import models

# Create your models here.
class Images(models.Model):
    imageId = models.IntegerField(unique=True)
    pageURL = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    tags = models.CharField(max_length=150)
    previewURL = models.CharField(max_length=125)
    previewWidth = models.CharField(max_length=20)
    previewHeight = models.CharField(max_length=20)
    webformatURL = models.CharField(max_length=500)
    webformatWidth = models.CharField(max_length=20)
    webformatHeight = models.CharField(max_length=20)
    largeImageURL = models.CharField(max_length=520)
    imageWidth = models.CharField(max_length=20)
    imageHeight = models.CharField(max_length=20)
    imageSize = models.CharField(max_length=20)
    views = models.CharField(max_length=20)
    downloads = models.CharField(max_length=20)
    collections = models.CharField(max_length=20)
    likes = models.CharField(max_length=20)
    comments = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    user = models.CharField(max_length=50)
    userImageURL = models.CharField(max_length=100)
    isActive = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.previewURL

class Blog(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    