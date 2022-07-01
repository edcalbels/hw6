from django.shortcuts import render, redirect
from main.models import Product, Category, Review
from main.forms import ProductForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    dict_ = {
        'key': 'Hello World',
        'color': '#1772d4',
        'list_': ['Abylai', "Salima", "Sanjar", 'Janat']
    }
    return render(request, 'index.html', context=dict_)


def product_list_view(request):
    print(request.user)
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'product_detail': product,
                                                   'category_list': Category.objects.all(),
                                                   'reviews': Review.objects.filter(product=product)})


def category_product_filter_view(request, category_id):
    context = {
        'product_list': Product.objects.filter(category_id=category_id),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)


def add_product_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    return render(request, 'add_product.html', context={
        'form': form,
        'category_list': Category.objects.all()
    })


def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/')
    return render(request, 'register.html', context={
        'form': form
    })


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
        return redirect('/login/')
    return render(request, 'login.html', context={
        'form': form
    })
