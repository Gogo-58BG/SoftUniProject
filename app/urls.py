from django.urls import path

from app.views.index import index
from app.views.traxxas import create_traxxas, details_traxxas, edit_traxxas, delete_traxxas

print(f'{details_traxxas}')
urlpatterns = (
    path('', index, name='index'),
    path('create/', create_traxxas, name='create traxxas'),
    path('details/<int:pk>/', details_traxxas, name='details traxxas'),
    path('edit/<int:pk>/', edit_traxxas, name='edit traxxas'),
    path('delete/<int:pk>/', delete_traxxas, name='delete traxxas'),

)