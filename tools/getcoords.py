import pyautogui
import keyboard

def get_coordinates():
    print("Move your mouse to the top-left corner of the inventory pool and press 'o'.")
    # Wait until 'o' key is pressed
    keyboard.wait('o')
    top_left = pyautogui.position()
    print(f"Top-left corner: {top_left}")

    print("Move your mouse to the bottom-right corner of the inventory pool and press 'o'.")
    # Wait until 'o' key is pressed
    keyboard.wait('o')
    bottom_right = pyautogui.position()
    print(f"Bottom-right corner: {bottom_right}")

    return top_left, bottom_right

if __name__ == "__main__":
    top_left, bottom_right = get_coordinates()
    print(f"Inventory pool coordinates: Top-left: {top_left}, Bottom-right: {bottom_right}")

    # Example: Use these coordinates in your main script
    inventory_top_left = (top_left.x, top_left.y)
    inventory_bottom_right = (bottom_right.x, bottom_right.y)

    print(f"Inventory pool coordinates set: Top-left: {inventory_top_left}, Bottom-right: {inventory_bottom_right}")
