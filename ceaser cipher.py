n = str(input("Enter the Text: "))
print("Normal text: ",n)
x=int(input("Key value: "))
print("Cipher text: ")
for i in n:
    if i.isalpha():
        cipher=chr((ord(i)-ord('a' if i.islower() else 'A') +x)%26+ord('a' if i.islower() else 'A'))
        print(cipher,end='')
    else:
        print(i,end='')
