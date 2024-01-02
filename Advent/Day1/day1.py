import re



# Path to the Python file
file_path = '/workspaces/python-playground/functions/Advent/data.txt'
total =0 
def find_first_and_last_single_digit_numbers(text):
    # Find all single-digit numbers in the text
    numbers = re.findall(r'\d', text)

    # Check if we found any numbers
    if not numbers:
        return None, None  # No numbers found

    # The first number is the first element, and the last number is the last element
    first_number = numbers[0]
    last_number = numbers[-1]

    return first_number, last_number

# Read and process the file line by line
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Process the line
        first_number, last_number = find_first_and_last_single_digit_numbers(line)
        combined = first_number + last_number;
        total += int(combined)
        print("First number:", first_number)
        print("Last number:", last_number)
        print(combined)
        print(total)

