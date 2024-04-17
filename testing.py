from PIL import ImageGrab
import win32gui
import pytesseract
import time

def get_image(name):
    def enum_cb(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            results.append((hwnd, win32gui.GetWindowText(hwnd)))
    
    winlist = []
    win32gui.EnumWindows(enum_cb, winlist)
    ascwin = None
    for hwnd, title in winlist:
        if title == name:
            ascwin = hwnd, title
            break

    if ascwin:
        id = ascwin[0]
        prev = win32gui.GetForegroundWindow()

        win32gui.SetForegroundWindow(id)
        bbox = win32gui.GetWindowRect(id)
        img = ImageGrab.grab(bbox)
        return img, id
    else:
        return None, None
    


def continuously_read_window(img):
    while True:
        if img:
            text = pytesseract.image_to_string(img)
            print(text)
        else:
            print("Window not found.")
        
        time.sleep(1)

# Specify the exact window title or part of it
_, id = get_image('Ascension')
bbox = win32gui.GetWindowRect(id)
img = ImageGrab.grab((1185, 825, 1700, 1000))
continuously_read_window(img)