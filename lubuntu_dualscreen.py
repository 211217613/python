#! /usr/bin/env python

import os
import subprocess

#print os.environ['DESKTOP_SESSION']
cmd = 'xrandr --output VIRTUAL1 --off --output DP3 --off --output DP2 --off --output DP1 --off --output HDMI3 --off --output HDMI2 --off --output HDMI1 --off --output LVDS1 --mode 1366x768 --pos 1920x312 --rotate normal --output VGA1 --mode 1920x1080 --pos 0x0 --rotate normal' 
wm = os.environ['DESKTOP_SESSION']

if wm == 'Lubuntu':
    print "applying monitor settings"
    os.system(cmd) #might cause errors. Use subprocess instead
    # process = subprocess.Popen(cmd.split(), stdout = subprocess.PIPE)
    # output = process.communicate()[0]

else:
    print "Running KDE"
