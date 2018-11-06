from tkinter import *
from tkinter import ttk
from webapp import fetch_details
import threading
import random
import time

global f, stop_event, pause_event

stop_event = threading.Event()
pause_event = threading.Event()


# Daemon thread function to write the data to the file.
def background(t, stop_event):
	curr = 0
	while curr < t and not stop_event.is_set():
		if not pause_event.is_set():
			f = open('data.txt', 'w+')
			print("Writing file")
			f.write(str(random.randint(1,100))+" ")
			time.sleep(1)
			curr += 1
			duration.set(str(t-curr))
			f.close()

def startIO():
	# Will prevent I/O error or seg fault during post request if it takes too long.
	threading1 = threading.Thread(target=background, args = (int(duration.get()), stop_event))

	# now threading1 runs regardless of user input
	threading1.daemon = True
	threading1.start()

def calculate(*args):
	try:
		action.set("Start")
		stop_event.clear()
		params = int(id.get())
		time,name = map(str,fetch_details(params).text.split(","))
		title.set(name)
		duration.set(time)
	except ValueError:
		pass

def getdata(*args):
	if action.get() == "Start":
		action.set("Pause")
		pause_event.clear()
		startIO()
	else:
		action.set("Start")
		pause_event.set()

def stop():
	stop_event.set()


root = Tk()
root.title("Smart Learning System")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

id = StringVar()
title = StringVar()
duration = StringVar()
action = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=id)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=title).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=duration).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Fetch Details", command=calculate).grid(column=3, row=1, sticky=W)

ttk.Label(mainframe, text="Video ID :").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Video Title :").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Duration :").grid(column=1, row=3, sticky=E)

ttk.Button(mainframe, textvariable=action, command=getdata).grid(column=1, row=4, sticky=W)
action.set("Start")
ttk.Button(mainframe, text="Stop", command=stop).grid(column=3, row=4, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()
