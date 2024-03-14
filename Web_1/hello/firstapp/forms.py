from django import forms
from .models import Person


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Не менее 3-х символов", min_length=2, max_length=20)
    age = forms.IntegerField(label="Возраст", help_text="от 1 до 120 лет", min_value=0, max_value=120)
    # email = forms.EmailField(label="Электронная почта", help_text="Введите электронную почту")
    # reklama = forms.BooleanField(label="Согласны получать рекламу?", required=False)
    # comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
    # # field_order = ['age', 'name']


class UserFormCheckBox(forms.Form):
    basket = forms.BooleanField(label='Положите товар в корзину', required=False)


class UserFormCharField(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text='ФИО не более 15 символов')


class UserFormChoiceField(forms.Form):
    ling = forms.ChoiceField(label="Выберите язык",
                             choices=((1, "Английский"),
                                      (2, "Немецкий"),
                                      (3, "Французский")))


class UserFormDateField(forms.Form):
    date = forms.DateField(label="Введите дату")


class UserFormDateTimeField(forms.Form):
    date_time = forms.DateTimeField(label="Введите дату и время")


class UserFormDecimalField(forms.Form):
    num = forms.DecimalField(label="Введите десятичное число", decimal_places=2)


class UserFormDurationField(forms.Form):
    time_delta = forms.DurationField(label="Введите промежуток времени")


class UserFormEmailField(forms.Form):
    email = forms.EmailField(label="Введите email", help_text="Обязательный символ - @")


class UserFormFileField(forms.Form):
    file = forms.FileField(label="Файл")


class UserFormFilePathField(forms.Form):
    file_path = forms.FilePathField(label="Выберите файл", path="C:/GIT/", allow_files="True", allow_folders="True")


class UserFormFloatField(forms.Form):
    num = forms.FloatField(label="Введите число")


class UserFormGenericIPAddressField(forms.Form):
    ip_address = forms.GenericIPAddressField(label="IP адрес", help_text="Пример формы 192.0.2.0")


class UserFormImageField(forms.Form):
    img_file = forms.ImageField(label="Изображение")


class UserFormIntegerField(forms.Form):
    num = forms.IntegerField(label="Введите целое число")


class UserFormJsonFiled(forms.Form):
    J_file = forms.JSONField(label="Данные формата JSON")


class UserFormMultipleChoiceField(forms.Form):
    country = forms.MultipleChoiceField(label="Выберите страны",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Франция"),
                                                 (4, "Нидерланды"),
                                                 (5, "Россия")))


class UserFormNullBooleanField(forms.Form):
    vyb = forms.NullBooleanField(label="Вы поедите в Сочи этим Летом?")


class UserFormRegexField(forms.Form):
    reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")


class UserFormSlugField(forms.Form):
    slug_text = forms.SlugField(label="Введите текст")


class UserFormTimeField(forms.Form):
    time = forms.TimeField(label="Введите время")


class UserFormTypedChoiceField(forms.Form):
    city = forms.TypedChoiceField(label="Выберите город",
                                  empty_value=None,
                                  choices=((1, "Москва"),
                                           (2, "Санкт-Петербург"),
                                           (3, "Воронеж"),
                                           (4, "Владивосток"),
                                           (5, "Сочи")))


class UserFormTypedMultipleChoiceField(forms.Form):
    city = forms.TypedMultipleChoiceField(label="Выберите город",
                                          empty_value=None,
                                          choices=((1, "Москва"),
                                                   (2, "Санкт-Петербург"),
                                                   (3, "Воронеж"),
                                                   (4, "Владивосток"),
                                                   (5, "Сочи")))


class UserFormURLField(forms.Form):
    url = forms.URLField(label="Введите URL", help_text="Например https://ya.ru/")


class UserFormUUIDField(forms.Form):
    uuid_text = forms.UUIDField(label="Введите UUID", help_text="Формат хххххххх-хххх-хххх-хххх-ххххххххххх")


class UserFormComboField(forms.Form):
    combo_text = forms.ComboField(label="Введите данные",
                                  fields=[
                                      forms.CharField(max_length=20),
                                      forms.EmailField()])


class UserFormMultiValueField(forms.Form):
    combo_text = forms.MultiValueField(label="Комплексное поле",
                                       fields=(
                                           forms.CharField(max_length=20),
                                           forms.EmailField()))


class UserFormSplitDateTimeField(forms.Form):
    date_time = forms.SplitDateTimeField(label="Введите дату и время")


class NameForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
