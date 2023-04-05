from django.urls import path

from generator import views as generator

urlpatterns = [
    path('primary-resume/<slug:hashcode>', generator.primaryResume),
]
