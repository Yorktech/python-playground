import re

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

# Sample data
data = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# Process each line in the data
for line in data:
    first_number, last_number = find_first_and_last_single_digit_numbers(line)
    print(f"Line: '{line}' - First number: {first_number}, Last number: {last_number}")
