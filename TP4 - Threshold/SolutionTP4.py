import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def see_gaussian(seuil):
    img = (mpimg.imread("gaussian.png")*255).astype(np.uint8)[:,:,0]
  
    new_image = np.zeros((img.shape[0], img.shape[1] ))
  
    aire= 0

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] > seuil:
                aire += 1
                new_image[i,j] = 1
   
    return new_image, aire, aire/(img.shape[0]*img.shape[1])

def see_shapes(obj):
    img = (mpimg.imread("shapes.png")*255).astype(np.uint8) 
    cat_img = np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    rectangle_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    oval_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    heart_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
    star_img= np.zeros((img.shape[0], img.shape[1] ),dtype=bool)
   
    for i in range (img.shape[0]):
        for j in range (img.shape[1]):
            vols = img[i,j]
        
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
    if (obj=='rectangle'):
        return rectangle_img
    if (obj=='cat'):
        return cat_img
    if (obj=='heart'):
        return heart_img
    if (obj=='oval'):
        return oval_img
    if (obj=='star'):
        return star_img
   

def get_histogram(image, bins):
    histogram = np.zeros(bins)
    
    for pixel in image:
        histogram[pixel] += 1
    
    return histogram

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

def equalize_image(img_name): 
    img = mpimg.imread(img_name)
    if len(img.shape) == 3: 
        img = np.mean(img, axis=2)  
    img = (img * 255).astype(np.uint8)
    plt.imshow(img, cmap='gray')
    plt.show()
    flat = img.flatten()
    plt.hist(flat, bins=50) 
    plt.show()

    hist = get_histogram(flat, 256)

    cs = cumsum(hist)
   
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()

    # re-normalize the cumsum
    cs = nj / N

    # cast it back to uint8 since we can't use floating point values in images
    cs = cs.astype('uint8')
    plt.plot(cs)
    plt.show()
    # get the value from cumulative sum for every index in flat, and set that as img_new
    img_new = cs[flat]

    # put array back into original shape since we flattened it
    img_new = np.reshape(img_new, img.shape)

    # set up side-by-side image display
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)

    fig.add_subplot(1,2,1)
    plt.imshow(img, cmap='gray')

    # display the new image
    fig.add_subplot(1,2,2)
    plt.imshow(img_new, cmap='gray')

    plt.show(block=True)

# Exemple d'utilisation de la fonction
img_name = "landscape.png"
equalized_image = equalize_image(img_name)
