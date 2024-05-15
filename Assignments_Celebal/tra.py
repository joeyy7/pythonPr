# Create lower triangular, upper triangular and pyramid containing the "*" character.
def lowerTriangle(n):
    for i in reversed(range(n)):
        print("* "*(i+1))

def upperTriangle(n):
    for i in range(n):
        print("* "*(i+1))

def pyramid(n):
    for i in range(n):
        print(" "*(n-i)+"* "*(i+1))

n=int(input("Enter the number: "))

print("\nLower Triangle: ")
lowerTriangle(n)

print("\nUpper Triangle: ")
upperTriangle(n)

print("\nPyramid: ")
pyramid(n)