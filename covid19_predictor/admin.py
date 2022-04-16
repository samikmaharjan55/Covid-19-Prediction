from django.contrib import admin
from .models import CovidSymptoms
# Register your models here.

@admin.register(CovidSymptoms)
class CovidSymptomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cough', 'fever', 'breath', 'age', 'environment', 'hypertension', 'diabetes', 'cardiovascular', 'respiratory', 'immune',)
