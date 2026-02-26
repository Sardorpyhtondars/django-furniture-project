from django.contrib import messages
from django.shortcuts import render
from users.forms import RegisterForm, LoginForm
from users.models import User


def register_view(request):
    if request.method == "GET":
        return render(request, 'users/register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f'{field}: {error}')
            messages.error(request, ' | '.join(errors))
        return render(request, 'users/register.html')

def login_view(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                messages.success(request, 'Login successful!')
            else:
                messages.error(request, 'Email or password is incorrect!')
        return render(request, 'users/login.html')

def account_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please login first.')
        return render(request, 'users/login.html')
    user = User.objects.filter(id=user_id).first()
    context = {
        'user': user,
    }
    return render(request, 'users/account.html')