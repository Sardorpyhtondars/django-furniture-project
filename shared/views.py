from django.shortcuts import render

def home_page_view(request):
    return render(request, 'shared/home.html')

def about_us_view(request):
    return render(request, 'shared/about-us.html')

def account_view(request):
    return render(request, 'shared/account.html')

def blog_detail_view(request):
    return render(request, 'shared/blog-detail.html')

def blogs_list_view(request):
    return render(request, 'shared/blogs-list.html')

def cart_view(request):
    return render(request, 'shared/cart.html')

def checkout_view(request):
    return render(request, 'shared/checkout.html')

def contact_view(request):
    return render(request, 'shared/contact.html')

def login_view(request):
    return render(request, 'shared/login.html')

def product_detail_view(request):
    return render(request, 'shared/product-detail.html')

def products_list_view(request):
    return render(request, 'shared/products-list.html')

def register_view(request):
    return render(request, 'shared/register.html')

def reset_password_view(request):
    return render(request, 'shared/reset-password.html')

def wishlist_view(request):
    return render(request, 'shared/wishlist.html')

def page_404_view(request, exception):
    return render(request, 'shared/404.html', status=404)