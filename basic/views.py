from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

def index(request:HttpRequest):
	return HttpResponse("Working on it!")

def register(request:HttpRequest):
	return HttpResponse("Working on it!")