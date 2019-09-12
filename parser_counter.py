import sys
from collections import defaultdict, Counter

visitors = defaultdict(Counter)
for line in sys.stdin:
    _, endpoint, uid = line.split()
    visitors[endpoint][uid] += 1

for endpoint, visitors in visitors.items():
    print(f'{endpoint} {sum(visitors.values())} {len(visitors)}')
