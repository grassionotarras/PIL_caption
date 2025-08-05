from PIL import Image, ImageDraw, ImageFont
from datetime import date
from random import randint


def main():
    date_ = date.today()
    img_id = randint(10000000, 99999999)

    image = Image.open("img.avif").convert("RGBA")

    print(f"Image details: {image}")
    cap = input("What caption do you want for the image to have? ")
    font = input("What font do you want the text to be? ex: Arial, Bahnschrift ")
    size = int(input("What size do you want the caption to be? "))


    iformat = input("What format do you want your image to be in? ex: .png, .jpg, .webp ")
    if not iformat.startswith("."):
        iformat = "." + iformat

    try:
        font_obj = ImageFont.truetype(f"C:/Windows/Fonts/{font}.ttf", size)
                                       # ^^^^^^^^^^^^^^^ if you are on a different os or you don't have a fonts folder then link a different folder.
    except OSError:
        font_obj = ImageFont.load_default()

    text = cap
    draw = ImageDraw.Draw(image)
    bbox = draw.textbbox((0, 0), text, font=font_obj)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (image.width - w) // 2
    y = image.height - 240 - h // 2
    draw.text((x, y), text, fill="white", font=font_obj, stroke_width=2, stroke_fill="black")

    cap = cap.replace(" ", "-")
    cap = cap.replace(".", "")
    cap = cap.lower()

    try:
        image.convert("RGB").save(f"img-{cap}-{date_}-{img_id}{iformat}")
    except ValueError:
        print(f"You must enter a valid extension like .png or .jpg yours: {iformat}\
                you will still see the image but it will not be saved.")
        
    image.show()
    
    
if __name__ == "__main__":
    main()
    
