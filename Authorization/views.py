from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from teacherprofile.models import UserInfo
from django.contrib import messages


def authentic(request):
	return render(request, 'Authorization/auth.html', )

def register(request):
	return render(request, 'Authorization/register.html', )

def registerForm(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			first_name= request.POST['first_name']
			last_name= request.POST['last_name']
			username= request.POST['username']
			email= request.POST['email']
			user_type= request.POST['user_type']
			password1= request.POST['password1']
			password2= request.POST['password2']
			if password1==password2:
				if User.objects.filter(username=username).exists():
					messages.info(request, 'username is already taken')
					return redirect('Authorization:loginForm')
				elif User.objects.filter(email=email).exists():
					messages.info(request, 'Email is already taken')
					return redirect('Authorization:registerForm')
				else:
					user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
					user.save()
					UserInfo.objects.create(id = user.id, user_type=user_type, users_id = user.id)
					return redirect('Authorization:loginForm')
			else:
				messages.info(request, 'Password do not match')	
				return redirect('Authorization:registerForm')
		return render(request, 'Authorization/register.html')
	else:
		return redirect('vacancy:main')		

def loginForm(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			username= request.POST.get('username')
			password= request.POST.get('password1')
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('vacancy:main')
			else:
				messages.info(request, 'Invalid Credentials')
				return redirect('Authorization:loginForm')
		else:
			return render(request,'Authorization/login.html')
	else:
		return redirect('vacancy:main')

def logoutuser(request):
	auth.logout(request)
	return redirect('Authorization:loginForm')