from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'realstate/listings.html', context)


def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'realstate/listing.html', context)


def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')
    context = {
    'form': form
    }
    return render(request, 'realstate/listing_create.html', context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing')
    context = {
    'form': form
    }
    return render(request, 'realstate/listing_update.html', context)
    
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('listing')
