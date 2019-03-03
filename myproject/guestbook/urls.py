from django.urls import path
from .views import index, sign

urlpatterns = [
    path('',index, name='index'),
    path('sign/', sign, name='sign')
]
