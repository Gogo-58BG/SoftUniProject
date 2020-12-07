from django.urls import path

from app.views.index import index
from app.views.traxxas import create_traxxas

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_traxxas, name='create traxxas'),
    # path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    # path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    # path('details/<int:pk>/', details_recipe, name='details recipe'),
)