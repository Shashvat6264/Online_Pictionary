from django.urls import path

from . import views
urlpatterns = [
    path('paint/',views.paint),
]