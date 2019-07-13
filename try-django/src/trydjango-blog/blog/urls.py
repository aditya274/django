from django.urls import path
# article_list_view
from .views import ArticleCreateView, ArticleListView, ArticleDetailView

app_name='articles'
urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name='article_create')
]
