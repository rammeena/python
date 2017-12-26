import sys
inname, outname = sys.argv[1:3]

def warning_filter(infilename):
    with open(infilename) as infile:
        yield from (line.replace('\tWARNING','')for line in infile if 'WARNING' in line)


filter = warning_filter(inname)

with open(outname,'w') as outfile:
    for line in filter:
        outfile.write(line)


