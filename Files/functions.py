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

# function annotations
a = 'hi'
a = 45

def sum_of_product(a: int, b:int) -> int:
    return a + b
c = sum_of_product(3,4)
c =sum_of_product('Hello', "there")