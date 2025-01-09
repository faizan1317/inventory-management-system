from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product),
    path('list_products/', views.list_products),
    path('add_supplier/', views.add_supplier),
    path('list_suppliers/', views.list_suppliers),
    path('add_stock_movement/', views.add_stock_movement),
    path('create_sale_order/', views.create_sale_order),
    path('update_sale_order/<int:order_id>/', views.update_sale_order),
    path('list_sale_orders/', views.list_sale_orders),
]
