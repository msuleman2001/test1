from django.urls import path
from . import views

urlpatterns = [
    path('', views.app2_fun, name='app2_fun'),
    path('fun2', views.app2_fun2, name='app2_fun2'),
]