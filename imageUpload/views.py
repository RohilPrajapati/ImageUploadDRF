from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
import os
from datetime import datetime


class ImageUploadView(APIView):
    def get(self,request,format=None):
        image = Image.objects.all();
        serializer = ImageSerializer(image,many=True)
        return Response(serializer.data )
    def post(self,request,format=None):
        serializer = ImageSerializer(data= request.data)
        # print(serializer.file)
        if serializer.is_valid(raise_exception=True):
            if(serializer.validated_data['image'].size > 307200):
                response = {
                    'message':'image size cant me more then 300KB'
                }
                return Response(response,status=status.HTTP_406_NOT_ACCEPTABLE)
            name = serializer.validated_data['image'].name
            file_name, ext = os.path.splitext(name)
            now = datetime.now()
            date_time = now.strftime("%Y%m%d%H%M%S")
            custom_file_name = "CN"+date_time+ext
            serializer.validated_data['image'].name = custom_file_name
            serializer.save()
            image = request.data.get('image')
            return Response({
                'message':'data has been save',
                'data':serializer.data,
            }, status= status.HTTP_200_OK)