"""
URL configuration for ch2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_fun/', views.my_function, name='my_function'),
    path('', views.home, name='home'),
    path('django-p/', views.learn_django, name='django_page'),
    path('python-p/', views.learn_python, name='python_page'),
    path('math-p/', views.learn_math, name='math_learn'),
    path('php-p/', views.learn_php, name='php_learner'),
    path('add-p/',views.add,name='addition')
    
]
