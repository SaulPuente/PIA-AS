from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
    path('etiqueta/',views.test.as_view(), name="tag_maker"),
]