def file_io(file):
    with open(file, 'r') as f:
        print(type(f))
        for line in f:
            print(line)

if __name__ == '__main__':
    import sys
    file_io(sys.argv[1])
