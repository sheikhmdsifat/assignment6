try:
    folder_name = input("Enter a file name: ")

    with open(folder_name, 'r') as file:
        line_number = 1
        
        for line in file:
            print(f"LINE NUMBER : {line_number}")
            print(line.upper(), end='')
            line_number += 1

except FileNotFoundError:
    print(f"Error: File '{folder_name}' not found")

except Exception as e:
    print(f"An error occurred: {e}")
