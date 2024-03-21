import cv2
import cvzone
import pickle

# width and height for the rectangle
width,height=107,48

try:
    # rb-readbinary , Opens the file in binary mode for reading
    with open('CarParkPos', 'rb') as f:
        # Whatever in file f save it to variable
        pos=pickle.load(f)
except:
    # Create an empty list
    pos=[]

def mouseclick(events,x,y,flags,params):
    # To check if the user click left button
    if events==cv2.EVENT_LBUTTONDOWN:
        # add the position of x and y in list 'pos'
        pos.append((x,y))

    # To check if the user click right button
    if events == cv2.EVENT_RBUTTONDOWN:
        # To iterate over inder and value
        for i, position in enumerate(pos):
            # Assigning the position of x,y in new variable
            x1,y1=position
            # The user click in between of the rectangle
            if x1<x<x1+width and y1<y<y1+height:
                # Delete the rectangle
                pos.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(pos,f)
while True:
    # Saving the image in the variable using cv2.imread method
    img = cv2.imread('carParkImg.png')

    for position in pos:
        # Creating a rectangle where user click left button
        cv2.rectangle(img,position,(position[0]+width,position[1]+height),(255,0,255),2)# (255,0,255) is defining the colour of rectangle,2 defines border width of rectangle

    # Open the save image
    cv2.imshow("Image",img)
    # To detect the mouse click
    cv2.setMouseCallback("Image",mouseclick)
    #  Waits for a key event for 1 millisecond. It allows the program to display the image and respond to user interaction
    cv2.waitKey(1)