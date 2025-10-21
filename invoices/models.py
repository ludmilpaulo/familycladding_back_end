from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
import uuid

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]
    
    invoice_number = models.CharField(max_length=50, unique=True)
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField()
    client_address = models.TextField()
    client_phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Invoice details
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    # Financial details
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)  # 15% VAT
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Additional fields
    notes = models.TextField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.client_name}"
    
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Generate unique invoice number
            self.invoice_number = f"FC-{timezone.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8].upper()}"
        
        # Calculate tax and total
        self.tax_amount = (self.subtotal * self.tax_rate) / 100
        self.total_amount = self.subtotal + self.tax_amount
        
        super().save(*args, **kwargs)
    
    def send_invoice_email(self):
        """Send invoice to client via email"""
        subject = f"Invoice {self.invoice_number} - Family Cladding"
        
        message = f"""
Dear {self.client_name},

Please find attached your invoice for services provided by Family Cladding.

Invoice Details:
- Invoice Number: {self.invoice_number}
- Issue Date: {self.issue_date}
- Due Date: {self.due_date}
- Total Amount: R{self.total_amount}

Payment Terms: {self.terms_conditions or 'Payment due within 30 days'}

If you have any questions regarding this invoice, please don't hesitate to contact us.

Best regards,
Family Cladding Team
        """
        
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [self.client_email],
                fail_silently=False,
            )
            self.status = 'sent'
            self.sent_at = timezone.now()
            self.save()
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.description} - {self.quantity} x R{self.unit_price}"
