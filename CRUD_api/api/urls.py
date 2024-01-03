from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='list-view'),
    path('product-list/', views.showall, name='showall'),
    path('product-detail/<str:pk>/', views.detailview, name='detailview'),
    path('product-create/', views.productcreate),
    path('product-update/<str:pk>/', views.productupdate),
    path('product-delete/<str:pk>/', views.productdelete),
]
