from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    banner = Banner.objects.all()
    mens = Product.objects.filter(category__name = 'Mens')
    womens = Product.objects.filter(category__name = 'Womens')
    kids = Product.objects.filter(category__name = 'Kids')
    wedding = Product.objects.filter(category__name = 'Wedding')

    paginator = Paginator(mens, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'banner' : banner,
        'mens' : mens,
        'womens' : womens,
        'kids' : kids,
        'wedding' : wedding,
        'page_obj': page_obj
    }
    return render(request, 'store/index.html', context)


def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form,
    }
    return render(request, 'store/registraion.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product
    }
    return render(request, 'store/product-detail.html', context)
    

from django.contrib import messages
from django.shortcuts import get_object_or_404

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product, created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    order_qs = OrderedProduct.objects.filter(user=request.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.cart_product.filter(product__pk=product.pk).exists():
            cart_product.quantity += 1
            cart_product.save()
            messages.info(request, 'This product quantity updated')
            return redirect('product_detail',pk=pk)
        else:
            order.cart_product.add(cart_product)
            messages.success(request, 'This product was add to cart')
            return redirect('product_detail',pk=pk)
    else:
        order = OrderedProduct.objects.create(user=request.user)
        order.cart_product.add(cart_product)
        messages.success(request, 'This product was add to cart')
        return redirect('product_detail',pk=pk)
    return redirect('product_detail',pk=pk)


def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = OrderedProduct.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.cart_product.filter(product__pk = product.pk).exists():
            cartproduct = CartProduct.objects.filter(user=request.user, ordered = False, product__pk = product.pk)[0]
            cartproduct.delete()
            messages.success(request, 'This product remove from cart')
            return redirect('product_detail', pk=pk)
        else:
            messages.info(request, 'This product was not your cart')
            return redirect('product_detail', pk=pk)
        
    else:
        messages.info(request, 'This product was not your cart')
        return redirect('product_detail', pk=pk)
    return redirect('product_detail', pk=pk)



#Web scrapping

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def show(request):
    # all_data = ScrapeProduct1.objects.all()
    # all_data_dict = {'data':all_data}
    return render(request,'store/scrape/data.html')


def add(request):
    if (request.method == "POST"):
        url = request.POST.get('w_url')
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        t_count = request.POST.get('t_count')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        title_list = []
        for product in range(1,int(t_count)+1):
            loop_div = x1+"["+str(product)+"]"+x2
            print(loop_div)
            x_path = loop_div
            title = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, x_path)))
            title_list.append(title.text)
            product = ScrapeProduct1(title=title.text)
            product.save()
        # time.sleep(50)
        print(title_list)
        all_data = ScrapeProduct1.objects.all()
        context = {
            'data':all_data,
            }

        return render(request, 'store/scrape/scrape_data.html', context)
    else:
        return HttpResponse('This is not a post method')