def reverse_iter(seq):
    position = len(seq) -1
    while True:
        if position < 0:
            raise StopIteration
        yield seq[position]
        position -= 1

class BackwardsSequence(list):
    def __iter__(self):
        return reverse_iter(self)
