from rest_framework import serializers
from .models import Photo, Album


class PhotosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'title', 'albumId', 'width', 'height', 'color', 'image', 'url']


class PhotosAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'albumId', 'url']
