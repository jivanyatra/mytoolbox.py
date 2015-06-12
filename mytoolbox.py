'''
This is my (jivanyatra) personal toolbox for python. I will accumulate useful
functions, paradigms, etc. in this module for use later in projects.
'''

def read_words(file_name, delimiter=''):
    '''A generator that parses a file and yields words.
    Call this function with a filename to be opened as read-only,
    and specify an optional delimiter for splitting lines into words.'''
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.split(delimiter):
                yield word

