(
    echo "PARSER #USERS #ENDPOINTS TIME MEM"
    for num_users in 100 1000 10000; do
       for num_endpoints in 10 100 1000; do
           python generate.py --num-users $num_users --num-endpoints $num_endpoints >my.log
           for parser in parser.py parser_counter.py parser_dataclass.py parser_accumulator.py; do
               echo "parser: $parser $num_users $num_endpoints"
               /usr/bin/time -l python $parser <my.log 2> >(grep -E 'max|real') >/dev/null
           done
       done
    done | sed -E '/parser:/ {N; N; s/\n/ /g;}' | awk '{ print $2, $3, $4, $5, $11 }'
) | column -t
