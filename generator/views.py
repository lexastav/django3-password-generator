from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = [chr(c) for c in range(97, 123)]
    if request.GET.get('uppercase'):
        characters.extend(chr(uc) for uc in range(65, 91))
    if request.GET.get('special'):
        characters.extend(chr(sc) for sc in range(33, 48))
        characters.extend(chr(sc1) for sc1 in range(58, 64))
    if request.GET.get('numbers'):
        characters.extend(str(n) for n in range(10))

    length = int(request.GET.get('length', 10))
    the_password = ''
    for _ in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
