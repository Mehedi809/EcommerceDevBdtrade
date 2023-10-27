from django.contrib import admin
from .models import *

# Register your models here.
all_model = [Banner, Category, Product, CartProduct, OrderedProduct, ScrapeProduct1]
admin.site.register(all_model)