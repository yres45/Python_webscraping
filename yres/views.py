# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:32:22 2019

@author: Yres
"""

from django.shortcuts import render



# Создайте ваше отображение здесь

from .models import Package





# получение данных из бд


def main (request):
     Login = request.POST.get('login')
     Password = request.POST.get('password')
     submitbutton = request.POST.get('Submit')     
     context = {'Login':Login, 'Password':Password, 'submitbutton':submitbutton}    

     return render(request,"aut.html",context)


def about (request):
     return render(request,"about.html")

def portf (request):
     return render(request,"portfolio.html")


def index(request):
     mail = Package.objects.all()
     return render(request,"index.html",{"mail":mail})


# ...

# сохранение данных в бд
#def create(request):
#    if request.method == "POST":
#        tom = Person()
#        tom.name = request.POST.get("name")
#        tom.age = request.POST.get("age")
#        tom.save()
#    return HttpResponseRedirect("/")



#def index(request):
#    """
#    Функция отображения для домашней страницы сайта.
#    """
#    # Генерация "количеств" некоторых главных объектов
#    num_books = Book.objects.all().count()
#    num_instances=BookInstance.objects.all().count()
#    # Доступные книги (статус = 'a')
#    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
#    num_authors=Author.objects.count()  # Метод 'all()' применен по умолчанию.
#    
#    # Отрисовка HTML-шаблона index.html с данными внутри 
#    # переменной контекста context
#    return render(
#        request,
#        'index.html',
#        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
#    )