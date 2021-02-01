from django.shortcuts import render
from django.http import HttpResponse

import csv

from .forms import CsvModelForm
from .models import Csv

from country.models import Country

# Create your views here.

def upload_file_view(request):
	form = CsvModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = CsvModelForm()
		obj = Csv.objects.get(activated=False)
		with open(obj.file_name.path, 'r') as f:
			reader = csv.reader(f)
			for i, row in enumerate(reader):
				if i==0:
					pass
				else:
					Country.objects.create(
						country_name = row[1],
						nick_name = row[2],
						description_name = row[3]
					)
			obj.activated = True
			obj.save()

	return render(request, 'csvs/upload.html', {'form': form})
