# Open the input file in read mode
with open("emails.txt", "r") as file:
    # Read all lines and store them in a list
    lines = file.readlines()

# Remove duplicate lines while preserving order
unique_lines = list(dict.fromkeys(lines))

# Write the unique lines back to the file (or a new file)
with open("output.txt", "w") as file:
    file.writelines(unique_lines)

print("Duplicates removed successfully!")
