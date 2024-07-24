from django.contrib import admin
from django.urls import path, include
from Accounting_button.views import dashboard_redirect_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),  # URL для страницы входа
    path('accounting/', include('Accounting_button.urls')),  # Подключение URL-ов приложения Accounting_button
    path('dashboard/', dashboard_redirect_view, name='dashboard_redirect'),  # URL для перенаправления на дашборд
]
