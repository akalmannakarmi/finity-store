from django.urls import path
from . import views

app_name='store'

urlpatterns = [
	path("itemList",views.ItemList.as_view(),name="Item List"),
	path("product/<int:pk>",views.Product.as_view(),name="Product"),

	path("wishlist",views.Wishlist.as_view(),name="Wishlist"),
	path("addToWishlist/<int:itemId>",views.AddToWishList.as_view(),name="Add to Wishlist"),
	path("removeFromWishlist/<int:wishId>",views.RemoveFromWishList.as_view(),name="Remove From Wishlist"),

	path("cart",views.Cart.as_view(),name="Cart"),
	path("addToCart/<int:productId>",views.AddToCart.as_view(),name="Add to Cart"),

	path("incrementCart/<int:cartId>",views.IncrementCart.as_view(),name="Increment Cart"),
	path("decrementCart/<int:cartId>",views.DecrementCart.as_view(),name="Decrement Cart"),

	path("checkout",views.checkout,name="checkout"),
]