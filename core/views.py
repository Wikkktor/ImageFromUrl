from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Photo
from rest_framework.response import Response
from .serializers import PhotosListSerializer, PhotosAddSerializer


class ListCreatePhotoItem(generics.ListCreateAPIView):
    model = Photo

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PhotosAddSerializer
        return PhotosListSerializer

    def get_queryset(self):
        return Photo.objects.all()

    def create(self, request, *args, **kwargs):
        photo_data = request.data

        photo = Photo.objects.create(
            title=photo_data['title'],
            albumId_id=photo_data['albumId'],
            url=photo_data['url'] if photo_data['url'] else None
        )

        response = {
            'success': 'You managed to add photo',
            'Attributes': {
                'Heigth': f'{photo.height}px',
                'Width': f'{photo.width}px',
                'Dominant Color': photo.color
            }
        }
        return Response(response, status=status.HTTP_202_ACCEPTED)


class GetUpdateDeletePhotoItem(generics.RetrieveUpdateDestroyAPIView):
    model = Photo
    serializer_class = PhotosAddSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Photo.objects.all()

    def update(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs['id'])
        photo_data = request.data

        photo.title = photo_data['title']
        photo.albumId_id = photo_data['albumId']
        photo.url = photo_data['url']
        photo.save()
        return Response(status=status.HTTP_202_ACCEPTED)


# @api_view(('GET',))
# def import_images_api(request):
#     response = requests.get('https://jsonplaceholder.typicode.com/photos')
#     if response.status_code == 200:
#         json_response = response.json()
#         for x in range(1, 5):
#             Photo.objects.create(
#                 title=json_response[x]['title'],
#                 albumId_id=json_response[x]['albumId'],
#                 url=json_response[x]['url']
#             )
#     return Response(status=status.HTTP_202_ACCEPTED)

