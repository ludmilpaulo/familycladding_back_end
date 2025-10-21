from django.urls import path
from .views import (
    InvoiceListCreateAPIView, 
    InvoiceRetrieveUpdateDestroyAPIView,
    send_invoice,
    mark_paid
)

urlpatterns = [
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-retrieve-update-destroy'),
    path('invoices/<int:pk>/send/', send_invoice, name='invoice-send'),
    path('invoices/<int:pk>/mark-paid/', mark_paid, name='invoice-mark-paid'),
]
