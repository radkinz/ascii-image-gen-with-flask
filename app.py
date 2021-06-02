from flask import Flask
app = Flask(__name__)

#ascii code
from PIL import Image

import math

#possible characters
chars = " $@B%8&WM#/\\|()1{}[]?-_+~<>!lI,\"^. "
charArray = list(chars)
charlen =  len(charArray)
interval = charlen/256

#constants
scaleFactor = 1
oneCharWidth = 8
oneCharHeight = 10

def getChar(inputInt):
  return charArray[math.floor(inputInt*interval)]

@app.route('/')
def index():
    output = ""
    img = Image.open("oikawa.png")
    width, height = img.size
    new_height = 150
    new_width  = new_height * width / height
    img = img.resize((int(new_width*(oneCharWidth/oneCharHeight)), int(new_height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = img.size
    pix = img.load()

    print(pix[0,0])

    for y in range(height):
      for x in range(width):
        r, g, b, a = pix[x,y]
        avg = math.floor(r/3 + g/3 + b/3)
        pix[x, y]  =  (avg, avg, avg)
        output += getChar(avg)
      output += "\n"
    return "<p>" + output + "</p>"

if __name__ == "__main__":
    app.run()