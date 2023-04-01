import sys
count = 0
for line in sys.stdin:
    try:
        left_side = line.strip().split()[0]
        int_val = int(left_side)
        count += int_val
    except ValueError:
        pass

print count