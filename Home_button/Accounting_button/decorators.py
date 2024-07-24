from django.core.exceptions import PermissionDenied

# Декоратор для проверки, что пользователь является владельцем (owner)
def owner_required(function):
    def wrap(request, *args, **kwargs):
        # Проверка, что пользователь аутентифицирован и его тип - 'owner'
        if request.user.is_authenticated and request.user.user_type == 'owner':
            # Если проверка успешна, вызываем оригинальную функцию
            return function(request, *args, **kwargs)
        else:
            # Иначе вызываем исключение PermissionDenied
            raise PermissionDenied
    # Копируем документацию и имя оригинальной функции
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

# Декоратор для проверки, что пользователь является организатором (organizer)
def organizer_required(function):
    def wrap(request, *args, **kwargs):
        # Проверка, что пользователь аутентифицирован и его тип - 'organizer'
        if request.user.is_authenticated and request.user.user_type == 'organizer':
            # Если проверка успешна, вызываем оригинальную функцию
            return function(request, *args, **kwargs)
        else:
            # Иначе вызываем исключение PermissionDenied
            raise PermissionDenied
    # Копируем документацию и имя оригинальной функции
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

# Декоратор для проверки, что пользователь является исполнителем (executor)
def executor_required(function):
    def wrap(request, *args, **kwargs):
        # Проверка, что пользователь аутентифицирован и его тип - 'executor'
        if request.user.is_authenticated and request.user.user_type == 'executor':
            # Если проверка успешна, вызываем оригинальную функцию
            return function(request, *args, **kwargs)
        else:
            # Иначе вызываем исключение PermissionDenied
            raise PermissionDenied
    # Копируем документацию и имя оригинальной функции
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
