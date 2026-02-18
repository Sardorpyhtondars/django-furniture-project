from django.urls import path

from blogs.views import blogs_list_view

app_name = 'blogs'

urlpatterns = [
    path('blogs/', blogs_list_view, name='list'),
]