'''
The Tribonacci sequence is the big brother of the Fibonacci sequence.

Unlike the Fibonacci sequence, each term of the Tribonacci sequence is formed by adding the three previous terms.
Given a signature array/list, the first elements of the sequence, your task is to return the first n elements of the Tribonacci sequence.

For example:
signature = [1, 1, 1], n = 10, the Tribonacci sequence
would be: [1, 1 ,1, 3, 5, 9, 17, 31, 57, 105]
'''




def tribonacci(signature, n):
    if n > 0:
        for i in range(3, n):
            signature.append(signature[i-1] + signature[i-2] + signature[i-3])
        return signature[:n]
    else:
        return []
    


print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]