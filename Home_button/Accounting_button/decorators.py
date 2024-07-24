# Accounting_button/decorators.py

from django.core.exceptions import PermissionDenied

def owner_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'owner':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def organizer_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'organizer':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def executor_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'executor':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
