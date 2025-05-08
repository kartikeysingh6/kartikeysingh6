import pyautogui
import time
import keyboard
import threading

# List of 40 countries
countries = [
    "Argentina", "Sri Lanka", "Germany", "Japan", "Canada", "Brazil", "France",
    "Italy", "India", "Australia", "China", "Mexico", "South Africa", "Spain",
    "Portugal", "Russia", "Norway", "Sweden", "Denmark", "Finland", "Netherlands",
    "Belgium", "Switzerland", "Poland", "Ukraine", "Turkey", "Thailand", "Vietnam",
    "Malaysia", "Indonesia", "New Zealand", "South Korea", "North Korea", "Egypt",
    "Saudi Arabia", "Iran", "Iraq", "Greece", "Israel", "Pakistan"
]

stop_flag = False

# Function to listen for 'q' keypress in a separate thread
def listen_for_quit():
    global stop_flag
    keyboard.wait('q')  # Blocks until 'q' is pressed
    stop_flag = True

# Start listener in background
threading.Thread(target=listen_for_quit, daemon=True).start()

# Give time to focus the Bing window
print("You have 5 seconds to focus on the Bing search bar...")
time.sleep(5)

for country in countries:
    if stop_flag:
        print("Quitting...")
        break
    pyautogui.typewrite(country, interval=0.05)
    pyautogui.press('enter')
    for _ in range(30):  # 3 seconds in 0.1s intervals
        if stop_flag:
            print("Quitting...")
            break
        time.sleep(0.2)
