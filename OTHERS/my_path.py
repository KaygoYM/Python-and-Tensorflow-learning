def square(x):
    '''
    Squares a number and returns the result

    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x**2

if __name__=='__main__':
    import doctest,my_path
    doctest.testmod(my_path)
