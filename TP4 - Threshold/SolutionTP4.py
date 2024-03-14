import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def see_gaussian(seuil):
    img = (mpimg.imread("gaussian.png")*255).astype(np.uint8)[:,:,2]
    print(img)
    
    print(img.shape)
    new_image = np.zeros((img.shape[0], img.shape[1] ))
  
    aire= 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] > seuil:
                aire += 1
                new_image[i,j] = 255
    plt.imshow(new_image)
    plt.show()
    return new_image, aire, aire/(img.shape[0]*img.shape[1])

see_gaussian(100)