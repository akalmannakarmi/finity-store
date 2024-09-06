from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect

def index(request:HttpRequest):
	return render(request,"index.html",{})

def register(request:HttpRequest):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form = UserCreationForm()
	return render(request,"registration/register.html",{"form":form})