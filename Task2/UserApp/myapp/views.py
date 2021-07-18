#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Products

def register(request):
    if request.method == 'POST' and request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})


@login_required
def home(request):

    #user = User.objects.all()

    print(request.user)
    context = {
        'user': request.user
    }
    return render(request, 'myapp/home.html', context)


def products(request):
    if request.method == "POST" and request.POST:
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_details = Products.objects.create(product_name=product_name, product_price=product_price)

        

    products = Products.objects.all()
    for product in products:
        print("Product Details :")
        print("Products name ",product.product_name)
        print("Products name ",product.product_price)

    #return render(request, 'dashboard/profile.test.html', context)

    context = {
            'products': products,
            'user' : request.user
            
    }

    return render(request, 'myapp/products.html', context)

