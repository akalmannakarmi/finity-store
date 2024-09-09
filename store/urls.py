from django.urls import path
from . import views

app_name='store'

urlpatterns = [
	path("itemList",views.ItemList.as_view(),name="Item List"),
	path("product/<int:pk>",views.Product.as_view(),name="Product"),
	path("cart",views.cart,name="Cart"),
	path("wishlist",views.wishlist,name="Wishlist"),

	path("addToCart/<int:productId>",views.addToCart,name="Add to Cart"),
	path("removeFromCart/<int:productId>",views.removeFromCart,name="Remove From Cart"),
	path("checkout",views.checkout,name="checkout"),
	path("addToWishlist/<int:itemId>",views.addToWishlist,name="Add to Wishlist"),
	path("removeFromWishlist/<int:itemId>",views.removeFromWishlist,name="Remove From Wishlist"),
]