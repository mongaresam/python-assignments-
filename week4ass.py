file = open('index.txt', 'w')

file.write('This is a new file created in week 4.\n')
file.write('This file is part of the Python course.\n')
file.write('We are learning about file handling in Python.\n')
file.write('Appending some additional content.\n')
file.write('File created and written successfully.\n')
file.write('File content:\n')

file = open('index.txt', 'r')
data = file.read()
print(data)

def total_letters(filename):
	with open(filename, 'r') as f:
		content = f.read()
		return sum(c.isalpha() for c in content)

filename = 'index.txt'
print ("total letters;", total_letters(filename))

try:
    file = open('index.txt', 'r')
    content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print("The file does not exist.")


    # File Read & Write Challenge  Error Handling Lab 

def total_letters(filename):
    """Count total alphabet letters in a file."""
    with open(filename, 'r') as f:
        content = f.read()
        return sum(c.isalpha() for c in content)

def main():

    filename = input("index.txt: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📖 Original File Content:")
            print(content)

    
        print("\n🔤 Total letters:", total_letters(filename))

        # Step 4: Modify content (uppercase)
        modified_content = content.upper()

        # Step 5: Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"\n✅ Modified content saved to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
