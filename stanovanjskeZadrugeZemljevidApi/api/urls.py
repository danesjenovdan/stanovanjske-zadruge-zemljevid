from django.urls import path
from .views import MapView, MessageView

urlpatterns = [
    path('map/', MapView.as_view()),
    path('message/', MessageView.as_view()),
]
