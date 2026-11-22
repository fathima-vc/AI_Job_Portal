
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm


def register_view(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Your account was created successfully!'
            )

            return redirect('home')

        else:
            print("REGISTRATION ERRORS:", form.errors)

    else:
        form = CustomUserCreationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(request, 'accounts/login.html')


@login_required
def home(request):

    return render(
        request,
        'accounts/home.html'
    )


def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('home')
