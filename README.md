# logparser implementations

Trying some different logparser implementations.

## benchmark

```
master$ time bash test.sh
PARSER                 #USERS #ENDPOINTS  TIME   MEM
parser.py              100    10          10.74  701382656
parser_counter.py      100    10          12.83  7069696
parser_dataclass.py    100    10          12.45  7942144
parser_accumulator.py  100    10          12.38  7045120
parser.py              100    100         11.30  688578560
parser_counter.py      100    100         12.28  8712192
parser_dataclass.py    100    100         11.35  9318400
parser_accumulator.py  100    100         11.40  8470528
parser.py              100    1000        11.32  719732736
parser_counter.py      100    1000        11.79  20123648
parser_dataclass.py    100    1000        13.60  23072768
parser_accumulator.py  100    1000        13.59  22953984
parser.py              1000   10          11.55  760074240
parser_counter.py      1000   10          12.19  8409088
parser_dataclass.py    1000   10          12.16  8863744
parser_accumulator.py  1000   10          11.68  7979008
parser.py              1000   100         12.19  747118592
parser_counter.py      1000   100         13.99  20631552
parser_dataclass.py    1000   100         13.69  17911808
parser_accumulator.py  1000   100         12.45  17387520
parser.py              1000   1000        13.39  775659520
parser_counter.py      1000   1000        18.88  134316032
parser_dataclass.py    1000   1000        17.63  107560960
parser_accumulator.py  1000   1000        11.66  106971136
parser.py              10000  10          10.90  764604416
parser_counter.py      10000  10          14.83  18501632
parser_dataclass.py    10000  10          14.48  21209088
parser_accumulator.py  10000  10          12.63  20340736
parser.py              10000  100         12.92  752971776
parser_counter.py      10000  100         14.99  107081728
parser_dataclass.py    10000  100         14.37  131231744
parser_accumulator.py  10000  100         13.74  130215936
parser.py              10000  1000        13.18  782086144
parser_counter.py      10000  1000        18.56  741048320
parser_dataclass.py    10000  1000        18.78  981254144
parser_accumulator.py  10000  1000        17.14  978939904

real	18m30.216s
user	17m19.656s
sys	0m30.117s
```
