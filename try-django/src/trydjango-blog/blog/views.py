from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
    "object" : obj,
    }
    return render(request, 'article_detail.html', context)
#
# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#     'object_list' : queryset,
#     }
#     return render(request, 'article_list.html', context)
# Create your views here.

class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all() #format = app/<modelname>_list.html
