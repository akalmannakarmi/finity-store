from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

def itemList(request:HttpRequest):
	return render(request,"store/itemList.html",{})

def product(request:HttpRequest,productId:int):
	return render(request,"store/product.html",{})

def cart(request:HttpRequest):
	return render(request,"store/cart.html",{})

def wishlist(request:HttpRequest):
	return render(request,"store/wishlist.html",{})


def addToCart(request:HttpRequest,productId:int):
	return HttpResponse("Working on it!")

def removeFromCart(request:HttpRequest,productId:int):
	return HttpResponse("Working on it!")

def addToWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!")

def removeFromWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!") 