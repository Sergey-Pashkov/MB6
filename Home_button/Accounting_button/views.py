from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse

# Представление для обработки страницы входа
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Получаем объект пользователя из формы
            login(request, user)  # Входим в систему с полученным пользователем
            return redirect('dashboard_redirect')  # Перенаправление на представление для перенаправления
    else:
        form = AuthenticationForm()  # Пустая форма для GET-запросов
    return render(request, 'Accounting_button/registration/login.html', {'form': form})  # Отображение формы входа

# Представление для перенаправления пользователя на соответствующий дашборд
def dashboard_redirect_view(request):
    if request.user.is_authenticated:
        # Перенаправление на соответствующий дашборд в зависимости от типа пользователя
        if request.user.user_type == 'owner':
            return redirect(reverse('owner_dashboard'))
        elif request.user.user_type == 'organizer':
            return redirect(reverse('organizer_dashboard'))
        elif request.user.user_type == 'executor':
            return redirect(reverse('executor_dashboard'))
        else:
            return redirect(reverse('default_dashboard'))  # Перенаправление по умолчанию, если тип пользователя не распознан
    else:
        return redirect(reverse('login'))  # Перенаправление на страницу входа, если пользователь не аутентифицирован

# Представление для дашборда владельца
def owner_dashboard(request):
    return render(request, 'Accounting_button/dashboards/owner_dashboard.html')

# Представление для дашборда организатора
def organizer_dashboard(request):
    return render(request, 'Accounting_button/dashboards/organizer_dashboard.html')

# Представление для дашборда исполнителя
def executor_dashboard(request):
    return render(request, 'Accounting_button/dashboards/executor_dashboard.html')



