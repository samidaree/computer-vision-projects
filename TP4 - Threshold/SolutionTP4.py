import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def see_gaussian(seuil):
    img = (mpimg.imread("gaussian.png")*255).astype(np.uint8)[:,:,0]
    print(img)
    
    print(img.shape)
    new_image = np.zeros((img.shape[0], img.shape[1] ))
  
    aire= 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] > seuil:
                aire += 1
                new_image[i,j] = 1
    plt.imshow(new_image)
    plt.show()
    return new_image, aire, aire/(img.shape[0]*img.shape[1])

def see_shapes(obj):
    img = (mpimg.imread("shapes.png")*255).astype(np.uint8) 
    cat_img = np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    rectangle_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    oval_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    heart_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    star_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    #img_values = open("images_values.txt","w")
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            vols = img[i,j]
            #img_values.write(str(vols)+'\n')
            if (obj=='rectangle'):
                if vols[2] ==178 :
                    rectangle_img[i,j]=1
            if (obj=='cat'):
                if vols[1]==148 or vols[1]==198 : 
                    cat_img[i,j]=1
            if (obj=='heart'):
                if vols[2]==148 :
                    heart_img[i,j]=1
            if (obj=='oval'):
                if vols[0]==178 or vols[0]==198 : 
                    oval_img[i,j]=1
            if (obj=='star'):
                if vols[1]==178 or vols[1]==198 : 
                    star_img[i,j]=1
    plt.imshow(cat_img)
    plt.show()

see_shapes('cat')