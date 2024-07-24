

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='Accounting_button/registration/login.html'), name='login'),  # Указание правильного пути к шаблону
    path('accounting/', include('Accounting_button.urls')),  # Включить URL из приложения Accounting_button
]
