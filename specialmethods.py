PYTHON_RELEASES = [
            'Python 3.6.1  2017-03-21',
            'Python 3.5.3  2017-01-17',
            'Python 3.4.6  2017-01-17',
            'Python 3.3.6  2014-10-12',
            'Python 3.2.6  2014-10-12',
            'Python 3.1.5  2012-04-09',
            'Python 3.0.1  2009-02-13',
            'Python 2.7.13 2016-12-17',
            'Python 2.6.7  2011-06-03',
            'Python 2.5.6  2011-05-26',
            ]
class ReleaseFields:
    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        return self.data[0:6]

    @property
    def version(self):
        return self.data[7:12]

    @property
    def date(self):
        return self.data[13:23]
