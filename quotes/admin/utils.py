#Import required libraries
import os
from quotes.admin.wpmodels import Images
import textwrap
from PIL import Image, ImageDraw, ImageFont
import urllib.request
from bestrani import env

app_root = env.get('quotes', 'APP_ROOT')
image_path = env.get('quotes', 'IMG_DIR')
fontDir = env.get('quotes', 'FONT_DIR')
fonts = env.get('quotes', 'FONT_LIST').split(',')
fontAndWordwrap = eval(env.get('quotes', 'FONT_AND_WORDWRAP'))
qHeight = int(env.get('quotes', 'HEIGHT'))
qWidth = int(env.get('quotes', 'WIDTH'))
pinHeight = int(env.get('quotes', 'PIN_HEIGHT'))
pinWidth = int(env.get('quotes', 'PIN_WIDTH'))
    
def writeQuotesOnImage(qot, param):   
    #Create Image object
    imageId = param[3] if param[3] else qot.imageId
    if not isImageExist(imageId):
        imageId = findOneImage().id
    fileName = app_root + image_path + 'raw/' + str(imageId) + '.jpg'

    im = Image.open(fileName)
    print(im.size)
    rNum = qot.id % len(fonts)

    fixed_height = qHeight
    height_percent = (fixed_height / float(im.size[1]))
    width_size = int((float(im.size[0]) * float(height_percent)))
    if width_size < qWidth:
        width_size = qWidth
    im = im.resize((width_size, fixed_height), Image.HAMMING)

    left = 0
    top = 0
    right = qWidth
    bottom = qHeight

    im = im.crop((left, top, right, bottom))
    
    font = app_root + fontDir + fonts[rNum]
    
    fSize = param[0] if param[0] else qot.fontSize
    wordWrap = param[1] if param[1] else qot.wordWrap
    fontColor = param[2] if param[2] else qot.fontColor

    #Update Value
    qot.fontSize = fSize
    qot.wordWrap = wordWrap
    qot.fontColor = fontColor
    qot.imageId = imageId
    qot.save()
    
    fSize = int(fSize)
    wordWrap = int(wordWrap)
    if fSize == None or fSize < 15:
        fSize = 20
    fontH1 = ImageFont.truetype(font, fSize)
    fontH2 = ImageFont.truetype(font, fSize + 3)

    #Draw line
    draw = ImageDraw.Draw(im)
    
    w, h = im.size
    
    lines = textwrap.wrap(qot.quotes, width=wordWrap)
    y_text = h/10 + 10
    for line in lines:
        width, height = fontH1.getsize(line)
        #print(width, height)
        if h > y_text + height*2:
            draw.text(((w - width) / 2, y_text), line, font=fontH2, fill=fontColor)
            y_text += height

    width, height = fontH2.getsize(qot.author)

    draw.text(((w / 2 - width/2) , y_text + height/4), qot.author, font=fontH1, fill=fontColor)
    #draw.multiline_text((45, 75), txt, fill=(18, 19, 20), font=fontH1)

    #Show image
    createDir(app_root + image_path + qot.imagePath)
    im.save(app_root + image_path + qot.imagePath, optimize = True, quality = 70)
    print('writeQuotesOnImage done for id: ', qot.id)

