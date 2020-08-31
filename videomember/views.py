from django.shortcuts import render, redirect
from .models import Course, Content
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.
def index(request):
	courses = Course.objects.all()
	return render(request, 'videomember/index.html', {'courses': courses})

def loginUser(request):
	form = loginForm
	return render(request, 'videomember/login.html', {'form': form})
	
def logoutUser(request):
	logout(request)
	return redirect('videomember:index')

def UserAccess(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request, user)
		return redirect('videomember:index')
	else:
		messages.warning(request, 'Wrong username or password')
		return redirect('videomember:login')

@login_required(login_url = '/login')
def detail(request, id):
	course = Course.objects.get(id=id)
	lessons = Content.objects.filter(course = course)

	return render(request, 'videomember/detail.html', {'lessons': lessons})

@login_required(login_url = '/login')
def lesson(request, id):
	lesson = Content.objects.get(id=id)
	return render(request, 'videomember/lesson.html', {'lesson': lesson})
