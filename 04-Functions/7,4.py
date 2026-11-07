def letter_e_count(string):
    """
    Function counts the number of letters 'e' in a string.
    :param string: string to count letters 'e'
    :return: number of letters 'e' in a string
    """
    count = 0
    for letter in string:
        if letter == 'e':
            count += 1
    return count

print(letter_e_count("Hello, welcome to the world of programming!"))  