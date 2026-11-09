





def f(name):
    acronym = ""
    words = name.split()
    for word in words:
        acronym = acronym + word[0]
    return acronym 
print(f("Internet of Things"))
print(f("For your immediate inforamtion"))
