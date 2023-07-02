from django.shortcuts import render
from .models import *

def main(request):
    title = 'Мой заголовок страницы'
    return render(request, 'main.html', {'title': title})
