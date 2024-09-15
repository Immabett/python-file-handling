# Step 1: Create a file and write text to it
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("This is line 2 with number 42.\n")
        file.write("Line 3 contains the word 'Python'.\n")
except Exception as e:
    print(f"Error occurred: {e}")

# Step 2: Read the file and display its contents
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("File Contents:\n", contents)
except Exception as e:
    print(f"Error occurred: {e}")

# Step 3: Append new text to the file
try:
    with open("my_file.txt", "a") as file:
        file.write("This is appended line 4.\n")
        file.write("This is appended line 5 with the number 88.\n")
        file.write("Appended line 6 mentions 'coding'.\n")
except Exception as e:
    print(f"Error occurred: {e}")

# Step 4: Improved error handling
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("This is line 2 with number 42.\n")
        file.write("Line 3 contains the word 'Python'.\n")
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("File Contents:\n", contents)
    with open("my_file.txt", "a") as file:
        file.write("This is appended line 4.\n")
        file.write("This is appended line 5 with the number 88.\n")
        file.write("Appended line 6 mentions 'coding'.\n")
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You don't have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operation completed.")
