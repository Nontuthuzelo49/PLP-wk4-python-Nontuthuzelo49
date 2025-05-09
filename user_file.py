def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., converting text to uppercase)
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content saved to {output_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except IOError:
        print("Error: Unable to read or write the file.")
        
# Example usage
modify_file('input.txt', 'output.txt')

def read_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            print("File content:\n", file.read())
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
read_file()
