from django.contrib import admin
from .models import Product
from .forms import RawProductForm
# Register your models here.
admin.site.register(Product)
