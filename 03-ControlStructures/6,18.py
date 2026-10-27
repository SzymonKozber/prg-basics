x = int(input("Enter the coordinate x: "))
y = int(input("Enter the coordinate y: "))
if x > 0 and y > 0:
    print(f'Point P({x},{y}) is in the first quandrant of the coordinate system')
if x > 0 and y < 0:
    print(f"Point P({x},{y}) is in the fourth quandrant of the coordinate system")
if x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quandrant of the coordinate system")
if x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quandrant of the coordinate system")
