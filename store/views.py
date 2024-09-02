from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

def itemList(request:HttpRequest):
	return HttpResponse("Working On it!")

def product(request:HttpRequest,productId:int):
	return HttpResponse("Working On it!")

def cart(request:HttpRequest):
	return HttpResponse("Working On it!")

def wishlist(request:HttpRequest):
	return HttpResponse("Working On it!")


def addToCart(request:HttpRequest,productId:int):
	return HttpResponse("Working On it!")

def removeFromCart(request:HttpRequest,productId:int):
	return HttpResponse("Working On it!")

def addToWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working On it!")

def removeFromWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working On it!") 