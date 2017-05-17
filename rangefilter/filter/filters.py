from .models import Apartment 

# django_filters is a third party library 
import django_filters

#class for filtering the list of apartments according to the fields in model
class ApartmentFilter(django_filters.FilterSet):
	location = django_filters.CharFilter(lookup_expr='icontains')
	rent__lt = django_filters.NumberFilter(name='rent',lookup_expr='lt')
	rent__gt=django_filters.NumberFilter(name='rent',lookup_expr='gt')

	class Meta:
		model = Apartment 
		fields = ['apartment_type','internet','rent']






