def return_spam(name, bases, namespace):
    """Ignore all arguments and return 'spam' """
    print('Call return_spam({!r})'.format((name, bases, namespace)))
    return 'spam'

