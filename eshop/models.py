from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Banner')
    description = models.TextField(max_length = 500 )

    class Meta:
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length= 150)
    image = models.ImageField(upload_to = 'Category')
    main_category = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'sub_category', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length = 150)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'Product')
    price = models.IntegerField()
    description = models.TextField(max_length = 5000)

    class Meta:
        verbose_name_plural = 'Products' 

    def __str__(self):
        return self.name


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username + ' \ ' + self.product.name
    

class OrderedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ManyToManyField(CartProduct)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null = True)
    total_amount = models.CharField(max_length = 150, blank=True, null=True)
    payment_method = models.CharField(max_length = 150, blank=True, null=True)
    orderedID = models.CharField(max_length = 150, blank=True, null=True)

    def __str__(self):
        return self.user.username
    



#data scraping and store database

class ScrapeProduct1(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
