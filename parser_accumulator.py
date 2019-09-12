from collections import defaultdict
import sys

visitors = defaultdict(lambda: [0, set()])

for line in sys.stdin:
    _, endpoint, uid = line.split()

    visitors[endpoint][0] += 1
    visitors[endpoint][1].add(uid)

for endpoint, visitors in visitors.items():
    print(f'{endpoint} {visitors[0]} {len(visitors[1])}')
