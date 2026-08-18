#Functions
#Functions are collection of things that do a particular task.
def func():
    print("Inside the function")

def add(a,b):
    return a+b
print(add(1,3))

#If you dont know the exact number of arguments you can use *args and **kwargs

def many(*args , **kwargs):
    print(args) # Returns a tuple of arguments
    print (kwargs) # Returns a dictionary of keyword arguments
    
many(1,2,3,4,5, name = "John", age = 30)
