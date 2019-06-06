from django.urls import path, include
from .views import *
from rest_framework import routers

router =routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigm', ParadigmView)
router.register('programmer', ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]
