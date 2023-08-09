# UTF-8 Validation

## Problem Description

The UTF-8 Validation problem involves validating whether a given list of integers represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding that can represent various characters from different languages and symbols.

To solve the UTF-8 Validation problem, you need to determine whether the sequence of bytes provided follows the rules of valid UTF-8 encoding.

## Rules for Valid UTF-8 Encoding

1. A valid UTF-8 character can be 1 to 4 bytes long.
2. For a character with N bytes, the first byte starts with N 1s and a 0 (N consecutive "1" bits followed by a "0" bit), while the following N-1 bytes start with "10".
3. The remaining bytes must all start with the bit pattern "10".

## Approach

To solve this problem, you can follow these steps:

1. Initialize a variable to keep track of the number of bytes remaining for the current character (initially set to 0).
2. Iterate through each byte in the given sequence of bytes.
   - If the `bytes_to_follow` variable is 0, determine the number of bytes for the current character based on the first byte's pattern.
   - If the `bytes_to_follow` variable is not 0, check that the current byte starts with the pattern "10".
   - Update the `bytes_to_follow` variable accordingly.
3. After processing all bytes, check if the `bytes_to_follow` variable is 0. If it is, the sequence is valid; otherwise, it's not.

## Example Implementation

Here's an example of how you could implement the UTF-8 validation algorithm in Python:

```
python
def validUtf8(data):
    bytes_to_follow = 0
    
    for num in data:
        if bytes_to_follow == 0:
            if num >> 5 == 0b110:
                bytes_to_follow = 1
            elif num >> 4 == 0b1110:
                bytes_to_follow = 2
            elif num >> 3 == 0b11110:
                bytes_to_follow = 3
            elif num >> 7:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            bytes_to_follow -= 1
    
    return bytes_to_follow == 0

```

## Usage

You can use the validUtf8 function to check whether a given sequence of bytes represents a valid UTF-8 encoding. Provide the sequence as a list of integers to the function, and it will return True if the sequence is valid and False otherwise.

```
data = [197, 130, 1]  # Example input
result = validUtf8(data)
print(result)  # Output: True

```
## Resources

* UTF-8 on Wikipedia
* UTF-8 Encoding

Remember that this README.md file provides a general overview of the UTF-8 Validation problem and its solution approach. You can adapt and expand it based on your specific implementation and requirements.

Feel free to add code explanations, test cases, and any additional information that may be relevant to your project or task.
