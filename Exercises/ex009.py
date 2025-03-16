# Your Student ID: 230543606
# Your Name and Surname: Saed Abdul Rahim
# ex9.py
choice = input("Convert (C to F) or (F to C)? ").strip().lower()
temp = float(input("Enter temperature: "))
if choice == "c to f":
    print(f"{temp}°C is {(temp * 9/5) + 32:.2f}°F")
elif choice == "f to c":
    print(f"{temp}°F is {(temp - 32) * 5/9:.2f}°C")
else:
    print("Invalid choice")
