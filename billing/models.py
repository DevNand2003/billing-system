from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

COMPANY_CHOICES = [
    ('Company A', 'Company A'),
    ('Company B', 'Company B'),
    ('Company C', 'Company C'),
]

class Bill(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100, choices=COMPANY_CHOICES)
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    start_date = models.DateField()
    end_date = models.DateField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.00'))])
    gst = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text="Enter GST percentage", validators=[MinValueValidator(Decimal('0.00'))])
    due = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.00'))])
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Calculate number of days (inclusive)
        duration = (self.end_date - self.start_date).days + 1
        rental_cost = self.rent_per_day * duration
        sub_total = rental_cost - self.discount
        gst_amount = (self.gst / Decimal('100.00')) * sub_total
        self.total_amount = sub_total + gst_amount + self.due
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.company}"
