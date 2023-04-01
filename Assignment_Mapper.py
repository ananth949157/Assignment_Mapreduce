import sys
for line in sys.stdin:
    line = line.strip()
    elements = line.split()
    for element in elements:
        print element, 1
