from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from vacancy.models import Prof

def Search(request):
	context= {}
	query =""

	if request.GET:
		query = request.GET['q']
	tutors= get_data_queryset(query)

	return render(request,'home.html',{"professors":tutors})


def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ") 
	for q in queries:
		tutors = Prof.objects.filter(

			Q(fname__icontains=q)|
			Q(lname__icontains=q)
		)

		for tutor in tutors:
			queryset.append(tutor)
			
	return list(set(queryset))

def home(request):
	professors = Prof.objects.all()
	return render(request,'home.html',{"professors":professors})

