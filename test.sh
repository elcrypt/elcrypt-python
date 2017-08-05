#!/bin/bash

git clone --depth=50 --branch=master https://github.com/elcrypt/elcrypt-tests.git

while read line; do
	input=$(echo -n "$line" | cut -d ' ' -f 1)
	length=$(echo -n "$line" | cut -d ' ' -f 2 | cut -c 2- | rev | cut -c 2- | rev)
	expected=$(echo -n "$line" | cut -d ' ' -f 3)

	hash=$(python elcrypt.py "$input" "$length")

	if [ "$hash" != "$expected" ]; then
		echo "Input: ($input)"
		echo "Length: ($length)"
		echo "Output:   $hash"
		echo "Expected: $expected"
		exit 1
	fi
done < "elcrypt-tests/tests.csv"
