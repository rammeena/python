class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only Integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)

