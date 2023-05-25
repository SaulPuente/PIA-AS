from django.urls import path
#now import the views.py file into this code
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('etiqueta/',views.test.as_view()),
]