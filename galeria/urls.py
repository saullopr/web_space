from django.urls import path
from galeria.views import index
"""create a list to keep all the addresses (endpoints) of our application related to the gallery, 
with the urlpatterns command, inside which we will create a list with [].
"""
urlpatterns = [path('', index)]
