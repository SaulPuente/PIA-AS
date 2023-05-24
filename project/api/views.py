from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from PIL import Image, ImageDraw, ImageFont

# Create your views here.
class test(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            print(request.FILES)
            with Image.open("/Users/sypr/Desktop/Captura de pantalla 2023-05-24 a la(s) 12.19.55.png") as img1:
                new = Image.new("RGBA", (2000,2000), "white")#color=(255,255,255,0))
                img1 = img1.resize((500,500))

                new.paste(img1, (500,200))
                # new.paste(img, (1000,0))
                # new.paste(img, (500,500))
                # new.paste(img, (1500,500))
                # new.paste(img, (0,1000))
                # new.paste(img, (1000,1000))
                # new.paste(img, (500,1500))
                # new.paste(img, (1500,1500))

                new.save("collage.png")

                img = Image.open('collage.png')

                # Call draw Method to add 2D graphics in an image
                I1 = ImageDraw.Draw(img)

                myFont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 65)

                bigFont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 200)

# Add Text to an image
                I1.text((10, 10), "Nice Car", font=myFont, fill =(255, 0, 0))

                I1.text((500, 500), "q onda", font=myFont, fill =(255, 255, 255))

                I1.text((500, 700), "holaaa", font=myFont, fill =(0, 0, 0))

                I1.text((0, 400), "20%", font=bigFont, fill =(0, 0, 0))

                img.save("collage.png")

                with open("collage.png", "rb") as f:
                    return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError as e:
            print("que haces aqui?")
            print(str(e))
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "png")
            return response