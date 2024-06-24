from django.urls import path

from .views import *

urlpatterns=[
    path('pv/',pview),
    path('hv/',hview),
    path('sv/',sview),
    path('uv/<int:pk>/',updateview),
    path('dv/<int:x>/',deleteview)
]