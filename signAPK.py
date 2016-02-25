#!/usr/bin/python3.4m

#Specify what apk to sign
#Get input from user or it can just sign all apks/
#Note paths must be in double quotes

from subprocess import call
import sys

def main():

	#get path to apk
	# apkpath1 = input("absolute path to apk\n")
	# apkpath = "/home/ruben/Dev/Cydia/VioletCydia/VioletCydia.apk"
	apkpath = sys.argv[1] 
	# call(['ls'])
	retcode = call(
		['jarsigner',
		'-verbose',
		'-keystore',
		"/home/ruben/.android/debug.keystore",
		'-storepass',
		'android',
		'-keypass',
		'android',
		 apkpath,
		 'androiddebugkey' ]
	)

	print(retcode)

if __name__ == '__main__':
	main()

#jarsigner -verbose -keystore ~/.android/debug.keystore -storepass android -keypass android /home/ruben/Dev/Cydia/VioletCydia/VioletCydia.apk androiddebugkey


#jarsigner -verbose -keystore ~/.android/debug.keystore -storepass android -keypass android /path/to/MY.apk androiddebugkey