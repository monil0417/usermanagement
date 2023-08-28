from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import User

def home_view(request):
    return render(request,'home.html')
def registration_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('login')
        else:
            error_message = "Passwords do not match."
    else:
        error_message = None

    return render(request, 'registration.html', {'error_message': error_message})
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()

        if user:
            # Implement session handling or authentication here
            return redirect('user-list')
        else:
            error_message = "Invalid email or password."
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})
def user_list_view(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def edit_user_view(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('user-list')

    return render(request, 'edit_user.html', {'user': user})


def delete_user_view(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('user-list')

    return render(request, 'delete_user.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or any other desired page