from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    cat_image = models.ImageField(upload_to="CategoryImages", null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories' 


class Carousel(models.Model):
    offer = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="CarouselImages")

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name_plural = 'Carousel Items'


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    gst_id = models.CharField(max_length=15)
    aadhar_number = models.CharField(max_length=12)

    class Meta:
        verbose_name_plural = 'Seller'

    def __str__(self):
        val = f"{self.user} (GST: {self.gst_id})"
        return str(val)


class Electronic(models.Model):
    type_choice = [
        ('Audio', 'Audio'),
        ('Cameras', 'Cameras'),
        ('Laptops', 'Laptops'),
        ('Monitors', 'Monitors'),
        ('Tablets', 'Tablets'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="ElectronicImages")
    image2 = models.ImageField(upload_to="ElectronicImages")
    image3 = models.ImageField(upload_to="ElectronicImages")

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Electronics'


class Fashion(models.Model):
    type_choice = [
        ('T-Shirts', 'T-Shirts'),
        ('Shirts', 'Shirts'),
        ('Casual Shoes', 'Casual Shoes'),
        ('Formal Shoes', 'Formal Shoes'),
        ('Jeans', 'Jeans'),
        ('Trousers', 'Trousers'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, null=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="FashionImages")
    image2 = models.ImageField(upload_to="FashionImages")
    image3 = models.ImageField(upload_to="FashionImages")

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Fashion'


class HomeDecor(models.Model):
    type_choice = [
        ('Bedsheets', 'Bedsheets'),
        ('Clocks', 'Clocks'),
        ('Lights', 'Lights'),
        ('Paintings & Posters', 'Paintings & Posters'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="HomeDecorImages")
    image2 = models.ImageField(upload_to="HomeDecorImages")
    image3 = models.ImageField(upload_to="HomeDecorImages")

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Home Decor'


class Mobile(models.Model):
    type_choice = [
        ('Android', 'Android'),
        ('ios', 'ios'),
        ('Symbian', 'Symbian'),
        ('Windows', 'Windows'),
    ]

    prod_name = models.CharField(max_length=400)
    type = models.CharField(max_length=40, choices=type_choice)
    price = models.BigIntegerField()
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, blank=True)
    slug = models.SlugField(default="", db_index=True, null=True)
    seller_name = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    in_stock = models.IntegerField()
    info = models.TextField(null=True)
    image1 = models.ImageField(upload_to="MobileImages")
    image2 = models.ImageField(upload_to="MobileImages")
    image3 = models.ImageField(upload_to="MobileImages")

    def __str__(self):
        return self.prod_name

    class Meta:
        verbose_name_plural = 'Category Mobiles'
