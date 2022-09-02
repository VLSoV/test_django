from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('paying/', views.paying, name='paying'),
]
