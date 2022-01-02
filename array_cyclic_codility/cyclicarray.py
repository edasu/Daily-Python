#example pop()
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# remove the element at index 2
removed_element = prime_numbers.pop(2)

print('Removed Element:', removed_element)
print('Updated List:', prime_numbers)

# Output:
# Removed Element: 5
# Updated List: [2, 3, 7]

#SOLUTION
A = [3, 8, 9, 7, 6]
K = 3

def solution(A, K):
    for i in range(0, K):
        if A == []:
            return A
        A.insert(0, A.pop())
return A

print(solution(A, K))
