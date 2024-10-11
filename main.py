import imageio.v3 as iio
import matplotlib.pyplot as plt
import time 
import numpy as np

print('code running')
starttime = time.time()
ascii = '$@B%8&Wm#*oahkbdpqwmZOQLCJUYXzcvrj+=-:. '

# load an image
image = iio.imread('C:/Users/oja37/OneDrive - University of Bath/year 4/python/ascii art/lowq.jpg')

shapeoftheimage = image.shape
imageheight = shapeoftheimage[0]
imagewidth = shapeoftheimage[1]

#now i will iterate through every pixel and get its pixel brightness
#by taking hte RGB values and using the luminance formula

#make an array to store data in
pixelvalues = np.zeros((imageheight,imagewidth))
ascii_image = np.zeros((imageheight,imagewidth))

#print(len(pixelvalues))
#print(len(pixelvalues[0]))
countx = 0 #my iterator
county = 0 #y iterator

masterpiece = ''
redchannel = shapeoftheimage[2]

points = len(ascii)
#print(image.shape)
#currently no checking that the image is rgb possible error
for row in pixelvalues:
    countx = 0;
    for item in row:
        #pixel to brightness
        r = image[county,countx, 0]#redchannel
        g = image[county,countx, 1]#green
        b = image[county,countx, 2]#blue
        pixelvalues[county,countx] = (0.299 * r) + (0.587 * g) + (0.114 * b)
        
        ascii_image[county,countx] = ( pixelvalues[county,countx] / 255 )  * (points -1)
        print(countx)

        countx = countx+ 1


   #increment counters
    county = county+ 1

countx = 0 #my iterator
county = 0 #y iterator

for row in ascii_image:
    countx = 0
    for item in row:
        masterpiece += ascii[int(ascii_image[county,countx])]
        countx = countx + 1
    masterpiece += '/n'
    county = county+ 1 
#print('no. of pixels')
#printing into a txtfile is better than cmd line
with open('estherino.txt', 'w') as file:
    file.write(masterpiece)

print('code done')
END = time.time();
elapsed = END - starttime
print("elapsed time:" , elapsed, "seconds")
#print('seconds')
#print(masterpiece)
  

#plt.imshow(image)
#plt.axis('off')
#plt.show()

