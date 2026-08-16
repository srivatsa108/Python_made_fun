#code for try except block

try:
    1/0
except ZeroDivisionError:
    print("You can't divide by zero!")
    
#try catch and finally block

my_dict = {"name": "John", "age": 30}

try:
    value=my_dict["name"]
except  IndexError:
    print("IndexError: The index does not exist in the dictionary.")
except KeyError:
    print("KeyError: The key does not exist in the dictionary.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No error Occured")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")