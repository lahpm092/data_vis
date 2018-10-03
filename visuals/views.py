from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Clinical, Infecto
import csv
import json
from enarm_django.settings import BASE_DIR
# Create your views here.
def index(request):
	clinical_test = Clinical.objects.order_by('id')
	infecto_test = Infecto.objects.order_by('name')
	context = {'clinical_test': clinical_test,\
	'infecto_test': infecto_test}
	return render(request, 'index.html', context)

def csv_data(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment;\
	filename="flare.csv"'
	writer = csv.writer(response)
	csv_list = []
	with open('flare.csv','r') as f:
		csv_reader = csv.reader(f)
		for row in csv_reader:
			writer.writerow(row)


	return response

def json_data(request):
	with open('simulation.json') as f:
		data = json.load(f)
	return JsonResponse(data, safe=False)

def radial_tree(request):
	return render(request, 'radial_tree.html')
