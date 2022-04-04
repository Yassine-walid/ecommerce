from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='Home'),
    path('products/',views.ProductList.as_view(),name='Products')
]