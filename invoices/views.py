from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
from django.utils import timezone
from .models import Invoice, InvoiceItem
from .serializers import InvoiceSerializer, InvoiceCreateSerializer

class InvoiceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = InvoiceCreateSerializer
    
    def get_queryset(self):
        cache_key = 'invoice_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Invoice.objects.prefetch_related('items').all().order_by('-created_at')
            cache.set(cache_key, queryset, 300)  # Cache for 5 minutes
        return queryset

class InvoiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.prefetch_related('items')
    serializer_class = InvoiceSerializer

@api_view(['POST'])
def send_invoice(request, pk):
    """Send invoice to client via email"""
    try:
        invoice = Invoice.objects.get(pk=pk)
        success = invoice.send_invoice_email()
        
        if success:
            return Response({'message': 'Invoice sent successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Failed to send invoice'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Invoice.DoesNotExist:
        return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def mark_paid(request, pk):
    """Mark invoice as paid"""
    try:
        invoice = Invoice.objects.get(pk=pk)
        invoice.status = 'paid'
        invoice.paid_at = timezone.now()
        invoice.save()
        
        # Clear cache
        cache.delete('invoice_list')
        
        return Response({'message': 'Invoice marked as paid'}, status=status.HTTP_200_OK)
    except Invoice.DoesNotExist:
        return Response({'error': 'Invoice not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
