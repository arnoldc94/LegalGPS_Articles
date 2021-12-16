from django.urls import path
from .views import ( 
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    HomePageView,
    CategoryView,
    
    
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('articles', ArticleListView.as_view(), 
    name="article_list"),

    path('detail/<int:pk>/', 
    ArticleDetailView.as_view(), name='article_detail'),

    path('new/', 
    ArticleCreateView.as_view(), name='article_new'),

    path('<int:pk>/edit/',
    ArticleUpdateView.as_view(), name='article_edit'),

    path('<int:pk>/delete/',
    ArticleDeleteView.as_view(), name='article_delete'),

    path('list/',
    ArticleListView.as_view(), name='article_list'),

    path('category/<str:cats>/', CategoryView, name = 'category')

]