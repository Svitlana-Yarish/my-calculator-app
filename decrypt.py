key = int(input("Enter key: "))
message = input("Enter message: ")

decrypted_message = ""

for char in message:
    if char.isalpha():  
        if char.isupper():
            shift = ord('A')
        else:
            shift = ord('a')
        decrypted_message += chr((ord(char) - shift - key) % 26 + shift)
    else:
        decrypted_message += char 

print("Result:", decrypted_message)
