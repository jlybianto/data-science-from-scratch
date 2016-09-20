# line_count.py

# Script that counts the lines it receives and writes out the count

import sys

count = 0
for line in sys.stdin:
	count += 1
	
# print goes to sys.stdout
print count