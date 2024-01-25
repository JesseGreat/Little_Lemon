from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import MenuSerialzer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerialzer



class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerialzer
    
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

