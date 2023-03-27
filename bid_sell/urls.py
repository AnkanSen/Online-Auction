from django.urls import path,include
from . import views

urlpatterns = [
    path('bid/',views.bid,name='bid'),
    path('sell/',views.sell,name='sell'),
    path('products/<str:pk>',views.products,name='products'),
    path('bids/<str:pk>',views.bids,name='bids'),
]