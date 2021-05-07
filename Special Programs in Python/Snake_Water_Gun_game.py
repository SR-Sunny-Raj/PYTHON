import random
print("\n* * * * * * * * * * * Snake , Water , Gun Game * * * * * * * * * * *\nThere are 10 round in this game\n")
i = 1
ys = 0
cs = 0
lst = ["s", "w", "g"]
while(i <= 10):
    cchoice = random.choice(lst)
    ychoice = input(
        "\nEnter your choice :- \nFor Snake - s\nFor Water - w\nFor Gun - g\n")
    if(cchoice == ychoice):
        print(f"\nRound Tie\nCurrent score -:\nComputer - {cs}\nYou - {ys}")
    elif cchoice == "s" and ychoice == "w" or cchoice == "w" and ychoice == "g" or cchoice == "g" and ychoice == "s":
        cs += 1
        print(
            f"\nComputer Won this Round\nCurrent score -:\nComputer - {cs}\nYou - {ys}")
    elif cchoice == "w" and ychoice == "s" or cchoice == "g" and ychoice == "w" or cchoice == "s" and ychoice == "g":
        ys += 1
        print(
            f"\nYou Won this Round\nCurrent score -:\nComputer - {cs}\nYou - {ys}")
    i += 1

print(f"\nFinal Score -:\nComputer - {cs}\nYou - {ys}")
if(cs == ys):
    print("\n* * * * * * * Game Tie * * * * * * *")
elif(cs > ys):
    print("\n* * * * * * * Computer won the game * * * * * * *")
else:
    print("\n* * * * * * * You Won the game * * * * * * *")
