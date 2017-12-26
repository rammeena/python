#o.py
"Program to search for a faulty disk"

import re

def match_regex(filename, regex):
    with open(filename,'r') as f:
        lines = f.readlines()

    for line in reversed(lines):
        match = re.match(regex, line)

        if match:
            regex = yield match.groups()[0]


def get_serial(filename):
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'
    print("ERROR_RE: {}".format(ERROR_RE))
    matcher = match_regex(filename, ERROR_RE)
    print("matcher: {}".format(matcher))
    device = next(matcher)
    print("device: {}".format(device))

    while True:
        bus = matcher.send('(sd \S+) {}.*'.format(re.escape(device)))
        print("bus: {}".format(bus))
        serial = matcher.send('{} \(SERIAL=([^)]*)\)'.format(bus))
        print("serial: {}".format(serial))
        yield serial
        device = matcher.send(ERROR_RE)


for serial_number in get_serial('kernel.log'):
    print(serial_number)



