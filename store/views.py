from collections.abc import Sequence
from typing import Any
from django.db.models.query import QuerySet

from django.http import HttpRequest,HttpResponse,Http404
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
			Item=get_object_or_404(models.Item,id= itemId),
		)
		if created:
			return HttpResponse("Added to Wishlist")
		return HttpResponse("Already in Wishlist")

class RemoveFromWishList(View):
	def post(self,request:HttpRequest,wishId):
		wish = get_object_or_404(models.Wishlist,id=wishId)
		wish.delete()
		return redirect("store:Wishlist")


class Cart(ListView):
	model=models.Cart
	template_name='store/cart.html'
	context_object_name='carts'

	def get_queryset(self) -> QuerySet[Any]:
		querySet = self.model.objects.filter(User=self.request.user)

		ordering = self.get_ordering()
		if ordering:
			if isinstance(ordering, str):
				ordering = (ordering,)
			queryset = queryset.order_by(*ordering)
		return querySet
	
	def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
		response_kwargs.setdefault("content_type", self.content_type)
		context['totalPrice'] = sum(cart.Listing.Price * cart.Quantity for cart in context.get(self.context_object_name))
		return self.response_class(
			request=self.request,
			template=self.get_template_names(),
			context=context,
			using=self.template_engine,
			**response_kwargs,
		)

class AddToCart(View):
	def post(self,request:HttpRequest,productId):
		cart,created = models.Cart.objects.get_or_create(
			User=request.user,
			Listing=get_object_or_404(models.Listing,id=productId),
			Quantity=request.POST.get("quantity"),
		)
		if created:
			return HttpResponse("Added to Cart")
		return HttpResponse("Already in Cart")
	
class IncrementCart(View):
	def post(self,request:HttpRequest,cartId):
		cart = get_object_or_404(models.Cart,id=cartId)
		cart.Quantity +=1
		if cart.Quantity <= cart.Listing.Stock:
			cart.save()
		return HttpResponse(cart.Quantity)

class DecrementCart(View):
	def post(self,request:HttpRequest,cartId):
		cart = get_object_or_404(models.Cart,id=cartId)
		cart.Quantity -=1
		if cart.Quantity<1:
			cart.delete()
		else:
			cart.save()
		return HttpResponse(cart.Quantity)

def checkout(request:HttpRequest):
	return HttpResponse("Working on it!")