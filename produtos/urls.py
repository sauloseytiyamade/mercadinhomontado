from django.urls import path
from .views import produtos_list
from .views import produtos_create
from .views import produtos_update
from .views import produtos_delete
from .views import mylogout

urlpatterns = [
    path('list', produtos_list, name='produtos_list'),
    path('create', produtos_create, name='produtos_create'),
    path('update/<int:id>', produtos_update, name='produtos_update'),
    path('delete/<int:id>', produtos_delete, name='produtos_delete'),
    path('logout', mylogout, name='mylogout'),
]
