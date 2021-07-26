"""
Bestrani Quotes App URL Configuration
"""
from django.urls import path
from quotes import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from quotes.sitemaps import QuotesAuthorSitemap, QuotesCategorySitemap, QuotesDetailsSitemap

sitemaps = {'quotes': QuotesDetailsSitemap, 'author' : QuotesAuthorSitemap, 'category' : QuotesCategorySitemap}

urlpatterns = [
    path('',views.index, name='index'),
    path('<slug:category>-quotes',views.category, name='category'),
    path('authors/<slug:authorSlug>-quotes',views.author, name='author'),
    path('authors-list',views.authorsList, name='authorsList'),
    path('category-list',views.categoryList, name='categoryList'),
    path('image-list',views.imageList, name='imageList'),
    path('quotes/<slug:quotesSlug>-<int:id>',views.details, name='details'),
    path('search',views.search, name='search'),
    path('mycms',views.showLogin, name='login'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
]