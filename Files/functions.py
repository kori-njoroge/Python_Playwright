def greeting():
    print ("Hello World")
    
greeting()


# //functions with parameters
def greeting1( name ):
    print (f"Hello World, {name}")
    
greeting1()

# return items from a function
def sum_of(a, b):
    sum = (a+b)
    return sum
    
c = sum_of(3,4)