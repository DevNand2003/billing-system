from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Bill
from .forms import BillForm, SearchForm

def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save()  # The total_amount is calculated in the model's save()
            
            # Prepare email content
            subject = f"Your Bill Invoice #{bill.invoice_number}"
            message = (
                f"Dear Customer,\n\n"
                f"Thank you for using our services. Here are your bill details:\n\n"
                f"Invoice Number: {bill.invoice_number}\n"
                f"Company: {bill.company}\n"
                f"Rent per Day: {bill.rent_per_day}\n"
                f"Start Date: {bill.start_date}\n"
                f"End Date: {bill.end_date}\n"
                f"Discount: {bill.discount}\n"
                f"GST (%): {bill.gst}\n"
                f"Due: {bill.due}\n"
                f"Total Amount: {bill.total_amount}\n\n"
                f"Regards,\nYour Company"
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [bill.email])
            
            return render(request, 'billing/bill_detail.html', {'bill': bill})
    else:
        form = BillForm()
    return render(request, 'billing/bill_form.html', {'form': form})

def search_bill(request):
    bill = None
    error = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            invoice_number = form.cleaned_data['invoice_number']
            try:
                bill = Bill.objects.get(invoice_number=invoice_number)
            except Bill.DoesNotExist:
                error = "No bill found with that invoice number."
    else:
        form = SearchForm()
    return render(request, 'billing/search_bill.html', {'form': form, 'bill': bill, 'error': error})
