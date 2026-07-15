#Empty and None checks

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("The list is empty.")

if empty_tuple == ():
    print("The tuple is empty.")

if not empty_string:
    print("The string is empty.")

if not nothing:
    print("The variable is None.")