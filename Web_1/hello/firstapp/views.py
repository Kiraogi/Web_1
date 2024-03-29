import datetime
from django.shortcuts import render, redirect
from .forms import *
from .models import Person, Image, File, VideoFile, AudioFile
from django.template.response import TemplateResponse
from django.http import *


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

    # header = 'Фильтры в шаблонах'  #
    # value_num = 5
    # value_date = datetime.datetime.now()
    # value_time = datetime.datetime.now()
    # value_title = 'Это пример использования фильтра title'
    # value_upper = 'Это пример использования фильтра upper'
    # value_lower = 'Это пример использования фильтра lower'
    # data = {'header': header, 'value_num': value_num, 'value_date': value_date, 'value_time': value_time,
    #         'value_title': value_title, 'value_upper': value_upper, 'value_lower': value_lower}

    # my_kv = ['I квартал ->', 'II квартал ->', 'III квартал ->', 'IV квартал ->']
    # my_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    # context = {'my_month': my_month, 'my_kv': my_kv}

    my_text = 'Изучаем модели Django!'
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, 'people_kol': people_kol}
    return render(request, 'firstapp/index.html', context)


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return render(request, 'firstapp/contact.html')


def my_form(request):
    # my_form = UserForm()
    # # my_form = UserForm(field_order=['age', 'name'])
    # context = {"form": my_form}
    # return render(request, "firstapp/my_form.html", context)
    # userform = UserForm()
    # if request.method == 'POST':
    #     userform = UserForm(request.POST)
    #     if userform.is_valid():
    #         name = userform.cleaned_data['name']
    #         return HttpResponse("<h2>Имя введено корректно - {0}</h2>".format(name))
    # return render(request, "firstapp/my_form.html", {'form': userform})
    #
    # if request.method == 'PSOT':
    #     userform = UserForm(request.POST)
    #     if userform.is_valid():
    #         name = request.POST.get('name') # Получить значение поля name
    #         age = request.POST.get('age') # Получить значение поля age
    #         output = "<h2>Пользователь</h2><h3>Имя: {0}, Возраст: {1}</h3>".format(name, age)
    #         return HttpResponse(output)
    # userform = UserForm()
    # return render(request, "firstapp/my_form.html", {'form': userform})

    # Взаимодействие с формой ввода данных о клиенте
    if request.method == "POST":  # Пользователь отправил данные
        form = UserForm(request.POST)  # Создание экземпляра формы
        if form.is_valid():  # Проверка валидности формы
            form.save()  # Запись данных в БД
            # Остаемся на той же странице, обновляем форму
        else:
            # Вывод ошибок вместо данных
            print(form.errors)
        # Загрузка формы для ввода клиента
    my_text = 'Сведенья о клиенте'
    people = Person.object_person.all()
    form = UserForm()
    context = {'form': form, 'my_text': my_text, 'people': people}
    return render(request, "firstapp/my_form.html", context)


def access(request, age):
    # Если возраст НЕ выходит в диапазон 1-110, посылаем сообщение 400
    if age not in range(1, 110):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:  # Если возраст больше 17, то доступ разрешен
        return HttpResponse("Доступ разрешен")
    else:  # Если нет, то возвращаем ошибку 403
        return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")


# def about(request):
#     return HttpResponse("<h2>О сайте</h2>")
#
#
# def contact(request):
#     return HttpResponseRedirect('/about')
#     # return HttpResponse("<h2>Контакты</h2>")


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


def db(request):
    # Если это POST-запрос, то нужно обрабатывать данные, полученные из формы
    if request.method == 'POST':
        # создаем экземпляр формы и заполнение ее введенными данными
        form = NameForm(request.POST)
        # Проверяем валидность формы
        if form.is_valid():
            # Обработка данных формы (например, запись в БД)
            form.save()
            # Перенаправление на другую страницу
            return redirect('new_form')


def edit_form(request, id):  # Изменение данных клиента в  БД
    person = Person.object_person.get(id=id)
    # Если пользователь вернул отредактированные данные
    if request.method == "POST":
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
        return redirect('my_form')
    # Если пользователь отправляет данные на редактирование
    data = {'person': person}
    return render(request, 'firstapp/edit_form.html', context=data)


# Удаление данных о клиенте
def delete(request, id):  # Удаление данных о клиенте
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('my_form')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>объект не найден</h2>')

    # Создание пустой формы
    form = NameForm()
    context = {'form': form}
    return render(request, 'name.html', context)


def form_up_img(request):  # Загрузка изображения
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'form': form, 'my_text': my_text, 'my_img': my_img}
    return render(request, "firstapp/form_up_img.html", context)


def delete_img(request, id):  # Удаление изображения
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Image.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_pdf(request):  # Загрузка PDF
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загруженные файлы'
    form = FileForm()
    file_obj = File.objects.all()
    context = {'form': form, 'my_text': my_text, 'file_obj': file_obj}
    return render(request, "firstapp/form_up_pdf.html", context)


def delete_pdf(request, id):  # Удаление PDF
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except File.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_video(request):  # Загрузка видео
    if request.method == "POST":
        form = VideoFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загрузка видеофайла'
    form = VideoFrom()
    file_obj = VideoFile.obj_video.all()
    context = {'form': form, 'my_text': my_text, 'file_obj': file_obj}
    return render(request, "firstapp/form_up_video.html", context)


def delete_video(request, id):  # Удаление видео
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        return redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')


def form_up_audio(request):  # Загрузка аудио
    if request.method == "POST":
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    my_text = 'Загрузка аудио'
    form = AudioForm()
    file_obj = AudioFile.obj_audio.all()
    context = {'form': form, 'my_text': my_text, 'file_obj': file_obj}
    return render(request, "firstapp/form_up_audio.html", context)


def delete_audio(request, id):  # Удаление аудио
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Объект не найден</h2>')
