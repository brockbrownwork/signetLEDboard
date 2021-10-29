import pyperclip
import time
import pyautogui
from PIL import ImageGrab
from time import sleep
import ctypes

image = ImageGrab.grab()
for y in range(0, 100, 10):
    for x in range(0, 100, 10):
        color = image.getpixel((x, y))

def move_mouse(x,y):
    pyautogui.moveTo(x, y, duration=0.1)

def show_desktop():
    move_mouse(1920-3, 1080-3)
    pyautogui.click()

def click_ic_production():
    move_mouse(714, 742)
    pyautogui.doubleClick()

def click_jeweler_snapshot():
    move_mouse(126, 442)
    pyautogui.click()

def click_current_snapshot():
    move_mouse(522, 397)
    pyautogui.click()

def copy_database():
    sleep(0.2)
    pyautogui.hotkey('ctrl', 'a')
    sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    sleep(0.2)
def exit_window():
    sleep(0.1)
    move_mouse(1897, 16)
    pyautogui.click()

show_desktop()
click_ic_production()
wait_time = 0.1
# wait for the page to show up
done = False
while not done:
    sleep(wait_time)
    image = ImageGrab.grab()
    if image.getpixel((673,847)) == (163, 167, 193):
        done = True
click_jeweler_snapshot()
# wait for the current snapshot button to show up
done = False
while not done:
    sleep(wait_time)
    image = ImageGrab.grab()
    if image.getpixel((551,406)) == (0, 120, 215):
        done = True
click_current_snapshot()
# wait for the data to show up
done = False
while not done:
    sleep(wait_time)
    image = ImageGrab.grab()
    if image.getpixel((298,209)) == (135, 131, 131):
        done = True
copy_database()
exit_window()

data = pyperclip.paste()
with open("data.txt", "w") as f:
    f.write(data)

print (image.getpixel((268,218)))

print(pyautogui.size())
print("Done!")
ctypes.windll.user32.MessageBoxW(0, "Done!", "Cell Data Grabber", 1)

