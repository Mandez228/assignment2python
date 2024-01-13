A = int(input("Enter the first integer: "))
B = int(input("Enter the second integer: "))
if A < B:
    prod = 1
    for n in range(A, B + 1):
        prod *= n
    print(f"Product of integers from {A} to {B} is: {prod}")
else:
    print("A is less than B, make sure to enter values A < B")



