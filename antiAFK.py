import keyboard
import time
import random

def hold_random_key():
    keys = ['w', 'a', 's', 'd', 'ctrl', 'space']
    random_key = random.choice(keys)
    
    sleep_time = random.uniform(2, 5)
    
    keyboard.press(random_key)
    time.sleep(sleep_time)
    keyboard.release(random_key)

print("ALT+TAB to your game now...")
time.sleep(5)

while True:
    hold_random_key()
    time.sleep(1)
