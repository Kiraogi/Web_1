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
