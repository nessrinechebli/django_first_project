from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def index(request):

    total_listings=Listing.objects.filter(is_published=True).order_by("add_date")
    paginator=Paginator(total_listings,3)
    page_number=request.GET.get('page',1)
    listings=paginator.get_page(page_number)

    context = {
        "listings": listings
    }

    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    listing=get_object_or_404(Listing,id=listing_id)
    context = {
        "listing":listing
    }
    return render(request, "listings/listing.html", context)