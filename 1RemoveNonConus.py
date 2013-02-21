#!/usr/bin/env python

#remove non-conus sequences and clean up header


import sys

fh = open(sys.argv[1], 'r')

name = 'FixedHeader' + sys.argv[1]
out = open(name, 'w')

#line = fh.readline()
#line = line.strip()
#line = line.split()
#print line[1]

for line in fh:
	if (line.startswith('>')):
		ID = line.strip().split()
		if ( ID[1] == 'Conus' ):
			output = ['>', ID[1], '_', ID[2], "\n"]
			out.writelines(output)
			newline = fh.next()
			out.writelines(newline)


	


#			for line in fh.next():
#				if (nextline.startswith('>')):


#				while position:
#					out.writelines(nextline)
#					line = fh.next()
#					position=False
			
			
#			line = fh.readlines()
#			if (line.startswith() == 'A' or 'G' or 'T' or 'C'):
#				out.writelines(line)
			 
out.close()
fh.close()

#for line in fh:
#	test = line.strip()
#	test = line.split(' ')	
#	if ( test[1] == 'Conus' ):
#		out.write("test[1] test[2] \n")


#print fh.readline()


