from django.shortcuts import render
from .models import *
# Create your views here.
from django.views.generic import View

class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self, request):
        self.views['categories'] = Category.objects.all()
        self.views['subcategories'] =Subcategory.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['products'] = Product.objects.filter(stock = 'In Stock')
        self.views['sale_products'] = Product.objects.filter(labels ='sale', stock = 'In Stock')
        self.views['new_products'] = Product.objects.filter(labels ='new', stock = 'In Stock')
        self.views['hot_products'] = Product.objects.filter(labels ='hot', stock = 'In Stock')
        return render(request, 'shop-index.html', self.views)