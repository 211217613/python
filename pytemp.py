#!/usr/bin/python3 -tt

"""
Get status of cpu temperatures every x seconds and log to a file
Compare to load average and get some graphs n shit
Upload automatically to a google doc spread sheet and try to compare with everyone else
Set up some correlation with load average
"""
import os
import time
import csv

output_file = open("./temp_data.csv", 'w', newline='')
outputWriter = csv.writer(output_file)
temps = []
# Open /sys/class..... and read temperature.
# Append to a file 
t1 = '/sys/class/thermal/thermal_zone0/temp'
t2 = '/sys/class/hwmon/'

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue #skips non-csv files
	else:
		print("")
# for (root, dirs, files) in os.walk('/sys/class/thermal/'):
# 	print("dirs is a string {}".format(dirs))

with open('/sys/class/thermal/thermal_zone0/temp', 'r') as paths:
	temp = int(paths.readline())/1000.0
counter = 0

while counter < 10:
	temps.append(temp/1000.0)
	outputWriter.writerow( temps )
	counter = counter + 1
	time.sleep(1)
print( temps )
output_file.close()