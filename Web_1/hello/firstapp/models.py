from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя клиента')
    age = models.IntegerField(verbose_name='Возраст клиента', validators=[
        MinValueValidator(1),  # Минимальное значение возраста
        MaxValueValidator(120)  # Максимальное значение возраста
    ])
    object_person = models.Manager()
    DoesNotExist = models.Manager()


class Image(models.Model):  # Загрузка изображения
    title = models.CharField(max_length=100, null=False, verbose_name="Описание изображения")
    image = models.ImageField(upload_to="images", null=True, blank=True, verbose_name="Файл с изображением")
    obj_img = models.Manager()

    def __str__(self):
        return self.title


class File(models.Model):  # Загрузка файлов
    title = models.CharField(max_length=100, verbose_name="Описание файла")
    file = models.FileField(upload_to="files", null=True, blank=True, verbose_name="Файл PDF")

    def __str__(self):
        return self.title


class VideoFile(models.Model):  # Загрузка видеофайлов
    title = models.CharField(max_length=100, verbose_name="Описание видеофайла")
    file = models.FileField(upload_to='videos', null=True, blank=True, verbose_name="Видеофайл")
    obj_video = models.Manager()

    def __str__(self):
        return self.title


class AudioFile(models.Model):  # Загрузка аудиофайлов
    title = models.CharField(max_length=100, verbose_name="Описание аудиофайла")
    file = models.FileField(upload_to='audio', null=True, blank=True, verbose_name="Аудиофайл")
    obj_audio = models.Manager()

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()


class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    course = models.ManyToManyField(Course)


class User(models.Model):
    name = models.CharField(max_length=30)


class Account(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
