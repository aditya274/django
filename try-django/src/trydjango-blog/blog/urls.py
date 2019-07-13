from django.urls import path
from .views import ArticleListView, article_detail_view
# article_list_view

app_name='articles'
urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<int:id>/', article_detail_view, name='article_detail')
]
