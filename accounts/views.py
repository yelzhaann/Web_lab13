from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Тіркелу
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            messages.success(request, f'Сәлем, {user.username}! Тіркелу сәтті өтті.')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


# Кіру
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Қош келдіңіз, {user.username}!')
            # ?next= параметрі болса — сол бетке жіберу
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Логин немесе пароль қате. Қайталап көріңіз.')

    return render(request, 'accounts/login.html')


# Шығу
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Жүйеден сәтті шықтыңыз.')
    return redirect('login')


# Тек авторизацияланғандарға
@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
