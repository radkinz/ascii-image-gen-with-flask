# Image to Ascii Generator Web App

Just started this project, and there is still a lot more to go:) 

## Progress Logs

6/9/21: I added a switch, so the user can go back and forth between the output being a text file and the output being a png. There are also two scale factors incase the user wants to distort the image. Next steps, I want the user to be able to change the character array, which are the ascii chars that the algorithm selects from to make the art. Sometimes changing the characters of the array help the output look better, but it is all dependent on the type of image. By the user being able to change this feature, it helps the program be more efficient at meeting the user's needs and it also will help the user better understand how the ascii generator works.

6/6/21: Now there is an input for users to adjust the scale factor of the output image. Currently, the scale factor adjusts the source image's width and height, and I want to experiment with maybe creating different scale factors for the dimensions. For example, maybe the user wants to see an image be really wide and distorted in ascii form for comedic purposes?

6/5/21: Altered the algorithm to work for JPGs, PNGs, and JPEGs. I also added some CSS and changed the HTML layout to be more aesthetically pleasing. Next steps are to allow the user to adjust the size of the output and maybe allow the user to switch between the output being text or an image.

6/4/21: There is now a form where users can upload an image that sends a post request to generate the image to ascii and display it to the user. This relatively works but there need to be a checking system that ensures the user uploaded a valid file. I also need to slightly change the ascii generator algorithm because the algorithm will have to act differently for a PNG than a JPG. 

6/3/21: Got flask running and able to display the ascii art of a source image already loaded in the flask app files.

