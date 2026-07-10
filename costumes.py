###### Binary Files and PIL ######

##### One moe type of file that we will dicuss today is a ginary file. A binary file is simply a collection of ones and zeros. This type of file can store anything including, music and image data.
#### There is a popular Python library called PILthat works well with image files.\
### Animated GIFs are a popular type of image file that has many image files within it that are played in sequence over and over again, creating a simplistic animation or video effect.
## Imagine that we have a series of costumes, as illustrated below.

##### Before proceeding, please make sure that you have downlaoded the source code files from the course website.
#### It will not be possible for you to code the following without having the two iamges above in your possession and stored in your IDE

### In the terminal window type code costumes.py and code as follows:

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

##### Notice that we import the Image functionality from PIL. Notice that the first for loop simply loops through the images provided as command-line arguments and stores theme into the list called images.
#### The 1: starts slicing argv at its second image to it as well, creating an animated gif.
### Typing python costumes.py costume1.gif costume2.gif into the terminal. Now type code costumes.gif into the terminal window, and you can now see an animated GIF.
