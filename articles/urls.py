from django.urls import path
from .views import ArticlesListView, ArticleDetailView, CreateArticleView, ArticleDeleteView, ArticleUpdateView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='articles_list'),
    path('article/<pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('changes/', CreateArticleView.as_view(), name='articles_changes'),
    path('delete/<pk>/', ArticleDeleteView.as_view(), name='articles_delete'),
    path('changes/<pk>/', ArticleUpdateView.as_view(), name='article_update'),

]