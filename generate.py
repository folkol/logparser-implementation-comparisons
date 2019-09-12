from datetime import datetime, timedelta
from string import ascii_lowercase
from itertools import permutations
from random import choice, randint

NUM_REQUESTS = 10_000_000
NUM_USERS = 1000

endpoints = ['/' + ''.join(p) for p in permutations(ascii_lowercase, r=3)]
uids = list(range(NUM_USERS))

t = datetime(2000, 1, 1)

for _ in range(NUM_REQUESTS):
    t = t + timedelta(0, randint(0, 1))
    endpoint = choice(endpoints)
    uid = choice(uids)
    print(f'{t.isoformat()} {endpoint} {uid}')
