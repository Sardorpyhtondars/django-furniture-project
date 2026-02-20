from django.urls import path

from shared import views

app_name = 'shared'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_us_view, name='about'),
    path('account/', views.account_view, name='account'),
    path('blog/<int:id>/', views.blog_detail_view, name='blog-detail'),
    path('blogs/', views.blogs_list_view, name='list'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('product/<int:id>/', views.product_detail_view, name='product-detail'),
    path('products/', views.products_list_view, name='list'),
    path('register/', views.register_view, name='register'),
    path('reset-password/', views.reset_password_view, name='reset-password'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
]