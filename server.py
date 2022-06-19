import socket
import pyautogui
from time import sleep

pyautogui.FAILSAFE = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',4444))

while True:
	keystroke,_ = s.recvfrom(1024)
	keystroke = keystroke.decode()
	if keystroke == 'CtTa':
		pyautogui.keyDown('ctrl')
		pyautogui.press('tab')
		pyautogui.keyUp('ctrl')
	elif keystroke == 'bckwrd':
		pyautogui.keyDown('alt')
		pyautogui.press('left')
		pyautogui.keyUp('alt')
	elif keystroke == 'frwrd':
		pyautogui.keyDown('alt')
		pyautogui.press('right')
		pyautogui.keyUp('alt')
	elif keystroke == 'nt':
		pyautogui.hotkey('ctrl','t')
	elif keystroke == 'ct':
		pyautogui.hotkey('ctrl','w')
	elif keystroke == 'mdown':
		pyautogui.move(0, 20)
	elif keystroke == 'mleft':
		pyautogui.move(-20, 0)
	elif keystroke == 'mright':
		pyautogui.move(20, 0)
	elif keystroke == 'mup':
		pyautogui.move(0, -20)
	elif keystroke == 'click':
		 pyautogui.click()
	elif keystroke == 'mclick':
		 pyautogui.click(button='middle')
	elif keystroke == 'rclick':
		 pyautogui.click(button='right')
	elif keystroke == 'scrldwn':
		pyautogui.scroll(-10)
	elif keystroke == 'scrlup':
		pyautogui.scroll(10)
	elif keystroke == 'cls':
		pyautogui.hotkey('alt','f4')
	elif keystroke == 'volumeup':
		pyautogui.hotkey('shift','ctrl','alt','}')
	elif keystroke == 'volumedown':
		pyautogui.hotkey('shift','ctrl','alt','|')
	else:
		pyautogui.press(keystroke)
