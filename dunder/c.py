#c.py
#context manager implementation

class ProgressBar:
    """Progress bar that normalizes progress to [0 - 100] scale"""

    def __init__(self, max_val):
        print("Initializing Class ProgressBar")
        self._curr_val = 0.0
        self._done_val = 100.0
        self._max_val = float(max_val)

    def __enter__(self):
        """Start of context manager, 'with' statement"""
        print("Entering context manager 'with statement' __enter__")
        self._curr_val = 0.0
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """End of context manager, leaving 'with' statement"""
        print("End of context manager, leaving 'with' statement")
        self.update(self._max_val)
        return False

    def update(self, value):
        if value >= self._max_val:
            self._curr_val = self._done_val

        else:
            self._curr_val = (value / self._max_val)

        print('%s' % self._curr_val)


