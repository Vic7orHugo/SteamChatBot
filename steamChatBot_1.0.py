#! python3
"""
steamChatBot_1.0.py - Bot to automatically answer steam chat notifications.
10/01/2018 at 15:42
"""

# Importing modules
import pyautogui as gui
from PIL import Image
import time, datetime
# import os

# Constants
STEAM_APP = (670, 735)
STEAM_APP_COLOR = (236, 223, 111)
STEAM_CHAT_POPUP = (1284, 675) # original -> (1284, 675)
STEAM_CHAT_POPUP_COLOR = (35, 35, 35)
STEAM_CHAT_WINDOW = (953, 476)
SHOW_DESKTOP = (1365, 767)
STATUS_ON = 'BOT RUNNING...'
STATUS_OFF = 'BOT OFF'
# WORKING_DIRECTORY = 'C:\\Users\\Victor\\Documents\\Python Scripts'

# Chance to exit code
gui.PAUSE = 0.5

# Changing working directory
# os.chdir(WORKING_DIRECTORY)

# Bot routine, with an exception to stop the bot by pressing CTRL-C
try:
	while True:
		# chatNotification = gui.locateOnScreen('steam_chat_notification.jpg')
		while not gui.pixelMatchesColor(STEAM_APP[0], STEAM_APP[1], STEAM_APP_COLOR):
			print(STATUS_ON, end='')
			time.sleep(0.5)
			print('\b' * len(STATUS_ON), end='', flush=True)
		gui.click(STEAM_APP[0], STEAM_APP[1])
		time.sleep(0.5)
		gui.click(STEAM_CHAT_WINDOW[0], STEAM_CHAT_WINDOW[1])
		dt = datetime.datetime.now()
		# timeString = dt.day + '/' + dt.month + '/' + dt.year + '---' + dt.hour + ':' + dt.minute + ':' + dt.second
		timeString = dt.strftime('%d/%m/%Y %H:%M:%S')
		gui.typewrite('SteamChat Bot (' + timeString + '): Usuario longe do teclado.')
		gui.press('enter')    
		# time.sleep(2)
		# gui.click(SHOW_DESKTOP[0], SHOW_DESKTOP[1])
except KeyboardInterrupt:
	print('\n' + STATUS_OFF)
