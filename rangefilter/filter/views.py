from django.shortcuts import render
from .models import Apartment 
from .filters import ApartmentFilter

# Views for filtering the list of apartments
def apartfilter(request):
	apartment_list = Apartment.objects.all()
	apartment_filter = ApartmentFilter(request.GET, queryset=apartment_list)
	return render(request, 'apartmentapp_filter.html',{'filter':apartment_filter})


