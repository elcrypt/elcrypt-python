#!/bin/bash

#git clone --depth=50 --branch=master https://github.com/elcrypt/elcrypt-tests.git

current=-1
while read line; do
	let "current+=1"
	if [ $current == 0 ]; then
		input=$(echo -n "$line")
	elif [ $current == 1 ]; then
		length=$(echo -n "$line")
	elif [ $current == 2 ]; then
		expected=$(echo -n "$line")
	elif [ $current == 3 ]; then
		hash=$(python elcrypt.py "$input" "$length")

		if [ "$hash" != "$expected" ]; then
			echo "Input: ($input)"
			echo "Length: ($length)"
			echo "Output:   $hash"
			echo "Expected: $expected"
			exit 1
		fi
		current=-1
	fi	
done < "elcrypt-tests/tests.csv"
