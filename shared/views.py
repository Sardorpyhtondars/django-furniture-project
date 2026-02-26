from django.contrib import messages
from django.shortcuts import render
from about.models import TeamMember
from shared.forms import ContactForm


def home_page_view(request):
    return render(request, 'shared/home.html')

def about_us_view(request):
    context = {
        'team_members': TeamMember.objects.all(),
    }
    return render(request, 'shared/about-us.html', context)

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
    if request.method == "GET":
        return render(request, 'shared/contact.html')
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            text = 'Successfully sent to the admin, thank you for your attention!'
            messages.success(request, text)
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f'{field}: {error}')

            error_text = ' | '.join(errors)
            messages.error(request, error_text)
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