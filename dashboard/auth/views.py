from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.user.is_authenticated:
        if request.user.superuser:
            return redirect('list_page')
        else:
            return redirect('login')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_staff:
                login(request, user)
                return redirect('list_page')
            else:
                error = "Sizda bu sahifaga kirish uchun ruxsat yo'q!"
        else:
            error = "Foydalanuvchi nomi yoki Parol xato!"

    return render(request, 'auth/login.html', {'error': error})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

