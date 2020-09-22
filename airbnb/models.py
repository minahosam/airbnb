from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
smoking_avability=[('smoke','smoke'),('not smoke','not smoke')]
single_double=[('single','single'),('double','double')]
class airbnb(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=200)
    owner_mail=models.EmailField()
    house_photos=models.ImageField(upload_to='post/')
    house_state=models.BooleanField(default=True)
    arrival_date=models.DateField(default=date.today)
    departure_date=models.DateField(default=date.today)
    duration=models.DurationField()
    SMOKING_CHOICES=models.CharField(max_length=20,choices=smoking_avability)
    ROOM_STATUES=models.CharField(max_length=20,choices=single_double)