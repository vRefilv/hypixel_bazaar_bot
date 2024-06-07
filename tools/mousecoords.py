import mouse

def print_mouse_position():
    # Get the current mouse position
    x, y = mouse.get_position()
    print(f"Mouse position: ({x}, {y})")

def on_ctrl_pressed():
    print_mouse_position()

# Bind the function to the 'ctrl' key
mouse.on_button(on_ctrl_pressed, buttons='left', types=('down',))

print("Press the left mouse button to get the current mouse coordinates. Press 'Ctrl+C' to exit.")

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")
    mouse.unhook_all()
