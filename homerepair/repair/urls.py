from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('servicemanage/', views.servicemanage, name='dashboard-servicemanage'),
    path('servicedelete/<int:pk>/',views.service_delete, name='dashboard-service-delete'),
    path('serviceupdate/<int:pk>/',views.service_update, name='dashboard-service-update'),
    path('serviceprovider/',views.serviceprovider, name='dashboard-serviceprovider'),
    # path('customerpage/',views.customerpage, name='dashboard-customer'),
    path('bookings/',views.booking, name='dashboard-booking'),
    path('review/',views.review, name='dashboard-review'),
    path('reviewlist/',views.reviewlist, name='dashboard-reviewlist')
]