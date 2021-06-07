# Image to Ascii Generator Web App

Just started this project, and there is still a lot more to go:) 

## Progress Logs

6/6/21: Now there is an input for users to adjust the scale factor of the output image. Currently, the scale factor adjusts the source image's width and height, and I want to experiment with maybe creating different scale factors for the dimensions. For example, maybe the user wants to see an image be really wide and distorted in ascii form for comedic purposes?

6/5/21: Altered the algorithm to work for JPGs, PNGs, and JPEGs. I also added some CSS and changed the HTML layout to be more aesthetically pleasing. Next steps are to allow the user to adjust the size of the output and maybe allow the user to switch between the output being text or an image.

6/4/21: There is now a form where users can upload an image that sends a post request to generate the image to ascii and display it to the user. This relatively works but there need to be a checking system that ensures the user uploaded a valid file. I also need to slightly change the ascii generator algorithm because the algorithm will have to act differently for a PNG than a JPG. 

6/3/21: Got flask running and able to display the ascii art of a source image already loaded in the flask app files.

