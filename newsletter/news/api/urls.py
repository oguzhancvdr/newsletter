from django.urls import path
from news.api import views as api_views


# route begins with api that we created settings.py
urlpatterns = [
  # our api will looks like /api/articles/
  # class based views
  path('authors/', api_views.ReporterListCreateView.as_view(), name="author-list"),
  path('articles/', api_views.ArticleListCreateView.as_view(), name="article-list"),
  path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name="article-detail"),
  # function based views
  # path('articles/', api_views.article_list_create_api_view, name="article-list"),
  # path('articles/<int:pk>', api_views.article_detail_api_view, name="article-detail"),
]