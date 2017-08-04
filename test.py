import os
import elcrypt
import csv

#os.system("git clone --depth=50 --branch=master https://github.com/elcrypt/elcrypt-tests.git")

with open('tests.csv', 'r') as datafile:
    datareader = csv.reader(datafile,delimiter=',',quotechar=' ')
    data = []
    for row in datareader:
        data.append(row)

for test in data:
    if (elcrypt.hash(test[0],test[1]) != test[2]):
        print("Given: "+test[0])
        print("Got: "+elcrypt.hash(test[0],test[1]))
        print("Expected: "+test[2])
        raise Exception("Test "+test[0]+" failed")