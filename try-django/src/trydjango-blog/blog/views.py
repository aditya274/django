from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

def article_detail_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {
    "object" : obj,
    }
    return render(request, 'article_detail.html', context)

def article_list_view(request):
    queryset = Article.objects.all()
    context = {
    'object_list' : queryset,
    }
    return render(request, 'article_list.html', context)
# Create your views here.
