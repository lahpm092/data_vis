from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('flare.csv', views.csv_data, name='csv_data'),
	path('json_data', views.json_data, name='json_data'),
	path('radial_tree', views.radial_tree, name='radial_tree'),
]
