from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import HomePage, Product
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView 
from .forms import ProductForm

def shop(request):
    product_list = Product.objects.all()
    template = loader.get_template('home/shop.html')
    context={
        'product_list': product_list
    }
    return render(request, 'home/shop.html', context)

class ShopIndexClassView(ListView):
    model = Product
    template_name = 'home/shopAdmin.html'
    context_object_name = 'product_list'

# class ProductDetail(DetailView):
#     model = Product
#     template_name = 'home/detail.html'

class CreateProduct(CreateView):
    model = Product
    fields = ['sku', 'short_description', 'price', 'image']
    template_name = 'home/product-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

