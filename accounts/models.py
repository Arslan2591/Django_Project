from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (('Indoor', 'Indoor'), ('Out Door', 'Out Door'))
    name = models.CharField(max_length=30, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=300, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (('Pending', 'Pending'), ('Out for Delivery',
                                       'Out for Delivery'), ('Delivered', 'Delivered'))

    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    tags = models.ManyToManyField(Tag)
