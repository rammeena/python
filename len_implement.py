mylist = [1,2,3,4,5]

class CustomeSequence:
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBackwards:
    def __reversed__(self):
        return "BACKWARDS!"

