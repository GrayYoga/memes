from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),
    path('like/<int:meme_id>', views.like, name='like'),
    path('skip/<int:meme_id>', views.skip, name='skip'),
]
