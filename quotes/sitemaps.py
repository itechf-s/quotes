from django.utils.text import Truncator, slugify
from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from quotes.models import Quotes

class QuotesDetailsSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Quotes.objects.filter(isActive=1).filter(publishAt__lt = timezone.now()).order_by('-publishAt')[:50]

    def lastmod(self, obj):
        return obj.publishAt

    def location(self, item):
        slugTxt = slugify(Truncator(item.quotes).words(5))
        return '/quotes/' + slugTxt + '-by-' + slugify(item.author) + '-' + str(item.id)

class QuotesAuthorSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Quotes.objects.values('author').filter(isActive=1).filter(publishAt__lt = timezone.now()).order_by('author').distinct()

    def location(self, item):
        return '/authors/' + slugify(item['author']) + '-quotes'
    
class QuotesCategorySitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.5

    def items(self):
        return Quotes.objects.values('category').filter(isActive=1).filter(publishAt__lt = timezone.now()).order_by('category').distinct()

    def location(self, item):
        return '/' + slugify(item['category']) + '-quotes'