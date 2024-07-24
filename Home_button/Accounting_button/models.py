from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Менеджер пользователей для создания обычных пользователей и суперпользователей
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# Кастомная модель пользователя
class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('owner', 'Собственник'),
        ('organizer', 'Организатор'),
        ('executor', 'Исполнитель'),
    )

    email = models.EmailField(unique=True)  # Уникальный email для каждого пользователя
    first_name = models.CharField(max_length=30, blank=True)  # Имя пользователя
    last_name = models.CharField(max_length=30, blank=True)  # Фамилия пользователя
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)  # Тип пользователя
    is_staff = models.BooleanField(default=False)  # Статус персонала
    is_active = models.BooleanField(default=True)  # Статус активности пользователя
    date_joined = models.DateTimeField(auto_now_add=True)  # Дата регистрации

    objects = CustomUserManager()  # Использование кастомного менеджера пользователей

    USERNAME_FIELD = 'email'  # Поле для аутентификации
    REQUIRED_FIELDS = []  # Дополнительные обязательные поля

    def __str__(self):
        return self.email  # Возвращение email в качестве строкового представления пользователя


from django.db import models

# Модель для хранения информации о должностях исполнителей
class ExecutorPosition(models.Model):
    # Поле для названия должности
    position = models.CharField(max_length=255, verbose_name="Должность")
    # Поле для комментариев к должности
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)

    # Метод для представления объекта модели в виде строки
    def __str__(self):
        return self.position

    # Мета-информация о модели
    class Meta:
        # Человекочитаемое название модели в единственном числе
        verbose_name = "Должность исполнителя"
        # Человекочитаемое название модели во множественном числе
        verbose_name_plural = "Должности исполнителей"
