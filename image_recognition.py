import cv2
import numpy as np
from PIL import ImageGrab
import time

# Load the template image
template = cv2.imread('template.png', 0)
w, h = template.shape[::-1]

def match_template(image, template):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    
    # Perform match operations.
    res = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
    
    # Specify a threshold
    threshold = 0.8
    
    # Store the coordinates of matched area in an array
    loc = np.where(res >= threshold)
    
    return loc

def continuously_detect_image(window_title):
    while True:
        # Capture the screen
        screen = ImageGrab.grab()
        
        # Match the template
        locations = match_template(screen, template)
        
        # If the image is detected
        if locations[0].size:
            print("Image detected on screen!")
        
        # Pause for a bit before the next screen capture
        time.sleep(1)

continuously_detect_image('Ascension')
