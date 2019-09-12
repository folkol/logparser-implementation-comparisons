from collections import defaultdict, Counter
import sys

visitors = defaultdict(list)
for line in sys.stdin:
    _, endpoint, uid = line.split()
    visitors[endpoint].append(uid)

for endpoint, visitors in visitors.items():
    print(f'{endpoint} {len(visitors)} {len(set(visitors))}')
