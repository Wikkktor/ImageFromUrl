from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import APIException
from .models import Photo
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PhotosListSerializer, PhotosAddSerializer


# Create your views here.


class PhotosAPIView(APIView):
    serializer_class = PhotosAddSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return Photo.objects.all()

    def get(self, request, *args, **kwargs):
        photos = self.get_queryset()
        serializer = PhotosListSerializer(photos, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        photo_data = request.data

        if not photo_data['image'] and not photo_data['url']:
            raise APIException("You must pass and url to img or image")

        photo = Photo.objects.create(
            title=photo_data['title'],
            albumId_id=photo_data['albumId'],
            image=photo_data['image'] if photo_data['image'] else None,
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
        return Response(response, status=200, template_name=None, headers=None, content_type=None)
