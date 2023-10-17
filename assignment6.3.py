try:
    fname = input("Enter a file name: ")
    total = 0
    count = 0

    with open(fname, 'r') as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        number = float(parts[1])
                        total += number
                        count += 1
                    except ValueError:
                        print(f"Warning: Invalid number on line - {line}")

    if count > 0:
        average = total / count
        print(f"Average spam confidence: {average:.4f}")
    else:
        print("No valid X-DSPAM-Confidence lines found in the file.")

except FileNotFoundError:
    print(f"Error: File '{fname}' not found")

except Exception as e:
    print(f"An error occurred: {e}")