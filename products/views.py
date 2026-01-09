from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from .forms import RegisterForm, ProductForm

def is_admin(user):
    return user.is_staff

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = None
    next_url = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect(next_url if next_url else 'home')
            return redirect('home')
        else:
            error = "Invalid username or password"
    return render(request, 'login.html', {'error': error})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@user_passes_test(is_admin, login_url='login')
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'product_form.html', {'form': form})

@user_passes_test(is_admin, login_url='login')
def delete_product(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')
