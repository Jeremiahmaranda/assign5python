# file_handling_assignment.py

def create_file():
    try:
        # Create a new file and write to it
        with open("my_file.txt", 'w') as file:
            file.write("Hello, World!\n")
            file.write("This is line 2 with a number: 42\n")
            file.write("Another line with text.\n")
        
def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    

def append_to_file():
    try:
        # Open the file in append mode and add more content
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2: 100\n")
            file.write("Appending line 3 with some more text.\n")
        
if __name__ == "__main__":
    create_file()    # Create and write to the file
    read_file()      # Read and display the contents
    append_to_file() # Append additional content
