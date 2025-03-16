# Your Student ID: 230543606
# Your Name and Surname: Saed Abdul Rahim
# ex7.py
string = input("Enter a string: ")
frequency = {char: string.count(char) for char in sorted(set(string))}
print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
