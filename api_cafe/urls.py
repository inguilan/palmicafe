from django.urls import path
from .views import CategoriaListCreate, ProductoListCreate, ProductoRetrieveUpdateDestroy, CategoriaRetrieveUpdateDestroy

urlpatterns = [
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroy.as_view(), name='categoria-retrieve-update-destroy'),
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-retrieve-update-destroy'),
]
