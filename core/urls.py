from django.urls import path
from .views import PhotosAPIView

urlpatterns = [
    path('photos', PhotosAPIView.as_view(), name='photos'),

]
