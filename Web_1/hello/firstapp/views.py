import datetime

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.http import HttpResponseBadRequest, HttpResponseForbidden


def index(request):
    # header = 'Персональные данные' # Символьная переменная
    # langs = ['Python', 'Java', 'C++', 'C#'] # Список
    # user = {'name': 'Igor', 'age': 25} # Словарь
    # addr = ('Россия', 'Москва', 'Льва Толстого', '16', '1') # Кортеж
    # data = {'header': header, 'langs': langs, 'user': user, 'addr': addr}
    # return TemplateResponse(request, 'firstapp/index.html', data)

    # header = 'Иностранные языки' # Символьная переменная
    # list_langs = ['Python', 'Java', 'C++', 'C#'] # Список
    # data = {'header': header, 'list_langs': list_langs}
    # return render(request, 'firstapp/index.html', data)

    # header = 'Разветления в шаблоне'
    # num =5
    # var1 = "Это первая ветка в инструкции if"
    # var2 = "Это вторая ветка в инструкции if"
    # data = {'header': header, 'num': num, 'var1': var1, 'var2': var2}
    # return render(request, 'firstapp/index_app1.html', data)

    header = 'Фильтры в шаблонах' #
    value_num = 5
    value_date = datetime.datetime.now()
    value_time = datetime.datetime.now()
    value_title = 'Это пример использования фильтра title'
    value_upper = 'Это пример использования фильтра upper'
    value_lower = 'Это пример использования фильтра lower'
    data = {'header': header, 'value_num': value_num, 'value_date': value_date, 'value_time': value_time, 'value_title': value_title, 'value_upper': value_upper, 'value_lower': value_lower}
    return render(request, 'firstapp/index_app1.html', data)



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
