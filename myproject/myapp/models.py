from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Farmer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=150, blank=True)  # Last name for identification
    contact = models.CharField(max_length=150, unique=True)  # Unique contact information
    password = models.CharField(max_length=128)  # Store hashed password
    address = models.TextField(blank=True, null=True)  # Optional address field
    created_at = models.DateTimeField(null=True)  # Timestamp for when the farmer was added

    def __str__(self):
        return f"{self.firstname} {self.lastname}"  # Full name representation

    def set_password(self, raw_password):
        """Set a hashed password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check if the raw password matches the hashed password."""
        return check_password(raw_password, self.password)

    class Meta:
        unique_together = ['contact']  # Ensure contact is unique

from django.db import models

class Agronomist(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=128, default='')  # Added password field

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    seed = models.CharField(max_length=100, null=True, blank=True)  # Name of the seed
    fertilizer = models.CharField(max_length=100, null=True, blank=True)  # Name of the fertilizer
    seedquantity = models.IntegerField(null=True, blank=True)  # Optional quantity
    fertilizerquantity = models.IntegerField(null=True, blank=True)  # Optional quantity
    planting_season = models.CharField(max_length=50)

    def __str__(self):
        seed_info = f"Seed: {self.seed} - Quantity: {self.seedquantity}" if self.seed else "No Seed"
        fertilizer_info = f"Fertilizer: {self.fertilizer} - Quantity: {self.fertilizerquantity}" if self.fertilizer else "No Fertilizer"
        return f"{seed_info}, {fertilizer_info}"


class FertilizerRequest(models.Model):
    agronomist = models.ForeignKey(Agronomist, on_delete=models.CASCADE)
    request_date = models.DateField(null=True)
    response_date = models.DateField(null=True, blank=True)
    pickup_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"Fertilizer Request by {self.agronomist} - Status: {self.status}"


class SeedRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    request_date = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.TextField(null=True, blank=True)  # New feedback field
    first_name = models.CharField(max_length=50, null=True, blank=True)  # First name field
    last_name = models.CharField(max_length=50, null=True, blank=True)   # Last name field
    email = models.EmailField(max_length=100, null=True, blank=True)     # Email field
    phone_number = models.CharField(max_length=15, null=True, blank=True) # Phone number field

    def __str__(self):
        return f"Seed Request by {self.first_name} {self.last_name} on {self.request_date} - Status: {self.status}"