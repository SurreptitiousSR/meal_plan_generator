#!/usr/bin/env python3

# while True:
#            try:
#                cvr = input("Would you like to enter another recipe (y/n)\n")
#                if cvr == "y":
#                    more_recipes = 0
#                elif cvr == "n":
#                    more_recipes = 1 #               else:
#                   cvr = "invalid input"
#                   cvr = int(yn)
#           except ValueError:
#                print("ERROR! You must enter \"y\" for yes and \"n\" for no")
#                continue
#            else:
#                break

def cvr(yn):
    while True:
        try:
            if yn == "n":
                more = 0

            elif valid == "y":
                more = 1
            else:
                valid = "incorrect input"

            valid = int(valid)

        except ValueError:
            print("ERROR! You must enter \"y\" for yes and \"n\" for no")
            continue

        else:
            break

yn = input()
print(yn)

cvr()
