#Ask the user for a filename and handle errors,
# if it doesn’t exist or can’t be read.

filename = input("Enter the filename: ")  # Prompting the user for a file name

try:
    with open(filename, 'r') as file:  # Attempting to open the file in read mode.
        content = file.read()
        print(content)                 # If the file is opened successfully, read its content and print it.

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: You do not have permission to read this file.")
