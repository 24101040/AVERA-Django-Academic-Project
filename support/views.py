from django.shortcuts import render
from .models import WishlistItem

def wishlist_list(request):
    items = WishlistItem.objects.filter(is_active=True)
    return render(request, 'support/wishlist.html', {'items': items})