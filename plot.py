import sys
import matplotlib.pyplot as plt

file = open(sys.argv[1], 'r')
x = list(map(int, file.read().split()))
y = [i for i in range(len(x))]
plt.title("Attention")
plt.xlabel("Time (secs)")
plt.ylabel("Attention (out of 100)")
plt.plot(y, x)
plt.savefig("plot.png")