from django.db import models
from django.utils.text import Truncator

# Create your models here.
class Quotes(models.Model):
    locale = models.IntegerField(default=1)
    quotes = models.CharField(max_length=500)
    quotesTxt = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=50)
    authorSlug = models.CharField(max_length=50, default='author')
    category = models.CharField(max_length=50)
    categorySlug = models.CharField(max_length=50, default='category')
    imageId = models.IntegerField(null=True, blank=True)
    imagePath = models.CharField(max_length=200, null=True, blank=True)
    imagePathPin = models.CharField(max_length=200, null=True, blank=True)
    rawImage = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    imageAlt = models.CharField(max_length=200, null=True, blank=True)
    isActive = models.IntegerField(default=0)
    isUpdated = models.IntegerField(default=0)
    isSchd = models.IntegerField(default=0)
    isAuto = models.IntegerField(default=0)
    isPin = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    publishAt = models.DateTimeField(null=True, blank=True)
    desc = models.CharField(max_length=1500, null=True, blank=True)
    fontName = models.CharField(max_length=50, null=True, blank=True)
    createdBy = models.CharField(max_length=10, null=True, blank=True)
    fontSize = models.IntegerField(null=True, blank=True)
    wordWrap = models.IntegerField(null=True, blank=True)
    fontColor = models.CharField(max_length=50, null=True, blank=True)
    xyPos = models.CharField(max_length=50, null=True, blank=True)
    xyPos2 = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        qotTxt = Truncator(self.quotes).words(5)
        return str(self.id) + '. ' + qotTxt + ' By ' + self.author