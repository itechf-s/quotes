from pixabay import Image
from quotes.admin.wpmodels import Images
from django.db.utils import IntegrityError
from quotes.admin import utils
import re
from bestrani import env

API_KEY = env.get('security', 'PIXABAY_API_KEY')

# image operations

# custom image search
def saveImagesInDb(param):
    q = param['q']
    url = param['url']
    isPin = param.get('isPin')
    id = ''
    urlList = url.split('\r\n')

    if urlList:
        for urlTxt in urlList:
            id = re.findall('\d+', urlTxt)[0]
            q=''
            downloadImage('', id, isPin)
    elif q:
        downloadImage(q, '', isPin)
    else:
        print('Param not Found')

def downloadImage(q, id, isPin):
    print(q, id, isPin)
    image = Image(API_KEY)
    ims = image.search(q=q,
                id=id,
                image_type='photo',
                orientation='horizontal',
                category='animals',
                safesearch='true',
                order='latest',
                page=1,
                colors='"red", "turquoise", "blue", "lilac", "pink", "gray", "black", "brown"',
                per_page=100)

    hits = ims['hits']
    for hit in hits:
        try:
            iVal =  (None,) + tuple(hit.values()) + (1,)
            img = Images(*iVal)
            img.save()
            utils.downloadImage(img.id, img.webformatURL)
            if isPin:
                img.isPin = isPin
                print('pintrest selected')
                utils.downloadImage('pin-' + str(img.id), img.largeImageURL)
                img.save()
        except IntegrityError:
            print('error in unique key')