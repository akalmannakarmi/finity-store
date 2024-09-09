from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import F, ExpressionWrapper, DateTimeField, DurationField

from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from . import models


class ItemList(ListView):
	model = models.Listing
	ordering = None
	paginate_by = 50
	template_name = 'store/itemList.html'
	context_object_name = 'items'
	
	def get_queryset(self) -> QuerySet[Any]:
		now = timezone.now()

		querySet = self.model.objects.filter(
			Status=0,
			Item__isnull=False,
			Stock__gt=0,
			Item__Type__in=self.request.GET.getlist("type"),
			Item__Rarity__in=self.request.GET.getlist("rarity"),
			Type=self.request.GET.get("listing"),
			Expiration__gt=now 
		)

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		
		print(querySet)
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

def checkout(request:HttpRequest):
	return HttpResponse("Working on it!")

def addToWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!")

def removeFromWishlist(request:HttpRequest,itemId:int):
	return HttpResponse("Working on it!") 