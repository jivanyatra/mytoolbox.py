'''
This is my (jivanyatra) personal toolbox for python. I will accumulate useful
functions, paradigms, etc. in this module for use later in projects.
'''

def read_words(file_name, delimiter=''):
    '''A generator that parses a file and yields words.
    Call this function with a filename to be opened as read-only,
    and specify an optional delimiter for splitting lines into words.
    
    Can be handed to collections.Counter() to count word frequency.
    Can be used in a genexp in any() to return words belonging to a subset.
    '''
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.split(delimiter):
                yield word

class Fib():
    '''Fibonacci sequence iterator, goes until (but not including) max'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

def fibgen(max=None):
    """Fibonacci numbers generator"""
    """If no value is used in calling, will return infinitely"""
    a, b, i = 0, 1, 0
    while True:
        if max and (i > max): return
        yield a
        a, b = b, a + b
        i += 1