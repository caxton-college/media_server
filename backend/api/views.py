from django.http import HttpResponse
from django.core.files.base import File

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Image

class Index(APIView):
	permission_classes = (permissions.AllowAny,)

	def get(self, request):
		return Response({"status": "API online"}, status=status.HTTP_200_OK)


class FetchRandomImage(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request):
        image = Image.objects.order_by('?').first()
        image_file = image.image.file
        response = HttpResponse(File(image_file), content_type='image/jpeg')
        return response