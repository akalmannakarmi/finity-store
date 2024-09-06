from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Bid)
admin.site.register(models.Cart)
admin.site.register(models.Item)
admin.site.register(models.Listing)
admin.site.register(models.Wishlist)