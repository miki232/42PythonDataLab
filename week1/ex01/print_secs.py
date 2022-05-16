import sys

hours = int(sys.argv[1])
minutes = int(sys.argv[2])
seconds = int(sys.argv[3])
conversion = hours * 3600 + minutes * 60
print(conversion + seconds)