import time
import pyautogui
import keyboard
from pynput.keyboard import Controller as PynputController, Key
import win32api
import win32con
import statistics

# Function to measure time taken for 100 key presses using pyautogui
def measure_pyautogui():
    start_time = time.time()
    for _ in range(100):
        pyautogui.press('a')
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 key presses using keyboard
def measure_keyboard():
    start_time = time.time()
    for _ in range(100):
        keyboard.write('a')
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 key presses using pynput
def measure_pynput():
    keyboard_controller = PynputController()
    start_time = time.time()
    for _ in range(100):
        keyboard_controller.press('a')
        keyboard_controller.release('a')
    end_time = time.time()
    return end_time - start_time

# Function to measure time taken for 100 key presses using pywin32
def measure_pywin32():
    start_time = time.time()
    for _ in range(100):
        win32api.keybd_event(0x41, 0, 0, 0)  # Press 'a'
        win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release 'a'
    end_time = time.time()
    return end_time - start_time

# Measure the key press speeds and average over 3 runs
def measure_average_time(measure_function, runs=3):
    times = []
    for _ in range(runs):
        times.append(measure_function())
    return statistics.mean(times)

# Main function to perform the measurements
def main():
    pyautogui_time = measure_average_time(measure_pyautogui)
    keyboard_time = measure_average_time(measure_keyboard)
    pynput_time = measure_average_time(measure_pynput)
    pywin32_time = measure_average_time(measure_pywin32)

    print(f"Pyautogui: {pyautogui_time:.2f} sec")
    print(f"Keyboard: {keyboard_time:.2f} sec")
    print(f"Pynput: {pynput_time:.2f} sec")
    print(f"Pywin32: {pywin32_time:.2f} sec")

if __name__ == "__main__":
    main()