from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.utils import timezone
from django.shortcuts import redirect, render
from quotes.models import Quotes
from quotes.admin import data, process, db, getImages, utils
from quotes.admin.wpmodels import Images
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from quotes.admin import cache
from bestrani import env

imageRows = int(env.get('quotes', 'IMAGE_ROWS'))
adminRows = int(env.get('quotes', 'ADMIN_ROWS'))
createRows = int(env.get('quotes', 'CREATE_ROWS'))
autoPinMaxChar = int(env.get('quotes', 'AUTO_PIN_MAX_CHAR'))
pinMod = int(env.get('quotes', 'PIN_MOD'))
autoCreateRows = int(env.get('quotes', 'AUTO_CREATE_ROWS'))
qotFilePath = env.get('quotes', 'TSV_FILE_PATH')


def showLogin(request):
    return render(request, 'login.html')

def chkLogin(request):
    if request.method == 'POST':
        user = request.POST.get('user', None)
        password = request.POST.get('password', None)

        print(user, password)
        dbUser = authenticate(username=user, password=password)
        if dbUser is not None:
            messages.success(request, 'Login success')
            login(request, dbUser)
            return redirect('/wp-admin/list/0/1')
        else:
            messages.error(request,'Invalid user password')
            return redirect('/mycms')
    else:
        messages.error(request,'Login Failed')
        return redirect('/mycms')


@login_required(login_url='/mycms')
def list(request, isActive, isUpdated):
    category = request.GET.get('category', None)
    quotesTxt = request.GET.get('quotes', None)
    author = request.GET.get('author', None)
    locale = request.GET.get('locale', None)
    id = request.GET.get('id', None)
    isSchd = request.GET.get('isSchd', None)

    filterParam = {'isActive' : isActive, 'isUpdated' : isUpdated}
    if quotesTxt:
        filterParam['quotes__startswith'] = quotesTxt
    if category:
        filterParam['category'] = category
    if author:
        filterParam['author'] = author
    if locale:
        filterParam['locale'] = locale
    if id:
        filterParam['id'] = id
    if isSchd:
        filterParam['isSchd'] = isSchd

    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')
    paginator = Paginator(quotes, adminRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})

@login_required(login_url='/mycms')
def activate(request):
    id = request.POST.get('id', None)
    isActive = request.POST.get('isActive', None)
    isSchd = request.POST.get('isSchd', None)

    quote = None
    if id:
        quote = Quotes.objects.filter(id=id).first()
        if isActive == '1':
            db.activateQuotes(quote)
        elif isActive == '0':
            db.deAactivateQuotes(quote)
        elif isSchd:
            db.scheduleQuotes(quote, isSchd)    
    return render(request, 'activate.html', {'quotes': quote})

def runSchedule():
    filterParam = {'isActive' : 0, 'isUpdated' : 1, 'isSchd' : 1}
    quote = Quotes.objects.filter(**filterParam).order_by('id').first()
    bulkQuotes(autoCreateRows)
    db.activateQuotes(quote)

@login_required(login_url='/mycms')
def update(request):
    id = request.POST.get('id', None)
    print(id)
    if id:
        quotes = Quotes.objects.filter(id=id).order_by('id')[:2]
    else:
        quotes = Quotes.objects.filter(isUpdated=0).order_by('id')[:createRows]
    process.updateQuotesImage(quotes)
    return render(request, 'list.html', {'quotes': quotes})

@login_required(login_url='/mycms')
def saveImagesInDb(request):
    getImages.saveImagesInDb(request.GET)
    rawImages = Images.objects.filter(isActive=1).filter(createdAt__lt = timezone.now()).order_by('-createdAt')[:adminRows]
    return render(request, 'images.html', {'images': rawImages})

@login_required(login_url='/mycms')
def listImages(request, isActive):
    tags = request.GET.get('tags', None)
    filterParam = {'isActive' : isActive, 'createdAt__lt' : timezone.now()}
    if tags:
        filterParam['tags__icontains'] = tags
    rawImages = Images.objects.filter(**filterParam).order_by('-createdAt')
    paginator = Paginator(rawImages, imageRows)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'images.html', {'page_obj': page_obj})

@login_required(login_url='/mycms')
def actImage(request):
    id = request.POST.get('id', None)
    isActive = request.POST.get('isActive', None)
    image = None
    if id != None:
        image = Images.objects.filter(id=id)
        db.activateImage(image, isActive)      
    return render(request, 'activate.html')

@login_required(login_url='/mycms')
def makeQuote(request):
    id = request.POST.get('id', None)
    wordWrap = request.POST.get('wordWrap', None)
    fontSize = request.POST.get('fontSize', None)
    fontName = request.POST.get('fontName', None)
    fontColor = request.POST.get('fontColor', None)
    imageId = request.POST.get('imageId', None)
    isPin = request.POST.get('isPin')
    param = (fontSize, wordWrap, fontColor, imageId, fontName)
    print('id : ', id)
    quote = None
    if id != None:
        quote = Quotes.objects.filter(id=id).filter(isUpdated=1).first()
        if quote:
            if isPin:
                quote.isPin = isPin
                utils.writeQuotesOnImagePin(quote, param)
            else:
                quote.isPin = 0
                utils.deleteImagePin(quote)
            utils.writeQuotesOnImage(quote, param)      
    return redirect('/wp-admin/list/0/1?isSchd=0')

@login_required(login_url='/mycms')
def makeBulkQuotes(request):
    rows = int(request.GET.get('rows', None))
    rows = rows if rows else 2
    bulkQuotes(rows)
    return redirect('/wp-admin/list/0/1?isSchd=0')

def bulkQuotes(rows):
    filterParam = {'isUpdated' : 0, 'isAuto': 0, 'isSchd': 0, 'isActive' : 0}
    quotes = Quotes.objects.filter(**filterParam).order_by('id')[:rows]
    process.updateQuotesImage(quotes)
    for quote in quotes:
        param = ('', '', '', '')
        quote.isAuto = 1
        utils.writeQuotesOnImage(quote, param)
        if quote.id % pinMod == 0 and quote.quotes.__len__() < autoPinMaxChar:
            quote.isPin = 1
            utils.writeQuotesOnImagePin(quote, param)

@login_required(login_url='/mycms')
def chkLogout(request):
    logout(request)
    messages.success(request,'Logout Success')
    return redirect('/')

@login_required(login_url='/mycms')
def cachePurge(request):
    id = request.GET.get('id', None)
    if id == '159753':
        cache.purge()
    else:
        print('Not Allowed')
    return redirect('/wp-admin/list/0/1')


@login_required(login_url='/mycms')
def importQuotes(request):
    username = request.user.username
    if request.method == 'POST':
        quotesFile = request.FILES['quotesFile'] if 'quotesFile' in request.FILES else None
        if quotesFile:
            fs = FileSystemStorage(location=qotFilePath)
            file = fs.save(quotesFile.name, quotesFile)
            data.csvImport(qotFilePath + file, username)
    return redirect('/wp-admin/list/0/1')