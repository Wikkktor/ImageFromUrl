from django.urls import path
from .views import GetUpdateDeletePhotoItem, ListCreatePhotoItem #, import_images_api


urlpatterns = [
    path('photos/', ListCreatePhotoItem.as_view(), name='photo'),
    path('photos/<int:id>', GetUpdateDeletePhotoItem.as_view(), name='photo'),
    # path('photos/api/', import_images_api, name='photos_api')
]
