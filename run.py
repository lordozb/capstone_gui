import os
import sys
import time

print "Connecting EEG Device.."
time.sleep(1)
print "Connecting to the application..."
time.sleep(1)
print "Fetching metadata.."
time.sleep(1)

os.system('python2 store_data.py '+str(sys.argv[1]))

time.sleep(1)

