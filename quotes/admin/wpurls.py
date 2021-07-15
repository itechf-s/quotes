"""
Bestrani Quotes App URL Configuration
"""
from os import name
from django.urls import path
from quotes.admin import wpviews
urlpatterns = [
    path('update',wpviews.update, name='update'),
    path('make-quote',wpviews.makeQuote, name='makeQuote'),
    path('list/<int:isActive>/<int:isUpdated>',wpviews.list, name='list'),
    path('activate',wpviews.activate, name='activate'),
    path('activateSchedule',wpviews.activateSchedule, name='activateSchedule'),
    path('cache-purge', wpviews.cachePurge, name='cachePurge'),
    path('import-quotes', wpviews.importQuotes, name='cachePurge'),

    path('saveImagesInDb',wpviews.saveImagesInDb, name='saveImagesInDb'),
    path('list-images/<int:isActive>',wpviews.listImages, name='listImages'),
    path('act-image',wpviews.actImage, name='actImage'),

    path('chk-login',wpviews.chkLogin, name='login'),
    path('chk-logout',wpviews.chkLogout, name='logout'),
]