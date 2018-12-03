from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Класс для формы регистрации
class CustomUserFormRegistration(forms.Form):
    username = forms.CharField(label='Введите логин', min_length=5, max_length=150)
    email = forms.EmailField(label='Введите адрес электронной почты')
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите введенный пароль', widget=forms.PasswordInput)

    # Возвращаем имя пользователя, которое проверено на валидность
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        result = User.objects.filter(username=username)
        if result.count():
            raise ValidationError('Введенный вами логин уже занят другим пользователям. Введите другой логин.')
        return username

    # Возвращаем уже проверенный e-mail адрес
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        result = User.objects.filter(email=email)
        if result.count():
            raise ValidationError('Пользователь с таким e-mail уже зарегистрирован')
        return email

    # Возвращаем пароль, если введенные пароли равны, иначе - ошибка
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if (password1 and password2) and (password1 != password2):
            raise ValidationError('Введенные вами пароли не совпадают')
        return password2

    # Метод сохранения пользователя
    def save(self, comit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user