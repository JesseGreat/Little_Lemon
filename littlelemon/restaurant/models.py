from django.db import models
from datetime import datetime

# Create your models here.

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(default=datetime.now)
    
    # Convert No_of_guests to a string before concatenating
    def __str__(self):
        return f"{self.Name} - Guests: {str(self.No_of_guests)} - Date: {self.BookingDate}"

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} - price: {str(self.price)} - inventory: {self.inventory}"

    