from django.urls import path
from . import views

urlpatterns = [
	path("itemList",views.itemList,name="Item List"),
	path("product/<int:productId>",views.product,name="Product"),
	path("cart",views.cart,name="Cart"),
	path("wishlist",views.wishlist,name="Wishlist"),

	path("addToCart/<int:productId>",views.addToCart,name="Add to Cart"),
	path("removeFromCart/<int:productId>",views.removeFromCart,name="Remove From Cart"),
	path("addToWishlist/<int:itemId>",views.addToWishlist,name="Add to Wishlist"),
	path("removeFromWishlist/<int:itemId>",views.removeFromWishlist,name="Remove From Wishlist"),
]