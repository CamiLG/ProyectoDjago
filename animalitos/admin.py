from django.contrib import admin
from .models import Pet
from .models import Vaccine

#Implementacion de un decorador que puede ser una clase o metodo

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']

admin.site.register(Vaccine)
