
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'Accounting_button/templates/login.html', {'form': form})
