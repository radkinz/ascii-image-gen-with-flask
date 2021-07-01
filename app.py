#import modules for setting up the flask app
from flask import Flask, render_template, Response, flash, send_file, request, redirect, url_for
from werkzeug.utils import secure_filename

#import modules needed to create the ascii image
from PIL import Image, ImageFont, ImageDraw
import math
import io

# Create a flask app
app = Flask( 
  __name__,
  template_folder='templates',
  static_folder='static'
)

#constants for handling files
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

#constants for ascii code
ONE_CHAR_WIDTH = 8
ONE_CHAR_HEIGHT = 18

#setup home page
@app.route('/')
def index():
  return render_template('index.html')

#handle post request from clicking the upload button
@app.route('/', methods = ['POST'])
def data():
  #get form data from other inputs like scale factor
  form_data = request.form

  #set scale factors from user input
  Scale_Factor_Width = eval(form_data['ScaleFactorWidth'])
  Scale_Factor_Height = eval(form_data['ScaleFactorHeight'])
  Char_Arr = list(form_data['CharArray'])
  Interval = len(Char_Arr)/256

  #set return type
  if eval(form_data["ReturnType"]) == 1:
     output_file_type_is_image = True
  else:
     output_file_type_is_image = False

  #get uploaded img
  file = request.files['pic']

  #get img type and see if the type is allowed
  file_type = '.' in file.filename and file.filename.rsplit('.', 1)[1].lower()
  if file and file_type in ALLOWED_EXTENSIONS:
    filename = secure_filename(file.filename)
    img = Image.open(file)
  else:
    flash('Allowed image types are - png, jpg, jpeg')
    return redirect(request.url)

  #setup font
  fnt = ImageFont.truetype('arial.ttf', 15)

  #resize uploaded image
  width, height = img.size
  img = img.resize((int(width*(ONE_CHAR_WIDTH/ONE_CHAR_HEIGHT)*Scale_Factor_Width), int(height*(ONE_CHAR_WIDTH/ONE_CHAR_HEIGHT)*Scale_Factor_Height)), Image.NEAREST)
  width, height = img.size

  #load image pixels
  pix = img.load()

  output_file = open("Output.txt", "w")

  #create output image and set up ImageDraw method to draw the ascii chars over the output Img
  outputImage = Image.new('RGB', (ONE_CHAR_WIDTH*width, ONE_CHAR_HEIGHT*height), color = (0, 0, 0))
  d = ImageDraw.Draw(outputImage)

  #loop through user image and avg out the pixels to get the greyscale pixel value
  for y in range(height):
    for x in range(width):
      #sometimes image pixels have r,g,b,a values and sometimes its just r,g,b values
      #take the above into consideration and then extract the pixel color
      if len(pix[x,y]) == 4:
        r, g, b, a = pix[x,y]
      else: 
        r, g, b = pix[x,y]
      avg = math.floor(r/3 + g/3 + b/3)
      
      #get the output ascii character based off the pixel's greyscale value
      output_char = Char_Arr[math.floor(avg*Interval)]
      output_file.write(Char_Arr[math.floor(avg*Interval)])

      #draw the output character ontop of the output img
      d.text((x*ONE_CHAR_WIDTH, y*ONE_CHAR_HEIGHT), output_char, font=fnt, fill=(r, g, b))
    output_file.write("\n")

  if output_file_type_is_image:
    #save and return output image and display to user
    outputImage.save('output.png')
    return send_file("output.png")
  else:
    #save and return text file
    output_file.close()
    return send_file("Output.txt")


