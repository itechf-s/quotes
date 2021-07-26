#Import required libraries
import textwrap, time
from django.utils.text import slugify
from quotes.admin.wpmodels import Images
from quotes.admin import utils

def updateQuotesImage(quotesObj):

    for obj in quotesObj:

        imgText = textwrap.wrap(obj.quotes, width=45)[0]
        today = time.strftime('%Y%m%d')
        obj.imagePath = today + '/' + slugify(imgText) + '-' + str(obj.id) + '.jpg'
        obj.imagePathPin = today + '/' + slugify(imgText) + '-pin-' + str(obj.id) + '.jpg'
        obj.imageAlt = imgText
        obj.authorSlug = slugify(obj.author)
        obj.title = textwrap.wrap(obj.quotes, width=100)[0]
        obj.isUpdated = 1
        img = utils.findOneImage()
        fontPlusWrap = utils.findFontSize(obj.quotes.__len__())
        obj.fontSize = fontPlusWrap[0]
        obj.wordWrap = fontPlusWrap[1]
        obj.rawImage = img.previewURL
        obj.fontColor = 'white'
        obj.imageId=img.id
        obj.save()