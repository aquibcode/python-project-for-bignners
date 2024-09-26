def second_largest(lst: list) -> int:
    '''
    Given a list of integers, return the second largest number in the list.
    Consider that the list contains at least two integers.

    Arguments:
    lst: list - the input list of integers

    Return:
    int - the second largest number in the list

    Example:
    >>> second_largest([1, 2, 3, 4, 5])
    4
    '''
    # Initialize the two largest numbers
    largest = float('-inf')
    second_largest = float('-inf')
    for num in list:
        if num > largest:
            second_largest = num
            num = largest
        elif num > second_largest and num< largest:
            second_largest = num
    return second_largest        
