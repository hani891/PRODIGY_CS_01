def caesar_cipher(text, shift, direction):
    result = ""
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure shift is within the range of the alphabet
            new_char_code = ord(char) + shift_amount if direction == "encrypt" else ord(char) - shift_amount
            
            # Handle wrap-around for uppercase and lowercase letters
            if char.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                elif new_char_code < ord('A'):
                    new_char_code += 26
            elif char.islower():
                if new_char_code > ord('z'):
                    new_char_code -= 26
                elif new_char_code < ord('a'):
                    new_char_code += 26

            result += chr(new_char_code)
        else:
            result += char  # Non-alphabet characters are added as they are

    return result

# Input from user
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
direction = input("Do you want to 'encrypt' or 'decrypt' the text? ")

# Output the result
output = caesar_cipher(text, shift, direction)
print(f"The resulting text is: {output}")
