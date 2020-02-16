from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Tutors
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def getTutors(request,page,size):
	if request.method == 'GET':
		skip = size * (page - 1)
		tutors = Tutors.objects.all()[skip:(page * size)]
		dict = {
			"tutors": list(tutors.values())
		}
		return JsonResponse(dict)
	else:
		return JsonResponse({"Status":"Error"})

@csrf_exempt
def deleteTutors(request,id):
	if request.method == 'DELETE' and Tutors.objects.filter(id=id).exists():
		tutor = Tutors.objects.get(id=id)
		tutor.delete()
		return JsonResponse({"Status":"Successfully deleted"})
	else:
		return JsonResponse({"Status":"Error"})

@csrf_exempt
def updateTutors(request,id):
	if request.method == 'PUT' and Tutors.objects.filter(id=id).exists() and request.body:
		decoded_data = request.body.decode('utf-8')
		data = json.loads(decoded_data)
		tutor = Tutors.objects.get(id=id)
		tutor.tutor_name = data['name']
		tutor.tutor_location = data['location']
		tutor.save()
		tutor = Tutors.objects.filter(pk=id)
		return JsonResponse({"tutor":list(tutor.values())})
	else:
		return JsonResponse({"Status":"Error","required":["name","location"]})

@csrf_exempt
def addTutors(request):
	if request.method == 'POST':
		try:
			decoded_data = request.body.decode('utf-8')
			data = json.loads(decoded_data)
			name = data['name']
			des = data['location']
			tutor = Tutors.objects.create(tutor_name =name , tutor_location=des)
			tutor = Tutors.objects.filter(id = tutor.pk)
			#successful
			return JsonResponse({"tutor":list(tutor.values())})
		except Exception as ex:
			print(ex)
			return JsonResponse({"Status":"Internal server error"})
	else:
		return JsonResponse({"Status":"Error","required":["name","location"]})
		