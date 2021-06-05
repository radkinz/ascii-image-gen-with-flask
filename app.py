#import modules for setting up the flask app
from flask import Flask, render_template, flash, send_file, request, redirect, url_for
import os
import urllib.request
from werkzeug.utils import secure_filename

#import modules needed to create the ascii image
from PIL import Image, ImageFont, ImageDraw
import math
import io

# Create a flask app
app = Flask( 
  __name__,
  template_folder='templates'
)

app.secret_key = "secret key"

#constants for handling files
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

#constants for ascii code
CHARS = " $@B%8&WM#/\\|()1{}[]?-_+~<>!lI,\"^. "
CHAR_ARR = list(CHARS)
INTERVAl = len(CHAR_ARR)/256
SCALE_FACTOR = .40
ONE_CHAR_WIDTH = 8
ONE_CHAR_HEIGHT = 18

#make directory to access user uploaded files
os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

#function to determine what ascii character can represent each pixel
def getChar(avg_color_of_pixel):
  return CHAR_ARR[math.floor(avg_color_of_pixel*INTERVAl)]

#setup home page
@app.route('/')
def index():
  return render_template('index.html')

#handle post request from clicking the upload button
@app.route('/', methods = ['POST'])
def data():
  if 'file' not in request.files:
    flash('No file part')
    return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
     flash('No image selected for uploading')

  #get file type and see if the type is allowed
  file_type = '.' in file.filename and file.filename.rsplit('.', 1)[1].lower()
  if file and file_type in ALLOWED_EXTENSIONS:
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.instance_path, 'htmlfi', filename))
  else:
    flash('Allowed image types are - png, jpg, jpeg')
    return redirect(request.url)

  print(file)

  #ascii conversion
  output = ""
  img = Image.open(app.instance_path + "\\htmlfi\\" + filename)
  fnt = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 15)
  width, height = img.size
  img = img.resize((int(width*(ONE_CHAR_WIDTH/ONE_CHAR_HEIGHT)*SCALE_FACTOR), int(height*(ONE_CHAR_WIDTH/ONE_CHAR_HEIGHT)*SCALE_FACTOR)), Image.NEAREST)
  width, height = img.size
  pix = img.load()

  outputImage = Image.new('RGB', (ONE_CHAR_WIDTH*width, ONE_CHAR_HEIGHT*height), color = (0, 0, 0))
  d = ImageDraw.Draw(outputImage)

  for y in range(height):
    for x in range(width):
      if len(pix[x,y]) == 4:
        r, g, b, a = pix[x,y]
      else: 
        r, g, b = pix[x,y]
      avg = math.floor(r/3 + g/3 + b/3)
      pix[x, y]  =  (avg, avg, avg)
      output += getChar(avg)
      d.text((x*ONE_CHAR_WIDTH, y*ONE_CHAR_HEIGHT), getChar(avg), font=fnt, fill=(r, g, b))
    output += "\n"

  file_object = io.BytesIO()
    
  outputImage.save(file_object, 'PNG')
  file_object.seek(0)

  return send_file(file_object, mimetype='image/PNG')

if __name__ == "__main__":
    app.run()