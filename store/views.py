from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet

from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import DetailView,ListView,DeleteView,CreateView,View
from . import models


class ItemList(ListView):
	model = models.Listing
	ordering = None
	paginate_by = 50
	template_name = 'store/itemList.html'
	context_object_name = 'products'
	
	def get_queryset(self) -> QuerySet[Any]:
		now = timezone.now()

		querySet = self.model.objects.filter(
			Status=0,
			Item__isnull=False,
			Stock__gt=0,
			# Item__Type__in=self.request.GET.getlist("type"),
			# Item__Rarity__in=self.request.GET.getlist("rarity"),
			# Type=self.request.GET.get("listing"),
			# Expiration__gt=now 
		)

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		
		return querySet
	
	def get_ordering(self) -> Sequence[str]:
		if "low" in self.request.GET:
			return ["Price",]
		if "high" in self.request.GET:
			return ["-Price",]
		if "new" in self.request.GET:
			return ["-Listing",]
		if "ending" in self.request.GET:
			return ["Expiration",]
		if "lowrarity" in self.request.GET:
			return ["Item__Rarity",]
		if "highrarity" in self.request.GET:
			return ["-Item__Rarity",]
		return []

class Product(DetailView):
	model=models.Listing
	template_name='store/product.html'
	context_object_name='product'

def cart(request:HttpRequest):
	return render(request,"store/cart.html",{})

class Wishlist(ListView):
	model=models.Wishlist
	template_name='store/wishlist.html'
	context_object_name='wishlist'

	def get_queryset(self) -> QuerySet[Any]:
		querySet = self.model.objects.filter(User=self.request.user)

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		return querySet

class AddToWishList(View):
	def post(self,request:HttpRequest,itemId):
		wish,created = models.Wishlist.objects.get_or_create(
			User=request.user,
			Item=get_object_or_404(models.Item),
		)
		if created:
			return HttpResponse("Added to Wishlist")
		return HttpResponse("Already in Wishlist")

class RemoveFromWishList(View):
	def post(self,request:HttpRequest,wishId):
		wish = get_object_or_404(models.Wishlist,id=wishId)
		wish.delete()
		return redirect("store:Wishlist")


def addToCart(request:HttpRequest,productId:int):
	return HttpResponse("Working on it!")

def removeFromCart(request:HttpRequest,productId:int):
	return HttpResponse("Working on it!")

def checkout(request:HttpRequest):
	return HttpResponse("Working on it!")

def addToWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!")

def removeFromWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!") 