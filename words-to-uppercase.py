# This file reads in a file name and changes all characters to upper-case
# 
#
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line=line.strip()
    print(line.upper())
