# Documentation for `generate_password` Function

## Function Name:
`generate_password`

## Purpose:
This function generates a random password with customizable options for length, inclusion of uppercase letters, numbers, and symbols.

## Parameters:
- **`length`** *(int)*: The length of the password to generate. The default value is 8.
  - *Example*: `length=12`
  
- **`use_uppercase`** *(bool)*: If `True`, the password will include uppercase letters (A-Z). The default value is `True`.
  - *Example*: `use_uppercase=False`
  
- **`use_numbers`** *(bool)*: If `True`, the password will include numeric digits (0-9). The default value is `True`.
  - *Example*: `use_numbers=False`
  
- **`use_symbols`** *(bool)*: If `True`, the password will include special symbols (!, @, #, etc.). The default value is `True`.
  - *Example*: `use_symbols=True`

## Returns:
- **`password`** *(str)*: A randomly generated password string that adheres to the provided options for length and character types.

## Exceptions:
- **`ValueError`**: Raised in the following cases:
  1. If no character sets (lowercase, uppercase, numbers, or symbols) are selected.
  2. If the specified `length` exceeds the number of unique characters available based on the chosen character sets.

## Usage Example:
```python
import json

# Load options from a JSON file
with open("./information.json", "r") as file:
    data = json.load(file)

# Generate the password based on user-provided options
password = generate_password(length=data['length'],
                             use_uppercase=data['use_uppercase'],
                             use_numbers=data['use_numbers'],
                             use_symbols=data['use_symbols'])

print(f"Generated password: {password}")
