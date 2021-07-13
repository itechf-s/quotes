from django.contrib import admin
from quotes.models import Quotes
from quotes.admin.wpmodels import Images, Blog
# Register your models here.
admin.site.register(Quotes)
admin.site.register(Images)
admin.site.register(Blog)
