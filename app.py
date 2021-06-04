from flask import Flask,render_template,send_file

app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
#  static_folder='static'  # Name of directory for static files
)

#ascii code
from PIL import Image, ImageFont, ImageDraw

import math
import io

#possible characters
chars = " $@B%8&WM#/\\|()1{}[]?-_+~<>!lI,\"^. "
charArray = list(chars)
charlen =  len(charArray)
interval = charlen/256

#constants
scaleFactor = 0.25
oneCharWidth = 8
oneCharHeight = 18

def getChar(inputInt):
  return charArray[math.floor(inputInt*interval)]

@app.route('/')
def index():
    output = ""
    img = Image.open("oikawa.png")
    fnt = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 15)
    width, height = img.size
    # new_width  = 800
    # new_height = new_width * width / height
    img = img.resize((int(width*(oneCharWidth/oneCharHeight)*scaleFactor), int(height*(oneCharWidth/oneCharHeight)*scaleFactor)), Image.NEAREST)
    width, height = img.size
    pix = img.load()

    outputImage = Image.new('RGB', (oneCharWidth*width, oneCharHeight*height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for y in range(height):
      for x in range(width):
        r, g, b, a = pix[x,y]
        avg = math.floor(r/3 + g/3 + b/3)
        pix[x, y]  =  (avg, avg, avg)
        output += getChar(avg)
        d.text((x*oneCharWidth, y*oneCharHeight), getChar(avg), font=fnt, fill=(r, g, b))
      output += "\n"

    file_object = io.BytesIO()
    
    outputImage.save(file_object, 'PNG')
    file_object.seek(0)

    return send_file(file_object, mimetype='image/PNG')

if __name__ == "__main__":
    app.run()