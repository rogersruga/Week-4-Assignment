# Open the input file in read mode
with open('input.txt', 'r') as file:
    content = file.read()

print(content)


# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open('output.txt', 'w') as file:
    file.write(modified_content)

print("File has been read and modified content written to 'output.txt'.")