from django.urls import path
from users.views import register_view, login_view, account_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
]