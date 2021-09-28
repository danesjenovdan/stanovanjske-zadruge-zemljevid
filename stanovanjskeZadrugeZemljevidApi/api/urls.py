from django.urls import path
from .views import MapView, MessageView, TokenView

urlpatterns = [
    path('map/', MapView.as_view()),
    path('message/', MessageView.as_view()),
    path('token/', TokenView.as_view()),
]
