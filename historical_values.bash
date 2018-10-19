cat log.txt | grep $1 | grep -v ERC | awk '{print $3}' | tr '=' ' ' | tr "," " " | awk '{print $2}' | bc -l | sort -n
