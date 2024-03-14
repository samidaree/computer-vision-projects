import numpy as np 
from matplotlib import pyplot as plt 



height = 50
width = 50
lines = [(0,10,30,20), (20,0,30,8)]

def see_lines(height, width,lines): 
    img = np.zeros((height,width))
    for line in lines : 
        i_start, j_start, i_end, j_end = line
        e = j_end - j_start
        dj = e*2
        di = (i_end - i_start)*2
        current_i = i_start 
        current_j = j_start
        while current_j <=j_end :
            img[current_i,current_j] = 1
            current_j +=1
            e = e+di
            if e<=0 : 
                current_i-=1
                e+=dj
        #plt.imshow(img, cmap='gray')
        #plt.show()
        return img


def see_lines2(width,height,lines) : 
    for (x1,y1,x2,y2) in lines : 
        tracerSegment(x1,y1,x2,y2)
    
    plt.imshow(array, cmap='gray')
    plt.show()
    return array
def tracerSegment(x1,y1,x2,y2): 
    x1,y1, = x1, height - y1 -1
    x2, y2 = x2,height - y2 - 1
    """
    e = x2-x1 
    dx = e*2 
    dy = (y2 - y1) *2 
    """
    e = y2 - y1 
    dx = e*2
    dy = (y2-y1)*2 
    """
    while x1<=x2 : 
        array[y1,x1]=1
        x1 +=1
        e = e-dy 
        if (e<0) :
            y1+=1
            e+=dx
    """
    while x1<=x2 : 
        array[y1,x1]=1
        x1 +=1
        e = e-dy 
        if (e<0) :
            x1+=1
            e+=dx




see_lines(width, height,lines)