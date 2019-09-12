import argparse
from datetime import datetime, timedelta
from itertools import permutations, islice
from random import choice, randint
from string import ascii_lowercase

arg_parser = argparse.ArgumentParser(description='Generates fake access logs')
arg_parser.add_argument('--num-requests', type=int, default=10_000_000)
arg_parser.add_argument('--num-users', type=int, default=1000)
arg_parser.add_argument('--num-endpoints', type=int, default=100)
args = arg_parser.parse_args()

endpoints = ['/' + ''.join(letters) for letters in islice(permutations(ascii_lowercase), args.num_endpoints)]
uids = list(range(args.num_users))

t = datetime(2000, 1, 1)

for _ in range(args.num_requests):
    t = t + timedelta(0, randint(0, 1))
    print(f'{t.isoformat()} {choice(endpoints)} {choice(uids)}')
