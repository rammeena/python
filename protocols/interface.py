class Team:
    def __init__(self, members):
        self._members = members
        print(self._members)

    def __len__(self):
        return len(self._members)

    def __contains__(self, member):
        return member in self._members

    def __repr__(self):
        return 'Team({!r})'.format(self._members)

