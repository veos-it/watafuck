from django.urls import path
from . import views

urlpatterns = [
    path('partners/', views.getPartners, name="partners"),
    path('advantages/', views.getAdvantages, name="advantages"),
]