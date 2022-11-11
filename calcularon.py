import numpy as np
import matplotlib.pyplot as plt

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print("Select operation.")
print("1.+")
print("2.-")
print("3.*")
print("4.%")
rec=np.recarray(100, dtype=[
('solution','f8', 20),
('ys','f8',20)
])
i=0
while True:
    choice = input("Enter choice(+/-/*/%): ")
    if choice in ('+', '-', '*', '%'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            solution = (num1, '+', num2, '=', add(num1, num2))

        elif choice == '-':
            solution = (num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '*':
            solution = (num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '%':
            solution = (num1, '/', num2, '=', divide(num1, num2))
        
        ys = float(input("what's your sulotion?"))

        print("the solution is " ,solution)
        if solution==ys:
            print("you were correct")
        elif solution!=ys:
            print("you were wrong")

        plt.figure()
        plt.title('constribution')
        plt.hist(['ys'], bins=np.linspace(0,10,100))
        plt.hist(['solution'], bins=np.linspace(0,10,100))
        plt.show()

        i=i+1


        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

plt.figure()
plt.title('constribution')
plt.hist(['ys'], bins=np.linspace(0,10,100))
plt.hist(['solution'], bins=np.linspace(0,10,100))
plt.show()


