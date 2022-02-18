from django.urls import path
from .views import MapView, MessageView, TokenView, SubscribersView, SubscriberView

urlpatterns = [
    path('map/', MapView.as_view()),
    path('message/', MessageView.as_view()),
    path('token/', TokenView.as_view()),
    path('subscribers-count/', SubscribersView.as_view()),
    path('subscriber/', SubscriberView.as_view())
]
