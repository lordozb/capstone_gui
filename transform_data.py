import sys

file = open('data.txt', 'r')
data = list(map(int, file.read().split()))

if len(data) < 10:
        print("Too less data to work with")
        sys.exit()

bucket = len(data) // 10
i = 0
count = 0
file_data = open('upload_data.txt', 'w+')
while count < 9:
	d = sum(data[i:i+bucket])/bucket
	file_data.write(str(d)+" ")
	i += bucket
	count += 1

d = sum(data[i:])/(len(data) - i)
file_data.write(str(d))
file_data.close()
