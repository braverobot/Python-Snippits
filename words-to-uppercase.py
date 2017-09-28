# This file reads in a file name and changes all characters to upper-case
#
fname = input("Enter file name: ")
### Check to make sure the file opens properly
try:
    fh = open(fname)
except:
    print("There was an error in your filename. Please check the name and try again")
    quit()
# Read in each line, strip the newline, and change all lines to caps
for line in fh:
    line=line.strip()
    print(line.upper())                     
