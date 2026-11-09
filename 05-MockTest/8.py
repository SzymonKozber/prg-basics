

def f(palindrom):
    if palindrom == palindrom[::-1]:
        return True
    return False
print(f("radar"))