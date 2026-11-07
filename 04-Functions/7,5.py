def in_range(value):
    """Check if the value is in the range [0, 100]."""
    return 0 <= value <= 100

print(in_range(int(input("Enter a number between 0 and 100: "))))