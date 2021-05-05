dic = {"mutable": "Objects/things whose values can be changed", "immutable": "Objects/things whose value can't be changed",
       "append": "to add something to the end of a written document", "assign": "allocate", "list": "a number of connected items or names written or printed consecutively"}
print(dic.get((input("Enter the word to see it's meaning :- ")),
              "Word not found in the dictionary"))
