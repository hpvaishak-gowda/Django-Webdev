from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('This is a Home page')



def my_function(request):               #This is called as a view function or function based view.
    # Logic is written here
    return HttpResponse('Hai vaishak How are you ')

def learn_django(request):
    return HttpResponse('Hai Django***')

def learn_python(request):            
    return HttpResponse('<h1>Hellow Django</h1>')

def learn_math(request):
    add=10+13
    return HttpResponse(add)


def learn_php(request):
    var='<h1>Hellow PHP</h1>'            
    return HttpResponse(var)

def add(req):
    html_code='<h1>Hai add means addition</h2>'
    return HttpResponse(html_code)