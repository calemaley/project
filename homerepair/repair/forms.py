from django import forms
from .models import Service, ServiceProvider, Booking, Review
 #this are the forms that are found in the system

#form for adding a service
class ServiceForm(forms.ModelForm):
    class Meta:
        model=Service
        fields=['category','description']

#form for adding a service provider
class ProviderForm(forms.ModelForm):
    class Meta:
        model=ServiceProvider
        fields=['name','specialization','email','number']

#form for booking a service
class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['service']

#form for review
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['type','brief_description']
    