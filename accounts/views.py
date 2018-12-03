from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Форма для регистрации пользователя
from .forms import CustomUserFormRegistration
# Create your views here.


# Регистрация пользователей в системе
def signup_view(request):
    # Получены ли данные методом POST
    if request.method == 'POST':
        form = CustomUserFormRegistration(request.POST)
        # Проверка данных на валидность
        if form.is_valid():
            # Если данные валидны, сохраняем форму
            user = form.save()
            # Авторизуем пользователя на сайте
            login(request, user)
            # Редирект на страницу, где находятся посты
            return redirect('posts:list')
    else:
        # Если данные не отправлены, просто создаем экземпляр формы
        form = CustomUserFormRegistration()

    return render(request, 'signup.html', {'form': form})


# Выход пользователей из системы
def logout_view(request):
    # Проверяем отправку формы
    if request.method == 'POST':
        logout(request)
        # Перенаправляем пользователя
        return redirect('posts:list')


# Авторизация в системе
def login_view(request):
    # Проверяем, отправлены ли данные
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Получаем экземпляр пользователя
            user = form.get_user()
            # Передаем управление встроенному методу login для авторизации пользователя
            login(request, user)
            # Нужно ли перенаправлять пользователя на url, содержащийся в параметре next
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # Если параметр next не задан, перенаправляем пользователя на страницу с постами
                return redirect('posts:list')
    else:
        # Если форма еще не отправлена
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})