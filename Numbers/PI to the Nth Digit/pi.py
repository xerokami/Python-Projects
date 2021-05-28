# Finding PI to the Nth Digit
# ---------------------------
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

import math

print("Display PI between 0-15 decimal places")

while True:
    try:
        n = int(input("Generate PI to what decimal place? "))
        n = int(n)
        break
    except ValueError:
        print("Not a valid integer! Try again...")

pi_lst = [x for x in str(math.pi)]

if n == 0:
    print(float("".join(pi_lst[0])))
elif n > 0 and n < 16:
    print(float("".join(pi_lst[0:n+2])))
else:
    print("Out of range!")
