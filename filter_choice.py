import cv2


def filter_prep(val):

    # For swag filter
    if val == 1:
        fil = cv2.imread('static/swag.jpg')

        return (fil)
    
    
    if val == 2:
        fil = cv2.imread('static/3dglasses.jpg')

        return (fil)
    
    
    if val == 3:
        fil = cv2.imread('static/eyes.jpg')

        return (fil)
    
    if val == 4:
        fil = cv2.imread('static/glasses.jpg')

        return (fil)

    if val == 5:
        fil = cv2.imread('static/spiderman.jpg')

        return (fil)
    
    if val == 6:
        fil = cv2.imread('static/ironman.png')

        return (fil)
    




