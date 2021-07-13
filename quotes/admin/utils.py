#Import required libraries
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
import urllib.request
from bestrani import env

app_root = env.get('quotes', 'APP_ROOT')
image_path = env.get('quotes', 'IMG_DIR')
fontDir = env.get('quotes', 'FONT_DIR')
fonts = env.get('quotes', 'FONT_LIST').split(',')
    
def writeQuotesOnImage(qot, param):   
    #Create Image object
    imageId = param[3] if param[3] != None else qot.imageId
    fileName = app_root + image_path + 'raw/' + str(imageId) + '.jpg'
    im = Image.open(fileName)
    rNum = qot.id % len(fonts)
    
    print(fonts, rNum)
    print(fonts[rNum])
    font = app_root + fontDir + fonts[rNum]
    print(font)
    
    fSize = param[0] if param[0] != None else qot.fontSize
    wordWrap = param[1] if param[1] != None else qot.wordWrap
    fontColor = param[2] if param[2] != None else qot.fontColor

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
    im.save(app_root + image_path + qot.imagePath)
    print('writeQuotesOnImage done for id: ', qot.id)

def findFontSize(len, width):
    width = int(width)
    print('image : ', width)
    fontSize = int(9 * width/1000)

    if len > 500:
        fontSize = fontSize * 1
    elif len < 500 and len > 400:
        fontSize = fontSize = fontSize * 3
    elif len < 400 and len > 300:
        fontSize = fontSize * 5
    elif len < 300 and len > 200:
        fontSize = fontSize * 6
    elif len < 200 and len > 100:
        fontSize = fontSize * 7
    else:
        fontSize = fontSize * 8
    return fontSize

def downloadImage(id, url):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    fileName = app_root + image_path + 'raw/' + str(id) + '.jpg'
    img = urllib.request.urlretrieve(url, fileName)
    print(img)

def createDir(dirName):
    #fullPath = os.path.join(app_root, dirName)
    dirName = os.path.dirname(dirName)
    isDir = os.path.isdir(dirName) 
    if not isDir:
        os.mkdir(dirName, mode = 0o755)
        print('Dir Created on : ', dirName)

