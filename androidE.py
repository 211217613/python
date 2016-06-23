#!/usr/bin/python3
import subprocess
import sys
import re
import os
from time import sleep
#Not running more than one emulator so serial number not needed
ADBFLAGS = '-e'

"""
1. get attached devices - No emulator -> goto 2
2. launch emulator
3. wait for emulator to finish booting - need a trigger adb shell getprop sys.boot_completed != 1
4. unlock the screen - wait for trigger
5. launch app 
6. trigger arqc_sign
"""


"""
Usage:
This script will launch and automate some processes 
regarding the emulator, there is usually lots of user interaction
required that slows down the process with the emulator
"""

emulator = False
screen = False

def getAttachedDevices():
	""" 
	This helps get dev id's
	just in case you have your phone plugged in
	"""

	counter = 0
	output = str(subprocess.check_output(['adb','devices']))	#returns byte string

	print("type output {}".format(type(output)))
	#TODO: maybe use a regex to parse the output
	if 'emulator' in output:
		print ("Emulator attached")
		emulator = True
	elif 'emulator' not in output:
		print ("no emulator attached...launching emulator")
		subprocess.call(['/home/ruben/Dev/Cydia/pandroid/start.sh'], shell = False)
		# os.system('sh /home/ruben/Dev/Cydia/pandroid/start.sh')

	# [for char in output counter = counter + 1]
	for char in output:
		# print char
		counter = counter + 1
	print("counter: {}".format( counter ) )

def screenUnlock():
	while subprocess.check_output(['adb -e shell getprop sys.boot_completed']) is not 1:
		sleep(2)
def main():
	print("Getting list of devices")
	getAttachedDevices()
	print("Starting the emulator")
	screenUnlock()
	print("waiting for boot up")

	" to unlock the screen adb shell input keyevent 82"

if __name__ == '__main__':
	main()


	"""

adb shell am start -a android.intent.action.MAIN -n graha.ms.tunnel/graha.ms.tunnel.TunnelConfig ##start new instance of tetherbot or bring current one to front
adb shell am start -n bw.ita.worldline.com.whiteboxtestapplication/bw.ita.worldline.com.whiteboxtestapplication.MainActivity

adb shell input keyevent 19 ###press up
adb shell input keyevent 66 ###press enter
adb shell am start -a android.intent.category.HOME -n com.fede.launcher/.Launcher
adb forward tcp:1080 tcp:1080

	"""


"""
0 -->  "KEYCODE_UNKNOWN" 
1 -->  "KEYCODE_MENU" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"

"""