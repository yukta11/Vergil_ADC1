from django.shortcuts import render
from .models import prof

# Create your views here.

def profile(request):
	professor = prof.objects.all()
	return render(request, 'teacherprofile/profile.html',{"dip" : professor})

