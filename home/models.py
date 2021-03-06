from django.db import models


# Create your models here.

LABELS = (('new','new'), ('hot', 'hot'), ('sale', 'sale'),('','default'))
class Category(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)

    def __str__(self):
        return self.name






class Slider(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'media')
    rank = models.IntegerField()
    description = models.CharField(max_length=500, blank = True)
    status = models.CharField(choices = (('active', 'active'), ('','default')), blank = True, max_length = 500)
    

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'media')
    rank = models.IntegerField()
    status = models.CharField(choices = (('active', 'active'), ('','default')), blank = True, max_length = 500)


    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=400)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to = 'media')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    description = models.TextField(blank = True)
    stock = models.CharField(max_length =50, 
    choices = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')))
    labels = models.CharField(max_length = 50, choices = LABELS)

    def __str__(self):
        return self.name











