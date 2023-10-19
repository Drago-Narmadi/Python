def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            encrypted_char_code = (char_code + shift) % 26
            encrypted_char = chr(encrypted_char_code + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    
    for char in encrypted_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            decrypted_char_code = (char_code - shift) % 26
            decrypted_char = chr(decrypted_char_code + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def main():
    choice = input("Choose an option (1 for Encryption, 2 for Decryption): ")
    
    if choice == '1':
        plain_text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_encrypt(plain_text, shift)
        print("Encrypted Text:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice. Please choose 1 for Encryption or 2 for Decryption.")

if __name__ == "__main__":
    main()
