#imports
import cv2
import numpy as np
import mouse
import keyboard
from time import sleep
import pyautogui
from mss import mss
#variables
ttw=0.5 #0.2
# Define the threshold for detecting the template
# Adjust this threshold based on your requirement
threshold = 0.8

def capture_screenshot():
    with mss() as sct:
        # Capture the screen
        screenshot = sct.grab(sct.monitors[1])
        # Convert to a format OpenCV can work with
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        return screenshot

#functions
def clickonimage(image,middlemove=False):
    # Take a screenshot using pyautogui
    screenshot = capture_screenshot()

    # Convert the screenshot to a format OpenCV can work with

    # Load the template image
    template_image = cv2.imread(image)  # Replace with your template image path

    if template_image is None:
        raise ValueError(f"Template image at path {image} could not be loaded.")

    # Convert the screenshot and the template image to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) 

    if max_val >= threshold:
        # Get the dimensions of the template
        template_height, template_width = template_gray.shape

        # Calculate the center of the detected region
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2

        # Simulate a mouse click at the center of the detected region
        mouse.move(center_x, center_y)
        sleep(ttw)
        mouse.click()

        if middlemove:
            # Move the cursor to the middle of the screen
            screen_width, screen_height = pyautogui.size()
            middle_x, middle_y = screen_width // 2, screen_height // 2
            sleep(ttw)
            mouse.move(middle_x, middle_y)
            sleep(ttw)
    else:
        print("Template not found")

def locateimage(image,middlemove=False):
    # Take a screenshot using pyautogui
    screenshot = capture_screenshot()

    # Convert the screenshot to a format OpenCV can work with
    

    # Load the template image
    template_image = cv2.imread(image)  # Replace with your template image path

    if template_image is None:
        raise ValueError(f"Template image at path {image} could not be loaded.")

    # Convert the screenshot and the template image to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Get the dimensions of the template
        template_height, template_width = template_gray.shape

        # Calculate the center of the detected region
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2

        # Simulate a mouse click at the center of the detected region
        return {"x": center_x, "y": center_y}
        
        if middlemove:
            # Move the cursor to the middle of the screen
            screen_width, screen_height = pyautogui.size()
            middle_x, middle_y = screen_width // 2, screen_height // 2
            sleep(ttw)
            mouse.move(middle_x, middle_y)
            sleep(ttw)
    else:
        print("Template not found")

def imageexists(image):
    # Take a screenshot using pyautogui
    screenshot = capture_screenshot()

    # Convert the screenshot to a format OpenCV can work with
    

    # Load the template image
    template_image = cv2.imread(image)  # Replace with your template image path

    # Convert the screenshot and the template image to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Get the dimensions of the template
        template_height, template_width = template_gray.shape

        # Calculate the center of the detected region
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2

        return True
    else:
        return False

def craftingoutput(craft,middlemove=False):
    
    if middlemove:
        # Move the cursor to the middle of the screen
        screen_width, screen_height = pyautogui.size()
        middle_x, middle_y = screen_width // 2, screen_height // 2
        sleep(ttw)
        mouse.move(middle_x, middle_y)

    sleep(ttw)
    coords=locateimage(craft)
    x=coords["x"]
    y=coords["y"]
    mouse.move(x,y)
    sleep(ttw)
    keyboard.press('shift')
    sleep(ttw)
    mouse.click()
    sleep(ttw)
    keyboard.release('shift')

def non_max_suppression(boxes, overlapThresh):
    if len(boxes) == 0:
        return []

    if boxes.dtype.kind == "i":
        boxes = boxes.astype("float")

    pick = []

    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(y2)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    return boxes[pick].astype("int")

