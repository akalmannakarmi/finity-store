from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
	RARITY_CHOICES = [
		(0,"Common"),
		(1,"Uncommon"),
		(2,"Rare"),
		(3,"Epic"),
		(4,"Legendary"),
	]
	TYPE_CHOICES = [
		(0,"Helmet"),
		(1,"Chestplate"),
		(2,"Leggings"),
		(3,"Boots"),
		(4,"Sword"),
		(5,"Staff"),
		(6,"Bow"),
	]

	Name = models.CharField(unique=True,max_length=100)
	Description = models.TextField(null=True)
	Details = models.TextField(null=True)
	Rarity = models.PositiveSmallIntegerField(choices=RARITY_CHOICES)
	Type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
	Image = models.ImageField(upload_to="images/items")


class Listing(models.Model):
	TYPE_CHOICES = [
		(0,"Store"),
		(1,"Auction"),
		(2,"BIN"),
	]
	STATUS_CHOICES = [
		(0,"Available"),
		(1,"Expired"),
		(2,"Purchased"),
	]

	Type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)
	Status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
	Price = models.DecimalField(max_digits=9,decimal_places=4)
	Stock = models.PositiveIntegerField()
	Listing = models.DateTimeField()
	Expiration = models.TimeField()
	Seller = models.ForeignKey(User,related_name="Listings",null=True,on_delete=models.SET_NULL)
	Buyer = models.ForeignKey(User,related_name="Purchases",null=True,on_delete=models.SET_NULL)


class Bid(models.Model):
	Listing = models.ForeignKey(Listing,related_name="Bids",null=True,on_delete=models.SET_NULL)
	Bidder = models.ForeignKey(User,related_name="Bids",null=True,on_delete=models.SET_NULL)
	Price = models.DecimalField(max_digits=9,decimal_places=4)
	Time = models.DateTimeField()


class Wishlist(models.Model):
	User = models.ForeignKey(User,related_name="Wishlist",on_delete=models.CASCADE)
	Item = models.ForeignKey(Item,related_name="wishlist",on_delete=models.CASCADE)
	Created = models.DateTimeField()

class Cart(models.Model):
	User = models.ForeignKey(User,related_name="Cart",on_delete=models.CASCADE)
	Listing = models.ForeignKey(Listing,related_name="Cart",on_delete=models.CASCADE)
	Quantity = models.PositiveIntegerField()
