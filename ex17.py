#this script can copy one file to another
from sys import argv
from os.path import exists
scrpit, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

input = open(from_file)
indata = input.read() #read file from from_file

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" %exists(to_file)
print "Ready,hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file, 'w')
output.write(indata)
print "Alright, all done"

output.close()
input.close()
