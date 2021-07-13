#Import required libraries
import textwrap, time
from django.utils.text import slugify
from quotes.admin.wpmodels import Images
from quotes.admin import utils

def updateQuotesImage(quotesObj):

    for obj in quotesObj:

        imgText = textwrap.wrap(obj.quotes, width=45)[0]
        today = time.strftime('%Y%m%d')
        obj.imagePath = today + "/" + slugify(imgText) + '.jpg'
        obj.imageAlt = imgText
        obj.isUpdated = 1
        img = Images.objects.filter(isActive=1).filter(webformatHeight__gt=400).order_by('?').first()
        obj.fontSize = utils.findFontSize(obj.quotes.__len__(), img.webformatWidth)
        obj.wordWrap = 30
        obj.rawImage = img.previewURL
        obj.fontColor = 'white'
        obj.imageId=img.id
        obj.save()