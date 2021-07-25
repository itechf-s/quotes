from django.shortcuts import render
from django.utils import timezone
from quotes.models import Quotes
from quotes import seo
from bestrani import env

rows = int(env.get('quotes','ROWS'))
pinRows = int(env.get('quotes','PIN_ROWS'))
urlPrefix = env.get('general','URL_PREFIX')

print(urlPrefix)
def index(request):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:pinRows]
    filterParam['isPin'] = 0
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/'
    metas = seo.setMetas(quotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, 'urlPrefix' : urlPrefix, 'pinQuotes': pinQuotes})

def category(request, category):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1, 'category' : category}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:pinRows]
    filterParam['isPin'] = 0
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/' + category + '-quotes'
    metas = seo.setMetas(quotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'pinQuotes': pinQuotes})

def author(request, authorSlug):
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:pinRows]
    filterParam['isPin'] = 0
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/authors/' + authorSlug + '-quotes'
    metas = seo.setMetas(quotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'pinQuotes': pinQuotes})

def details(request, quotesSlug, id):
    quote1 = Quotes.objects.filter(id=id).filter(publishAt__lt = timezone.now()).filter(isActive=1).first()
    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now(), 'isPin' : 1}
    pinQuotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:pinRows]
    filterParam['isPin'] = 0
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    quotes = Quotes.objects.filter(**filterParam).exclude(id=id).order_by('-publishAt')[:rows]
 
    url = urlPrefix + '/quotes/' + quotesSlug + '-' + str(id)
    metas = seo.setMetas((quote1,), url)
    return render(request, 'details.html', {'quotes': quotes, 'quote1' : quote1, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix, 'pinQuotes': pinQuotes})

def showLogin(request):
    return render(request, 'login.html')

def search(request):
    q = request.GET.get('q', None)

    filterParam = {'isActive' : 1, 'publishAt__lt' : timezone.now()}
    if q:
        filterParam['category__istartswith'] = q
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    
    if not quotes.exists():
        filterParam['quotes__istartswith'] = q
        filterParam.pop('category__istartswith')
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]


    if not quotes.exists():
        filterParam['quotes__icontains'] = q
        filterParam.pop('quotes__istartswith')
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    
    if not quotes.exists():
        filterParam.pop('quotes__icontains')
    
    quotes = Quotes.objects.filter(**filterParam).order_by('-publishAt')[:rows]
    url = urlPrefix + '/search?q=' + q
    metas = seo.setMetas(quotes, url)
    return render(request, 'index.html', {'quotes': quotes, 'metas' : metas, 'url': url, "urlPrefix" : urlPrefix})