def locatecraft(image, click_once=False, click_multiple=False, max_clicks=None, holdshift=True,craft=False,craftimg=None):
    inventory_top_left = (700, 568)
    inventory_bottom_right = (1228, 856)
    screenshot = capture_screenshot()

    
    inventory_screenshot = screenshot[inventory_top_left[1]:inventory_bottom_right[1], inventory_top_left[0]:inventory_bottom_right[0]]

    template_image = cv2.imread(image)
    if template_image is None:
        raise ValueError(f"Template image at path {image} could not be loaded.")
    
    inventory_gray = cv2.cvtColor(inventory_screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(inventory_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        template_height, template_width = template_image.shape[:2]
        boxes = []
        for pt in zip(*loc[::-1]):
            top_left = (pt[0] + inventory_top_left[0], pt[1] + inventory_top_left[1])
            bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
            boxes.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        boxes = np.array(boxes)
        picked_boxes = non_max_suppression(boxes, overlapThresh=0.3)
        matched_coords = []

        for (startX, startY, endX, endY) in picked_boxes:
            center_x = (startX + endX) // 2
            center_y = (startY + endY) // 2
            matched_coords.append((center_x, center_y))

        if click_once:
            if len(matched_coords) > 0:
                mouse.move(matched_coords[0][0], matched_coords[0][1])
                sleep(ttw)
                if holdshift == True:
                    keyboard.press('shift')
                    sleep(ttw)
                mouse.click()
                if holdshift == True:
                    sleep(ttw)
                    keyboard.release('shift')
                if craft == True:
                    try:
                        craftingoutput(craftimg)
                    except:
                        pass

        if click_multiple:
            clicks_done = 0
            for coord in matched_coords:
                if max_clicks is not None and clicks_done >= max_clicks:
                    break
                mouse.move(coord[0], coord[1])
                sleep(ttw)
                if holdshift == True:
                    keyboard.press('shift')
                    sleep(ttw)
                mouse.click()
                if holdshift == True:
                    sleep(ttw)
                    keyboard.release('shift')
                clicks_done += 1
                if craft == True:
                    try:
                        craftingoutput(craftimg)
                    except:
                        pass
                sleep(ttw) #idk
    else:
        print("Template not found")

def clickonempty(image):
    crafting_top_left = (766, 291)
    crafting_bottom_right = (934, 458)
    screenshot = capture_screenshot()

    
    crafting_screenshot = screenshot[crafting_top_left[1]:crafting_bottom_right[1], crafting_top_left[0]:crafting_bottom_right[0]]

    template_image = cv2.imread(image)
    if template_image is None:
        raise ValueError(f"Template image at path {image} could not be loaded.")
    
    crafting_gray = cv2.cvtColor(crafting_screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(crafting_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        template_height, template_width = template_image.shape[:2]
        boxes = []
        for pt in zip(*loc[::-1]):
            top_left = (pt[0] + crafting_top_left[0], pt[1] + crafting_top_left[1])
            bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
            boxes.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        boxes = np.array(boxes)
        picked_boxes = non_max_suppression(boxes, overlapThresh=0.3)
        matched_coords = []

        for (startX, startY, endX, endY) in picked_boxes:
            center_x = (startX + endX) // 2
            center_y = (startY + endY) // 2
            matched_coords.append((center_x, center_y))

        if len(matched_coords) > 0:
            mouse.move(matched_coords[0][0], matched_coords[0][1])
            sleep(ttw)
            mouse.click()
    else:
        print("Template not found")

def locatesplit(image,max_clicks=None):
    coords=locateimage("bin/crafted.png")
    x=coords["x"]
    y=coords["y"]

    crafting_top_left = (766, 291)
    crafting_bottom_right = (934, 458)
    screenshot = capture_screenshot()
    print("Screenshot taken.")

    
    crafting_screenshot = screenshot[crafting_top_left[1]:crafting_bottom_right[1], crafting_top_left[0]:crafting_bottom_right[0]]
    template_image = cv2.imread(image)
    if template_image is None:
        raise ValueError(f"Template image at path {image} could not be loaded.")
    
    crafting_gray = cv2.cvtColor(crafting_screenshot, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(crafting_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)

    if loc[0].size > 0:
        print("Match found.")
        template_height, template_width = template_image.shape[:2]
        boxes = []
        for pt in zip(*loc[::-1]):
            top_left = (pt[0] + crafting_top_left[0], pt[1] + crafting_top_left[1])
            bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
            boxes.append([top_left[0], top_left[1], bottom_right[0], bottom_right[1]])

        boxes = np.array(boxes)
        picked_boxes = non_max_suppression(boxes, overlapThresh=0.3)
        matched_coords = []

        for (startX, startY, endX, endY) in picked_boxes:
            center_x = (startX + endX) // 2
            center_y = (startY + endY) // 2
            matched_coords.append((center_x, center_y))

        clicks_done = 0
        for coord in matched_coords:
            if max_clicks is not None and clicks_done >= max_clicks:
                break
            mouse.move(coord[0], coord[1])
            sleep(ttw)
            mouse.click(button='right')
            print(f"Clicked at {coord}")
            mouse.move(x,y)
            sleep(ttw)
            clickonempty("bin/empty.png")
            clicks_done += 1
            sleep(ttw) #idk
    else:
        print("Template not found")