def f(palindrome):
    return palindrome == palindrome[::-1]

print(f("radar"))     
print(f("12-11-21"))  
print(f("book"))      






























def f(palindrom):
    if palindrom == palindrom[::-1]:
        return True
    return False
print(f("radar")) 
print(f("12-11-21")) 
print(f("book")) 