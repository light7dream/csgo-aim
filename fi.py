import pyautogui as pygui
import time
import math

fov = 54.0
time.sleep(3)
while True:
	b = 640.0 / math.tan(fov / 2 / 180.0 * math.pi)
	dx= 6546 * (math.atan(120.0 / b) / 360.0 * 180 / math.pi) * 2.5
	pygui.moveTo(960 + dx, 550)
	print(dx)
	time.sleep(1)