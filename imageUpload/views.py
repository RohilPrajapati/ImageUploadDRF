from rest_framework.views import APIView
from .models import Image
from django.http import request
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.parsers import FormParser,MultiPartParser,JSONParser
from rest_framework import status


class ImageUploadView(APIView):
    # parser_classes = [MultiPartParser]
    def post(self,request,format=None):
        serializer = ImageSerializer(data= request.data)
        # print(serializer.file)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            serializer.save()
            image = request.data.get('image')
            return Response({
                'message':'data has been save',
                'data':serializer.data,
            }, status= status.HTTP_200_OK)