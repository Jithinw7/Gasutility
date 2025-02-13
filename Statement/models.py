from django.db import models

# Create your models here.

class Customer(models.Model):
    name =models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name
    

class ServiceRequest(models.Model):
    SERVICE_TYPE =[
        ('GAS_LEAK', 'Gas Leak'),
        ('METER_ISSUE', 'Meter Issue'),
        ('BILLING', 'Billing Issue'),
        ('OTHER', 'Other'),
    ]


    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=23, choices=SERVICE_TYPE)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachment/', blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    submitted_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.request_type} - {self.status}"