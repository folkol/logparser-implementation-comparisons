# logparser implementations

Time and memory as reported by `time -l`.

| impl        | time   | mem     |
|-------------|--------|---------|
| naive list  | 10.92s | 775 Mb  |
| counter     | 14.68s | 817 Mb  |
| dataclass   | 14.42s | 1033 Mb |
| accumulator | 13.03s | 1031 Mb |

## Log

```bash
$ time python generate.py >my.log
$ /usr/bin/time -l python parser.py <my.log >/dev/null
       10.92 real        10.19 user         0.68 sys
 775327744  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
    192590  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         0  voluntary context switches
      6819  involuntary context switches
$ /usr/bin/time -l python parser_counter.py <my.log >/dev/null
       14.68 real        14.14 user         0.48 sys
 817537024  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
    201282  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         0  voluntary context switches
      7006  involuntary context switches
$ /usr/bin/time -l python parser_dataclass.py <my.log >/dev/null
       14.43 real        13.84 user         0.54 sys
1033084928  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
    252990  page reclaims
         1  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         9  voluntary context switches
      5463  involuntary context switches
$ /usr/bin/time -l python parser_accumulator.py <my.log >/dev/null
       13.03 real        12.46 user         0.53 sys
1031704576  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
    252544  page reclaims
         0  page faults
         0  swaps
         0  block input operations
         0  block output operations
         0  messages sent
         0  messages received
         0  signals received
         2  voluntary context switches
      5235  involuntary context switches
```