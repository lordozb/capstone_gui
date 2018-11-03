import threading
import time
import sys
import requests

#for testing
import random


# For using file inside the daemon thread
global f
global flag
f = open('data.txt', 'w+')
r = requests.get("http://localhost:3000/duration", data = {"id":sys.argv[1]})
flag = 1

# Daemon thread function to write the data to the file.
def background(t, stop_event):
	curr = 0
	while curr < t and not stop_event.is_set():
		if flag:
			print "Writing file"
			f.write(str(random.randint(1,100))+" ")
			time.sleep(1)
			curr += 1
	print "Press q"


# Will prevent I/O error or seg fault during post request if it takes too long.
stop_event = threading.Event()

threading1 = threading.Thread(target=background, args = (int(r.text), stop_event))

# now threading1 runs regardless of user input
threading1.daemon = True
threading1.start()

while True:
	if raw_input() == 'p':
		flag ^= 1
	if raw_input() == 'q':
		stop_event.set()
		f.close()
		print "Quitting"
		sys.exit()
	