def writeQuotesOnImagePin(qot, param):   
    #Create Image object
    imageId = param[3] if param[3] else qot.imageId
    if not isImageExist(imageId):
        imageId = findOneImage().id
    fileName = app_root + image_path + 'raw/' + str(imageId) + '.jpg'
    im = Image.open(fileName)
    rNum = qot.id % len(fonts)

    fixed_height = pinHeight
    height_percent = (fixed_height / float(im.size[1]))
    width_size = int((float(im.size[0]) * float(height_percent)))
    if width_size < qWidth:
        width_size = qWidth
    im = im.resize((width_size, fixed_height), Image.NEAREST)

    left = 0
    top = 0
    right = pinWidth
    bottom = pinHeight
    
    im = im.crop((left, top, right, bottom))
    
    font = app_root + fontDir + fonts[rNum]
    
    fSize = param[0] if param[0] else qot.fontSize
    wordWrap = param[1] if param[1] else qot.wordWrap
    fontColor = param[2] if param[2] else qot.fontColor

    #Update Value
    qot.fontSize = fSize
    qot.wordWrap = wordWrap
    qot.fontColor = fontColor
    qot.imageId = imageId
    qot.save()
    
    fSize = int(fSize)
    wordWrap = int(wordWrap) - 6
    fSize = fSize + 55

    fontH1 = ImageFont.truetype(font, fSize)
    fontH2 = ImageFont.truetype(font, fSize + 3)

    #Draw line
    draw = ImageDraw.Draw(im)

    w, h = im.size
    
    lines = textwrap.wrap(qot.quotes, width=wordWrap)
    y_text = h/9 + 10
    for line in lines:
        width, height = fontH1.getsize(line)
        #print(width, height)
        if h > y_text + height*2:
            draw.text(((w - width) / 2, y_text), line, font=fontH2, fill=fontColor)
            y_text += height

    width, height = fontH2.getsize(qot.author)

    draw.text(((w / 2 - width/2) , y_text + height/4), qot.author, font=fontH1, fill=fontColor)
    #draw.multiline_text((45, 75), txt, fill=(18, 19, 20), font=fontH1)

    #Show image
    createDir(app_root + image_path + qot.imagePathPin)
    im.save(app_root + image_path + qot.imagePathPin, optimize = True, quality = 70)
    print('writeQuotesOnImage done for id: ', qot.id)


def findFontSize(Qlen):
    wordWrap = 38
    fontSize = 11
    for len, fontWrap in fontAndWordwrap.items():
        if Qlen <= len:
            fontSize = fontWrap[0]
            wordWrap = fontWrap[1]
            print('Quotes Length : ', Qlen, ' | fontSize: ', fontSize, ' wordwrap : ', wordWrap)
            break
    return (fontSize, wordWrap)


def findFontSize2(len, width):
    width = int(width)
    wordWrap = 38
    print('image : ', width)
    fontSize = int(9 * width/1000)

    if len > 350:
        fontSize = 30
    elif len > 300:
        fontSize = 35
        wordWrap = 35
    elif len > 250:
        fontSize = 40
        wordWrap = 32
    elif len > 200:
        fontSize = 45
        wordWrap = 30
    elif len > 150:
        fontSize = 50
        wordWrap = 28
    elif len > 100:
        fontSize = 52
        wordWrap = 21
    elif len > 50:
        fontSize = 55
        wordWrap = 21
    elif len > 25:
        fontSize = 60
        wordWrap = 20
    else:
        fontSize = 65
        wordWrap = 15
    print('final font size', fontSize, wordWrap)
    return (fontSize, wordWrap)

def downloadImage(id, url):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    fileName = app_root + image_path + 'raw/' + str(id) + '.jpg'
    urllib.request.urlretrieve(url, fileName)

def createDir(dirName):
    #fullPath = os.path.join(app_root, dirName)
    dirName = os.path.dirname(dirName)
    isDir = os.path.isdir(dirName) 
    if not isDir:
        os.mkdir(dirName, mode = 0o755)
        print('Dir Created on : ', dirName)

def isImageExist(imageId):
    flag = False
    fileName = app_root + image_path + 'raw/' + str(imageId) + '.jpg'
    if os.path.isfile(fileName):
        print('file found')
        flag = True
    return flag

def deleteImagePin(qot):
    flag = False
    fileName = app_root + image_path + qot.imagePathPin
    if os.path.isfile(fileName):
        print('file found')
        os.remove(fileName)
        flag = True
    return flag

def findOneImage():
    img = Images.objects.filter(isActive=1).filter(isDeleted=0).order_by('?').first()
    if img:
        if isImageExist(img.id):
            return img
        else:
            img.isDeleted = 1
            img.save()
            findOneImage()