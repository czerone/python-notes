"""
This is to add two number and return the result
"""
def add_num(first_num, sec_num, third_num=0):
    """
    >>> add_num(1, 2)
    3
    >>> add_num(4, 5, 6)
    15
    """
    result = first_num + sec_num + third_num
    return result

if __name__ == '__main__':
    RESULT = add_num(2, 3)
    print RESULT
