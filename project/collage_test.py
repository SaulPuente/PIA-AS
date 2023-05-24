from PIL import Image, ImageEnhance

new = Image.new("RGBA", (2000,2000))

img = Image.open("/Users/sypr/Desktop/Captura de pantalla 2023-05-24 a la(s) 12.19.55.png")
img = img.resize((500,500))

new.paste(img, (0,0))
new.paste(img, (1000,0))
new.paste(img, (500,500))
new.paste(img, (1500,500))
new.paste(img, (0,1000))
new.paste(img, (1000,1000))
new.paste(img, (500,1500))
new.paste(img, (1500,1500))

new.show()

new.save("/Users/sypr/Desktop/collage.png")