


def f(binary_number):
    for char in binary_number:
        if char not in ['1', '0']:
            return False
    return True


