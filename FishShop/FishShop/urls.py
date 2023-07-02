from django.contrib import admin
from django.urls import path
from fish.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
]
