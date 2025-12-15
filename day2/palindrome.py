num = input("Enter a 5-digit number: ")

if len(num) != 5 or not num.isdigit():
    print("Error: Please enter a valid 5-digit number.")
else:
    if num == num[::-1]:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
