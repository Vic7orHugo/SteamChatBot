#! python3
"""
steamChatBot_1.3.py - Bot to automatically answer steam chat notifications.
12/01/2018 at 10:00
"""

# Importing modules
import pyautogui as gui
from PIL import Image
import time, datetime, threading

# Constants
STEAM_APP = 'steam_icon.png' # (670, 735)
##STEAM_APP_COLOR = (236, 223, 111)
STEAM_CHAT_POPUP = 'steam_popup_window.png' # original -> (1284, 675)
##STEAM_CHAT_POPUP_COLOR = (35, 35, 35)
STEAM_CHAT_WINDOW_OPTIONS = 'steam_chat_window_options.png' # (953, 476)
STEAM_CHAT_TEXT_FIELD = 'steam_chat_text_field.png'
##SHOW_DESKTOP = (1365, 767)
STATUS_ON = 'BOT RUNNING...'
STATUS_OFF = 'BOT OFFLINE'
USER_AWAY_STATUS = 'USER AWAY'
USER_ONLINE_STATUS = 'USER ONLINE'
AFK_TIME = 10*60		# Time in seconds

# Chance to exit code
gui.PAUSE = 0.1
gui.FAILSAFE = True

# Getting a screenshot to save images for the bot guidance
##im = gui.screenshot()
##im.save('steam_icon.png')

# Bot routine, with an exception to stop the bot by pressing CTRL-C
try:
	# Start
	print(STATUS_ON)
	steamChatNotification = None
	timeAway = 0
	message = ''
	while True:
		# Routine to sense mouse movement, A.K.A., checking if the user is away
		# If the user came back before the time needed to the bot start sending automatic responses, go back to the main while
		afkStartTime = time.time()
		mousePosX, mousePosY = gui.position()
		while ((mousePosX, mousePosY) == gui.position()) and (timeAway < AFK_TIME):		# Counts the time that the user is away
			if message != USER_ONLINE_STATUS:
				print(USER_ONLINE_STATUS)
				message = USER_ONLINE_STATUS
			afkEndTime = time.time()
			timeAway = afkEndTime - afkStartTime		
			#print('\b' * len(USER_ONLINE_STATUS), end='', flush=True)	
		if timeAway < AFK_TIME:		
			continue
		# Routine to send automatic responses. If the user comes back before anyone talks to the user, this routine ends	
		while (steamChatNotification == None) and ((mousePosX, mousePosY) == gui.position()):
			if message != USER_AWAY_STATUS:
				print(USER_AWAY_STATUS)
				message = USER_AWAY_STATUS	
			steamChatNotification = gui.locateOnScreen(STEAM_CHAT_POPUP)
			if steamChatNotification == None:
				steamChatNotification = gui.locateOnScreen(STEAM_APP)			
			# print('\b' * len(USER_AWAY_STATUS), end='', flush=True)		
		# Goes back to the main while	
		if (mousePosX, mousePosY) != gui.position():
			timeAway = 0		
			continue	
		# Clicks the steam chat window popup or the steam app icon	
		steamChatLocation = gui.center(steamChatNotification)
		gui.click(steamChatLocation[0], steamChatLocation[1])							
		# Clicks on the field to enter the text
		while gui.locateOnScreen(STEAM_CHAT_TEXT_FIELD) == None:
			time.sleep(0.5)
		steamChatTextField = gui.locateOnScreen(STEAM_CHAT_TEXT_FIELD)
		steamChatTextFieldLocation = gui.center(steamChatTextField)
		gui.click(steamChatTextFieldLocation[0], steamChatTextFieldLocation[1])			
		# Automatic response section
		dt = datetime.datetime.now()													# Gets the time and date
		timeString = dt.strftime('%d/%m/%Y %H:%M:%S')									# Creates the time and date string
		gui.typewrite('SteamChat Bot (' + timeString + '): Usuario longe do teclado.')	# The standart automatic response
		gui.press('enter')							 
		# Final section
		steamChatWindowOptions = gui.locateOnScreen(STEAM_CHAT_WINDOW_OPTIONS)
		steamChatWindowOptionsLocation = gui.center(steamChatWindowOptions)
		gui.click(steamChatWindowOptionsLocation[0], steamChatWindowOptionsLocation[1])	# Goes back to the previous window
		gui.moveTo(mousePosX, mousePosY)				# Moves the cursor to the original position
		steamChatNotification = None
		time.sleep(5)	# Waits 5 seconds, so the bot doenst flood the chat in case the other user sends to much messages

except KeyboardInterrupt:
	print(STATUS_OFF)
