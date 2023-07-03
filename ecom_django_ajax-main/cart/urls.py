from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = 'store'),
    path('cart', views.cart, name = 'cart'),
    path('checkout', views.checkout, name = 'checkout'),
    path('updatecart', views.updateCart),
    path('updatequantity', views.updateQuantity),
    path('payment', views.payment, name = 'payment'),
      path('credit/<int:order_id>', views.credit, name='credit'),
      path('createorder', views.createorder, name='createorder'),
      path('savetransaction', views.savetransaction, name='savetransaction'),

      
      path('api/products', views.product_detail, name='product_detail'),
]