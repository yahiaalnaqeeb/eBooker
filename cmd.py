#!/usr/bin/python3
version = "0.1"

from time import sleep
import sys
import os
try:
	import curses
except ImportError:
	print("Hmmm... I wonder where \"curses\" is! If the program is still running, please stop it with ^C. Please contact the developer at archmaster@yahoo.com. Please type \"51189819\" into the subject box (without the quotes)!")
	sleep(2)
os.system("clear")
print("Loading...")
sleep(3)
os.system("clear")
print("******************** eBooker v" + version + " ********************")
print("")
sleep(1)

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit this session\nabout - read about this tool\nedit - edit a file\nclear -  clear the screen"
aboutString = "eBooker\nA command-line tool written in Python for writing Kindle eBooks. So far, it will just execute simple commands like \"help\" and \"exit.\""
def editor(stdscr):
	stdscr.clear()
	stdscr.addstr("Testing...")

while True:
	cmd = str(input("ebooker > "))
	if cmd == "help":
		print(helpString)
	elif cmd == "exit":
		exitloopBool = True
		while exitloopBool:
			exitBool = str(input("Would you like to quit? (y/n) "))
			if exitBool == "y":
				exitloopBool = False
				os.system("clear")
				sys.exit()
			elif exitBool == "n":
				exitloopBool = False
				print("OK, not exited!")
			else:
				print("Please type in \"y\" or  \"n\".")
	elif cmd == "about":
		print(aboutString)
	elif cmd == "edit":
		editloopBool = True
		while editloopBool:
			editBool = str(input("Would you like to create a new file? (y/n) "))
			if editBool == "y":
				editloopBool = False
				print("You want to create a new file.")
			elif editBool == "n":
				editloopBool = False
				print("You want to edit an existing file!")
			else:
				print("Please type in \"y\" or  \"n\".")
			stdscr = curses.initscr()
			curses.noecho()
			curses.cbreak()
			stdscr.keypad(True)
			curses.wrapper(editor)
			curses.nocbreak()
			stdscr.keypad(False)
			curses.echo()
			stdscr = None;
	elif cmd == "clear":
		print("Clearing...")
		sleep(2)
		os.system("clear")
		print("******************** eBooker v" + version + " ********************")
		print("")
		sleep(1)
	else:
		print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")