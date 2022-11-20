# Programmed by: Lee Anne Y. Angeles

# List
msg = []
key = []
add = []
mod = []
cipher = []

# Input statement
message = input("\nEnter your message: ").lower()
keyword = input("Enter your keyword: ").lower()
k = keyword

for i in range(len(message)):
    keyword = keyword + keyword
    keyword = keyword[0:len(message)]

    key_value = ord(keyword[i]) - 97
    key.append(key_value)
    msg_value = ord(message[i]) - 97
    msg.append(msg_value)

    x = ((ord(message[i]) - 97) + (ord(keyword[i]) - 97))
    add.append(x)
    y = ((ord(message[i]) - 97) + (ord(keyword[i]) - 97)) % 26
    mod.append(y)
    y += ord('A')
    cipher.append(chr(y).upper())

# Print Statement
print(f"\n{'Message': <15s}{':': <5s}", message.upper(), ' '.join(str(i) for i in msg))
print(f"\n{'Key': <15s}{':': <5s}", k.upper(), '  '.join(str(i) for i in key))
print(f"\n{'Add': <15s}{':': <5s}", ' '.join(str(i) for i in add))
print(f"\n{'Mod': <15s}{':': <5s}", ' '.join(str(i) for i in mod))
print(f"\n{'Ciphertext': <15s}{':': <5s}", ' '.join(cipher))



