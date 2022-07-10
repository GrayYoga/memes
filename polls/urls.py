from django.urls import path

from . import views
from .views import MemoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),
    path('<int:meme_id>', views.page, name='page'),
    path('like/<int:meme_id>', views.like, name='like'),
    path('skip/<int:meme_id>', views.skip, name='skip'),
    path("likest/", views.tops_list, name='likest'),
    path("points20/", views.points20, name='points20')
]
