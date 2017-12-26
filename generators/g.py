#g.py
import sys

inname, outname = sys.argv[1:3]

with open(inname,'r') as infile:
    with open(outname,'w') as outfile:
        warnings = (line.replace('\tWARNING', '')for line in infile if 'WARNING' in line)
        for line in warnings:
            outfile.write(line)
