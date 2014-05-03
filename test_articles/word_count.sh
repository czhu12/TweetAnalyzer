tr -c '[:alnum:]' '[\n*]' < $1 | sort | uniq -c | sort -nr | head  -10

