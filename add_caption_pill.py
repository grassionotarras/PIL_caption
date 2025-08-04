from PIL import Image, ImageDraw, ImageFont
from datetime import date
from random import randint

date_ = date.today()
img_id = randint(10000000, 99999999)
print(date_)

image = Image.open("img.avif").convert("RGBA")

print(f"Image details: {image}")
cap = input("What caption do you want for the image to have? ")
font = input("What font do you want the text to be? ex: Arial, Bahnschrift ")
size = int(input("What size do you want the caption to be? "))
iformat = input("What format do you want your image to be in? ex: .png, .jpg, .webp ")

try:
    font = ImageFont.truetype(f"C:/Windows/Fonts/{font}.ttf", size) 
except OSError:
    font = ImageFont.load_default()

text = cap
draw = ImageDraw.Draw(image)
bbox = draw.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (image.width - w) // 2
y = image.height - 240 - h // 2
draw.text((x, y), text, fill="white", font=font, stroke_width=2, stroke_fill="black")

cap = cap.replace(" ", "-")
cap = cap.replace(".", "")
cap = cap.lower()

image.convert("RGB").save(f"img-{cap}-{date_}-{img_id}{iformat}")
image.show()