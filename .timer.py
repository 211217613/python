#!/usr/bin/python
import time, sys, notify2

notify2.init("60-minute Timer")

n = notify2.Notification("HI",
						  "Dont forget to stretch",
						  "notification-message-im"
						  )
n.set_timeout(10e3) #10e3 mseconds == 10 seconds

while True:
	n.show()
	time.sleep(3600)