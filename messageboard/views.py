from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def addView(request):
	if request.method == "GET":
		m = Message(user=request.user, content=request.GET.get('content'))
		m.save()
	return redirect('/')

@login_required
def removeView(request):
	if request.method == "GET":
		m = Message.objects.get(pk=request.GET.get('pk'))
		m.delete()
	return redirect('/')

@login_required
def searchView(request):
	if request.method == "GET":
		content = request.GET.get('content')
		messages = Message.objects.raw(f"SELECT * FROM messageboard_message WHERE content LIKE '%{content}%'")
		return render(request, 'pages/search.html', {'messages': messages})
	return redirect('/')

@login_required
def homePageView(request):
	messages = Message.objects.all()
	return render(request, 'pages/index.html', {'messages': messages})

def registerView(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	email = request.POST.get('email')
	if not User.objects.filter(username=username).exists():
		User.objects.create_user(username, email, password)
	return redirect('/')