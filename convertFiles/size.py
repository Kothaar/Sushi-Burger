import os
import sys

filename = sys.argv[1]

stats = os.stat(filename)
sz = stats.st_size / (1024 * 1024)
print("size in MB : ", sz)
