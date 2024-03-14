import numpy as np
from matplotlib import pyplot as plt
from PIL import Image as im
import matplotlib.image as mpimg
def blackout(width,height):
array = np.zeros((height,width))
""" print(type(array))
array = np.reshape(array, (width, height))
print(array.shape)
print(array)
data = im.fromarray(array)
print(type(data)) """
return array.reshape(height,width)

def see_points(width,height,points):
array = np.zeros((height,width))
print(array)
#array = array.reshape(height,width)
#print(array)
for x,y in points :
if 0<=x<width and 0<=y<height:
array [x,y] = 1
print(array)
return array

#see_points(256,256, [(1,1), (45,2), (34,102)])


def see_quadrant(image_name,quadrant) :
image = mpimg.imread(image_name)
print(image)
height,width = image.shape
if quadrant == 'top_left':
center_x = width // 4
center_y = height //4
elif quadrant == 'top_right':
center_x = 3 * width // 4
center_y = height // 4
elif quadrant == 'bottom_left':
center_x = width // 4
center_y = 3 * height // 4
elif quadrant == 'bottom_right':
center_x = 3 * width // 4
center_y = 3 * height // 4
else :
print("Quadrant invalide")
return
center_pixel_value = image[center_y,center_x]
print(center_pixel_value)
return int(center_pixel_value * 255)
#plt.imshow(image)
#plt.show()

#see_quadrant('an_image.png', 'top_left')


""" def see_lines(width, height, lines):
array = np.zeros((height, width))
for (x1, y1, x2, y2) in lines:
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
for x in range(min(x1, x2), max(x1, x2) + 1):
y = int(m * x + b)
if 0 <= y < height and 0 <= x < width:
array[y, x] = 1

plt.imshow(array, cmap='gray')
plt.show() """

def see_lines(width, height, lines):
image = np.zeros((height, width))
for line in lines:
i_start, j_start, i_end, j_end = line
if i_start == i_end:
image[i_start, j_start:j_end+1] = 1
elif j_start == j_end:
image[i_start:i_end+1, j_start] = 1

return image

width = 10
height = 8
lines = [(2, 3, 2, 7), (4, 1, 7, 1), (5, 2, 8, 2)]

see_lines(width, height, lines)
