def reverse_num(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = (rev * 10) + digit
        temp = temp // 10
    return rev

n = int(input("Enter a number you want to reverse: "))
reversed_number = reverse_num(n)
print("Reversed number:", reversed_number)
