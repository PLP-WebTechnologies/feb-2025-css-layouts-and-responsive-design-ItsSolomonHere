# This script reads a file, modifies its content, and writes the modified content to a new file.
# It handles various exceptions that may occur during file operations.
# Import necessary modules
def modify_file_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, "r") as original_file:
            content = original_file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)

        # Write modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content saved to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: The file could not be read or written.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()