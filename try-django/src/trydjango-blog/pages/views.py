from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World</h1>")
    print(request.user)
    return render(request, "home.html", {})  #can pass context via {}

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    my_context = {
    'my_text':'This is about us',
    'my_number':123,
    'this_is_true': True,
    'my_list': [123, 234, 345, 456, 'tomato']
    }
    return render(request, 'about.html', my_context)
