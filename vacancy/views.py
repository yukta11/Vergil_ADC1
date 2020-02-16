from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render,redirect
from .models import Prof
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# Create your views here.

@login_required(login_url="/login/")
def vacancyform(request):
	
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		date_of_birth = request.POST['date_of_birth']
		qualifications = request.POST['qualification']
		experience = request.POST['experience']
		salary = request.POST['salary']
		image = request.FILES.get('image')

		professor = Prof.objects.create(fname=fname, lname=lname, date_of_birth=date_of_birth, qualifications=qualifications, experience=experience, salary=salary, image=image)
		return redirect("vacancy:main")

	else:
		return render(request, 'vacancy/vacancyform.html')

def main(request):
	return render(request,'main.html')

def home(request):
	professors = Prof.objects.all()
	return render(request,'home.html',{"professors":professors})

@login_required
def updateprofile(request,id):
	prof = Prof.objects.get(id=id)
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		date_of_birth = request.POST['date_of_birth']
		qualifications = request.POST['qualification']
		experience = request.POST['experience']
		salary = request.POST['salary']


		prof.fname=fname
		prof.lname=lname
		prof.date_of_birth=date_of_birth
		prof.qualifications=qualifications
		prof.experience=experience
		prof.salary=salary
		prof.save()
		return redirect("vacancy:home")

	else:
		return render(request, 'vacancy/updateprofile.html',{"prof":prof})

def deleteprofessor(request, pk):
	if request.method == "POST":
		professor = Prof.objects.get(id=pk)
		professor.delete()
	return redirect("vacancy:home")

def book(request):
	return render(request,'book.html')
