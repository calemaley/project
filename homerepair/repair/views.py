from django.shortcuts import render,redirect
from .models import Service, ServiceProvider, Booking, Review
from .forms import ServiceForm,ProviderForm, BookingForm, ReviewForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
# in django views, define what will be displayed on a webpage. Those views are created in a function
def homepage(request):
    return render(request, 'dashboard/homepage.html')

def index(request):
    item_count = Service.objects.all().count()
    provider_count = ServiceProvider.objects.all().count()
    booking_count = Booking.objects.all().count()
    review_count = Review.objects.all().count()
    bookings = Booking.objects.all()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form=BookingForm()
    context = {
        'item_count':item_count,
        'provider_count':provider_count,
        'booking_count':booking_count,
        'review_count':review_count,
        'form':form,
        'bookings':bookings,
    }
    return render(request,'dashboard/dashboard.html',context)

# function for adding a service 
def servicemanage(request):
     items = Service.objects.all()
     if request.method=="POST":
        form= ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            category_name = form.cleaned_data.get('category')#gets the name from the form so and stores in variable duty_name
            messages.success(request, f'Duty for {category_name} has been added')
            return redirect('dashboard-servicemanage')
     else:
        form = ServiceForm()
     context = {
         'form':form,
         'items':items,
     }
     return render(request, 'dashboard/servicemanagement.html',context)
#function to delete service
def service_delete(request, pk):
    item = Service.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-servicemanage')
    context = {
        'item':item
    }
    return render(request, 'dashboard/servicedelete.html',context)

#function to update the service
def service_update(request, pk):
    item=Service.objects.get(id=pk)
    if request.method=="POST":
        form = ServiceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-servicemanage')
    else:
        form = ServiceForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/serviceupdate.html',context)

#function for adding a service provider
def serviceprovider(request):
    providers = ServiceProvider.objects.all()
    if request.method=='POST':
        form=ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-serviceprovider')
    else:
        form=ProviderForm()
    context= {
        'form':form,
        'providers':providers
    }
    return render(request,'dashboard/serviceprovider.html', context)

#function for seeing booked a services
def booking(request):
    bookings = Booking.objects.all()
    context= {
        'bookings':bookings
    }
    return render(request, 'dashboard/bookinglist.html',context)
#function for viewing the customer page 
def customerpage(request):
    bookings = Booking.objects.all()
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-customer')
    else:
        form=BookingForm()
    context= {
        'form':form,
        'bookings':bookings,
    }
    return render(request, 'dashboard/customer.html',context)
#function for adding a review
def review(request):
    reviews = Review.objects.all()
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-customer')
    else:
        form=ReviewForm()
    context= {
        'form':form,
        'reviews':reviews,
    }
    return render(request, 'dashboard/review.html', context)

    #function for showing reviews

def reviewlist(request):
    reviews = Review.objects.all()
    context={
        'reviews':reviews
    }
    return render(request,'dashboard/reviewmanage.html',context)

# logout function
def logout_user(request):
    logout(request)
    return render(request,'user/logout.html')