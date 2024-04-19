import keyboard
import subprocess
import pystray
import os
from PIL import Image
from pystray import MenuItem as item

# Running screenshot.exe
def take_screenshot():
    exe_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'screenshot.exe'))
    subprocess.run([exe_path])


def exit_action(icon, item):
    icon.stop()

# Receiving call from PrtSc
def main():
    keyboard.add_hotkey("print_screen", take_screenshot)

    icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'icon.ico'))
    image = Image.open(icon_path)
    menu = (item('Exit', exit_action),)
    icon = pystray.Icon("name", image, "Screenshot capture", menu)
    icon.run()

# Run program
if __name__ == "__main__":
    main()
