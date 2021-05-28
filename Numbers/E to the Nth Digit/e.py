# Finding E to the Nth Digit
# ---------------------------
# Just like the previous problem, but with e instead of PI. 
# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go.
# ---------------------------
# Ref - https://www.mathsisfun.com/numbers/e-eulers-number.html

def nth_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError as e:
            print("Not an integer! Try again...")

def e_gen(n):
    e = (1 + 1 / n) ** n
    return e

def e_decimal(func, i):
    e_lst = [x for x in str(func)]

    if i == 0:
        print("".join(e_lst[0]))
    elif i > 0 and i < len(e_lst):
        print("".join(e_lst[0:i+2]))
    else:
        print("Out of range!")

print("Display e to n decimal places.")
e_decimal(e_gen(100000), nth_input("Enter the value for n "))
