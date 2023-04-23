from django.urls import path, include
from .views import (
    MyModelListApiView,
)

urlpatterns = [
    path('api', MyModelListApiView.as_view()),
]