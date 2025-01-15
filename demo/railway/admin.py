from django.contrib import admin
from .models import ClassTypes,Station,Train_data,Passenger
# Register your models here.
admin.site.register(ClassTypes)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_name', 'train_number', 'source', 'destination', 'departure_time', 'arrival_time')

admin.site.register(Station)

admin.site.register(Train_data)

admin.site.register(Passenger)