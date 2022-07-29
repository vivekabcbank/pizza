from django.urls import path
from .views import *


urlpatterns = [
    path("",HellOrderhView.as_view(),name="hello_order"),
    path('orders/', OrderView.as_view(), name='orders'),
    path('order/<int:order_id>/', OrderIdView.as_view(), name='order'),
    path('update-status/<int:order_id>/', UpdateOrderStatusView.as_view(), name='update_order_status'),
    path('user/<int:user_id>/orders', UserOrdersView.as_view(), name='users_orders'),
    path('user/<int:user_id>/order/<int:order_id>/', UserOrderDetailView.as_view(), name='user_order_detail'),
]
