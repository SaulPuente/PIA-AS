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

            imagen = request.FILES['imagen'] 
            data = request.data
            with Image.open(imagen) as img1:
                new = Image.new("RGBA", (1000,600), "white")
                
                width, height = img1.size

                p = 220/float(height) 
                img1 = img1.resize((int(width*p), int(height*p)))

                new.paste(img1, (580,120))

                line1 = ""

                product_name = data['producto'].split()
                
                i = 0
                while i < len(product_name) and len(line1) + len(product_name[i]) < 32:
                    line1 += " " + product_name[i]
                    i += 1
                line2 = ""
                while i < len(product_name) and len(line2) + len(product_name[i]) < 32:
                    line2 += " " + product_name[i]
                    i += 1

                new.save(data['destino'] + "/etiqueta.png")

                img = Image.open(data['destino'] + "/etiqueta.png")

                # Call draw Method to add 2D graphics in an image
                I1 = ImageDraw.Draw(img)

                myFont = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 16)
                font_producto = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)

                bigFont = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 200)

                font_promo = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 70)

                I1.text((60, 35), line1, font=font_producto, fill =(0, 0, 0), stroke_width=1, stroke_fill="black")
                I1.text((60, 80), line2, font=font_producto, fill =(0, 0, 0), stroke_width=1, stroke_fill="black")

                I1.text((70, 170), "#74119", font=myFont, fill =(0, 0, 0))

                I1.text((160, 150), "Precio reg.:", font=myFont, fill =(0, 0, 0))
                I1.text((160, 170), ("$" + data['precio_regular']).center(12), font=myFont, fill =(0, 0, 0))

                I1.text((290, 150), "Precio final:", font=myFont, fill =(0, 0, 0))
                I1.text((290, 170), ("$" + data['precio_final']).center(13), font=myFont, fill =(0, 0, 0))

                I1.text((420, 150), "Ahorra:", font=myFont, fill =(0, 0, 0))
                I1.text((420, 170), ("$" + data['ahorro']).center(7), font=myFont, fill =(0, 0, 0))

                I1.text((60, 220), data['promocion'] + "%", font=bigFont, fill =(0, 0, 0), stroke_width=2, stroke_fill="black")
                I1.text((490, 340), "de descuento", font=font_promo, fill =(0, 0, 0), stroke_width=1, stroke_fill="black")

                I1.text((60, 460), "Aplica en producto seleccionado.", font=myFont, fill =(0, 0, 0))

                pdg = ""
                i = 0
                while i < len(product_name) and len(pdg) + len(product_name[i]) < 25:
                    pdg += " " + product_name[i]
                    i += 1
                I1.text((370, 500), "Vigencia " + data['vigencia'] + " - PDG: " + pdg + " - SKU: " + data['sku'], font=myFont, fill =(0, 0, 0))

                img.save(data['destino'] + "/etiqueta.png")

                with open(data['destino'] + "/etiqueta.png", "rb") as f:
                    return HttpResponse(f.read(), content_type="image/jpeg")
        except IOError as e:
            red = Image.new('RGBA', (1, 1), (255,0,0,0))
            response = HttpResponse(content_type="image/jpeg")
            red.save(response, "png")
            return response