def ackermann(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

def main():
    print(ackermann(3,5))
main()

#This code works by recursively calling itself until it reaches the base case, which is when either n or m is equal to 0. In the base case, the function simply returns the appropriate value. Otherwise, the function returns the result of calling itself with n - 1 and the result of calling itself with n and m - 1.
