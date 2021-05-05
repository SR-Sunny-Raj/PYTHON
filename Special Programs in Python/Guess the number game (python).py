import random
lb = 1
ub = 500
g = 9
print("\n* * * * * * * * Guess a number between {} to {} in {} gusses * * * * * * * * * * *".format(lb, ub, g))
n = random.randint(lb, ub)
# n = 395
i = 0
while(i < g):
    i += 1
    num = int(input("\nEnter your guessed number -: "))
    if num > ub or num < lb:
        print("Please enter your guess in the specified range")
        i -= 1
    elif num > n:
        print("\nActual number is smaller than your guess\nNumber of guesses left -: ", g-i)
    elif num < n:
        print("\nActual number is greater than your guess\nNumber of guesses left -: ", g-i)
    else:
        print("\n* * * * * * * * You WON!! * * * * * * * *\nNumber of guesses used - : ", i)
        i -= 1
        break
if i >= g:
    print(
        "\nActual number was -: {}\n\n* * * * * * * * Game Over * * * * * * * *\n* * * * * * * * You Lost!! * * * * * * * *\n* * * * * Better luck next time * * * * * ".format(n))
