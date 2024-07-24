from django.urls import path
from .views import login_view, owner_dashboard, organizer_dashboard, executor_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),  # URL для страницы входа
    path('owner_dashboard/', owner_dashboard, name='owner_dashboard'),  # URL для дашборда владельца
    path('organizer_dashboard/', organizer_dashboard, name='organizer_dashboard'),  # URL для дашборда организатора
    path('executor_dashboard/', executor_dashboard, name='executor_dashboard'),  # URL для дашборда исполнителя
]

