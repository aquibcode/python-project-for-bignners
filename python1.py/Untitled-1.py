def unflatten(t: tuple, m: int, n: int) -> tuple:
    '''Given a flat tuple of length m*n, convert it into a tuple of tuples 
    with dimensions m x n.

    Args:
        t (tuple): Flat tuple of length m*n.
        m (int): Number of rows in resulting tuple of tuples.
        n (int): Number of columns in resulting tuple of tuples. 

    Returns:
        tuple: A tuple of tuples with dimension m x n. 

    Examples:
    >>> unflatten((1, 2, 3, 4, 5, 6), 2, 3)
    ((1, 2, 3), (4, 5, 6))
    >>> unflatten((1, 2, 3, 4), 2, 2)
    ((1, 2), (3, 4))
    '''
    # Create a list of tuples where each tuple has n elements
    result = tuple(t[i*n:(i+1)*n] for i in range(m))
    return result
print(unflatten((1, 2, 3, 4, 5, 6), 2, 3))