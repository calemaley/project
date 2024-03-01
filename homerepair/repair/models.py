from django.db import models
from django.contrib.auth.models import User

REVIEWTYPE = (
    ('good','good'),
    ('bad','bad'),
)

# Create your models here.
#this classes represent how data is stored in your database

#database model for creating a service
class Service(models.Model):
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = 'Service'

    def __str__(self):
        return f'{self.category}'

 #database model for creating a service provider   
class ServiceProvider(models.Model):
    name = models.CharField(max_length=20)
    specialization = models.ForeignKey(Service, on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'ServiceProvider'

    def __str__(self):
        return f'{self.name}-{self.specialization}'

   #database model for creating a booking  
class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

#database model for creating a review
class Review(models.Model):
    type = models.CharField(max_length=20, choices=REVIEWTYPE)
    brief_description = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    


