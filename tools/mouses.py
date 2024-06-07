import time
import pyautogui
import mouse
from pynput.mouse import Controller as PynputController, Button as PynputButton
import win32api
import win32con
import statistics

# Function to measure time taken for 100 clicks using pyautogui
def measure_pyautogui():
    start_time = time.time()
    for _ in range(100):
        pyautogui.click()
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 clicks using mouse
def measure_mouse():
    start_time = time.time()
    for _ in range(100):
        mouse.click()
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 clicks using pynput
def measure_pynput():
    mouse_controller = PynputController()
    start_time = time.time()
    for _ in range(100):
        mouse_controller.click(PynputButton.left)
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 clicks using pywin32
def measure_pywin32():
    start_time = time.time()
    for _ in range(100):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    end_time = time.time()
    return end_time - start_time

# Measure the click speeds and average over 3 runs
def measure_average_time(measure_function, runs=3):
    times = []
    for _ in range(runs):
        times.append(measure_function())
    return statistics.mean(times)

# Main function to perform the measurements
def main():
    pyautogui_time = measure_average_time(measure_pyautogui)
    mouse_time = measure_average_time(measure_mouse)
    pynput_time = measure_average_time(measure_pynput)
    pywin32_time = measure_average_time(measure_pywin32)

    print(f"Pyautogui: {pyautogui_time:.2f} sec")
    print(f"Mouse: {mouse_time:.2f} sec")
    print(f"Pynput: {pynput_time:.2f} sec")
    print(f"Pywin32: {pywin32_time:.2f} sec")

if __name__ == "__main__":
    main()
