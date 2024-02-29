from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden


def index(request):
    return TemplateResponse(request, 'firstapp\home.html')


def access(request, age):
    # Если возраст НЕ выходит в диапазон 1-110, посылаем сообщение 400
    if age not in range(1, 110):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17: # Если возраст больше 17, то доступ разрешен
        return HttpResponse("Доступ разрешен")
    else: # Если нет, то возвращаем ошибку 403
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact(request):
    return HttpResponseRedirect('/about')
    # return HttpResponse("<h2>Контакты</h2>")


def products(request, productid=1):
    category = request.GET.get('cat', 'Не задана')
    output = "<h2>Товар № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get('id', 'Не задан')
    name = request.GET.get('name', 'Не задано')
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
    return HttpResponse(output)


def details(request):
    return HttpResponsePermanentRedirect('/')
