key = int(input("Enter key: "))
message = input("Enter message: ")

encrypted_message = ""

for char in message:
    if char.isalpha():  
        if char.isupper():
            shift = ord('A')
        else:
            shift = ord('a')
        encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
    else:
        encrypted_message += char 

print("Result:", encrypted_message)
