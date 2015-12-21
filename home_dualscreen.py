#!/usr/bin/env python

import os
import subprocess

cmd = """xrandr --output VIRTUAL1 --off --output DP3 --off --output DP2 --off --output DP1 
--off --output HDMI3 --off --output HDMI2 --off --output HDMI1 --off --output LVDS1 --mode 
1366x768 --pos 1920x312 --rotate normal --output VGA1 --mode 1920x1080 --pos 0x0 --rotate
 normal
"""

os.system(cmd)
print "applying monitor settings"
