import pyautogui
import time
import playsound
#pip install pyautogui playsound
#stops the pause
pyautogui.PAUSE=False
#puts to max volume
for _ in range(50):
    time.sleep(0.001)
    pyautogui.keyDown("volumeUp")
#plays a really loud sound download audio file
playsound.playsound("HEEEEELP.mp3")
