from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('format', views.format_code, name='format'),
    path('execute', views.execute_code, name='execute'),
] 