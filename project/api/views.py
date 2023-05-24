from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from PIL import Image

# Create your views here.
class test(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            print(request.FILES)
            with open("/Users/sypr/Desktop/Captura de pantalla 2023-05-24 a la(s) 12.19.55.png", "rb") as f:
                return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "JPEG")
            return response