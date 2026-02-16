from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def about_us_view(request):
    return render(request, 'about-us.html')

def account_view(request):
    return render(request, 'account.html')

def blog_detail_view(request):
    return render(request, 'blog-detail.html')

def blogs_list_view(request):
    return render(request, 'blogs-list.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def product_detail_view(request):
    return render(request, 'product-detail.html')

def products_list_view(request):
    return render(request, 'products-list.html')

def register_view(request):
    return render(request, 'register.html')

def reset_password_view(request):
    return render(request, 'reset-password.html')

def wishlist_view(request):
    return render(request, 'wishlist.html')

def page_404_view(request, exception):
    return render(request, '404.html', status=404)