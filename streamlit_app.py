import streamlit as st
import imageio
import cv2

# create streamlit app that displays captures from webcam and creates gif
# from the images
def streamlit_app():
    # create a video capture object
    cap = cv2.VideoCapture(0)
    # set the width and height, and UNSUCCESSFULLY set the exposure time
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(15, 0.1)
    # create a list to store image data
    img_list = []
    # create a text to display on the streamlit app
    st.write("Press the spacebar to capture an image. Press the enter key to create a gif.")
    # create a while loop to continuously capture images from webcam
    while True:
        # read the frame from the webcam
        ret, frame = cap.read()
        # display the current frame
        st.image(frame, channels="BGR")
        # create a key variable to store the key pressed
        key = cv2.waitKey(1)
        # if the spacebar is pressed, store the image data in the list
        if key == 32:
            img_list.append(frame)
        # if the enter key is pressed, create the gif and break the loop
        elif key == 13:
            create_gif(img_list)
            break
    # release the video capture object
    cap.release()
    # close all windows
    cv2.destroyAllWindows()
    # display the gif
    st.image("gif.gif")

def create_gif(img_list):
    # create a gif from the list of images
    imageio.mimsave("gif.gif", img_list)

streamlit_app()