#File Handling code
#The default mode in file handling is read only mode. If we want to write to a file, we need to open it in write mode or append mode.
# To execute  change the directory to the location of the file and run the command "python filehandling.py" in the terminal.

handle=open("sample.txt","r")  # Open the file in read mode
data=handle.read()  # Read the contents of the file
print(data)  # Print the contents of the file
handle.close()  # Close the file