from django.conf.urls import url 
from .views import apartfilter

urlpatterns = [
	url(r'^$', apartfilter, name='browse-apartment'),
	
	]