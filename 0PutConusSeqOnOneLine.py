#!/usr/bin/env python

#script to put conus sequence on one line

import sys



fh = open(sys.argv[1], 'r')

name = 'processed' + sys.argv[1]
out = open(name, 'w')

#line = fh.readline()
#line = line.strip()
#line = line.split()
#print line[1]

for line in fh:
	if (line.startswith('>')):
		line = "\n"+line
		out.writelines(line)
	else:
		line = line.strip()
		out.writelines(line)

fh.close
out.close
