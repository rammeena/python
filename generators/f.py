import sys
inname, outname  = sys.argv[1], sys.argv[2]

with open(inname, 'r') as infile:
    with open(outname,'w') as outfile:
        warnings = (line for line in infile if 'WARNING' in line)
        for l in warnings:
            outfile.write(l)

