print("\n* * * * * * * * Guess a number between 1 to 1000 * * * * * * * * * * *")
n = 395
g = 9
i = 0
while(i < g):
    i += 1
    num = int(input("\nEnter your guessed number -: "))
    if num > n:
        print("\nActual number is smaller than your guess\nNumber of guesses left -: ", g-i)
    elif num < n:
        print("\nActual number is greater than your guess\nNumber of guesses left -: ", g-i)
    else:
        print("\nYou WON!!\nNumber of guesses used - : ", i)
        break
if i >= g:
    print("\nGame Over\nYou Lost!!\nBetter luck next time")
