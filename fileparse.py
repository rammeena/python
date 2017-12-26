#!/usr/local/python-envs/Py3env/bin/python
import sys
def total_size():
    f = sys.argv[1]
    with open (f) as f:
        rbd_list = [float(line.split()[0]) for line in f.readlines()]
    print('Total Consumed size in Ceph: ', sum(rbd_list)/1024,'MB')

if __name__ == "__main__":
    total_size()
