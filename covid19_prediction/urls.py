from django.contrib import admin
from django.urls import path
from covid19_predictor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.symptoms_db),
]