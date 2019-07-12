from django.urls import path
from .views import article_detail_view, article_list_view

app_name='articles'
urlpatterns = [
    path('', article_list_view, name='article_list'),
    path('<int:id>/', article_detail_view, name='article_detail')
]
