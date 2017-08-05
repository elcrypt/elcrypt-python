#!/bin/bash

git clone --depth=50 --branch=master https://github.com/elcrypt/elcrypt-tests.git

while read line; do
	input=$(echo -n "$line" | cut -d ' ' -f 1)
	salt=$(echo -n "$line" | cut -d ' ' -f 2 | cut -c 2- | rev | cut -c 2- | rev)
	expected=$(echo -n "$line" | cut -d ' ' -f 3)

	hash=$(python elcrypt.py "$input" "$salt")

	if [ "$hash" != "$expected" ]; then
		echo "Input: ($input)"
		echo "Salt: ($salt)"
		echo "Output:   $hash"
		echo "Expected: $expected"
		exit 1
	fi
done < "elcrypt-tests/tests.csv"

#with open('elcrypt-tests/tests.csv', 'r') as datafile:
#    datareader = csv.reader(datafile,delimiter=',',quotechar=' ')
#    data = []
#    for row in datareader:
#        data.append(row)
#
#for test in data:
#    if (elcrypt.hash(test[0],test[1]) != test[2]):
#        print("Given: "+test[0])
#        print("Got: "+elcrypt.hash(test[0],test[1]))
#        print("Expected: "+test[2])
#        raise Exception("Test "+test[0]+" failed")
