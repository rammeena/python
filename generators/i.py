#i.py
import sys

inname, outname = sys.argv[1:3]

def warning_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')

with open('inname','r') as infile:
    with open('outname','w') as outfile:
        filter = warnings_filter(infile)
        for l in filter:
            outfile.write(l)
