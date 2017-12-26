class SentenceEndsWith:
    def __init__(self, characters):
        self.punctuation = characters

    def __call__(self, sentence):
        print("Calling {!r}".format(self.__call__))
        return sentence[-1] in self.punctuation


