from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse('This is home')
    return render(request, 'PasswordGeneratorApp/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase', False):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVUWXYZ'))
    if request.GET.get('numbers', False):
        characters.extend(list('0123456789'))
    if request.GET.get('special', False):
        characters.extend(list('!@#$%^&*()'))

    generatedpassword = [random.choice(characters) for x in range(0, length)]
    # print(characters)

    return render(request, 'PasswordGeneratorApp/Password.html', {'password': ''.join(generatedpassword)})

def about(request):
    return render(request, 'PasswordGeneratorApp/about.html')
