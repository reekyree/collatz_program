# This program asks the user to enter a number. 
# The program will indefinitely use a math function
# on the entered number until the result is finally 1.
# The program will use a different equation on each number
# depending on whether the number is even or odd.


def main():
    number = int(input('Enter a number: '))
    result = collatz(number)
    while result != 1:
        result = collatz(result)

# Create the collatz function
def collatz(num):
    if num % 2 == 0:
        result = num // 2
        print(result)
        return result
    elif num % 2 == 1:
        result = 3 * num + 1
        print(result)
        return result

main()

