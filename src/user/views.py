from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, '¡Registro exitoso! Ahora estás logueado.')
                return redirect('user:profile')
            except Exception as e:
                messages.error(request, f'Ocurrió un error inesperado: {str(e)}')
        else:
            messages.error(request, 'Error en el registro. Por favor, revisa los campos.')
    else:
        form = RegisterForm()
    
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, "user/profile.html")