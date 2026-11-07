def ft_and_inch_to_cm(ft, inch):
    total_inches = ft * 12 + inch
    return total_inches * 2.54

def cm_to_inch(n):
    return n/2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2ft 6in = {ft_and_inch_to_cm(2, 6)}cm')
    print(f'532cm = {cm_to_inch(532)}in')

