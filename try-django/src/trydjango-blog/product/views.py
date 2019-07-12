from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


def product_detail_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
    'object': obj
    }
    return render(request, "product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
    "object" : obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect(request, "product_delete.html", context)
    return render(request, "product_delete.html", context)

def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            print("\n\nAdded to database!")
        else:
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
    'object_list' : queryset
    }
    return render(request, "product_list.html", context)
