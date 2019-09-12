import sys
from collections import defaultdict
from dataclasses import make_dataclass

Visitors = make_dataclass('Visitors', [('total', int), ('unique', set)])

visitors = defaultdict(lambda: Visitors(0, set()))
for line in sys.stdin:
    _, endpoint, uid = line.split()

    visitors[endpoint].total += 1
    visitors[endpoint].unique.add(uid)

for endpoint, visitors in visitors.items():
    print(f'{endpoint} {visitors.total} {len(visitors.unique)}')
