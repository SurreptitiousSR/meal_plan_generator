#!/usr/bin/env python3
# Meal plan generator - a work in progress
import csv
# kg keep going

rm = "x"
valid = 1
recipe = []
# Function to check for a valid yes or no response from the user
def cvr(response):
    global valid
    while True:
        try:
            if response == "n":
                valid = 0

            elif response == "y":
                valid = 1

            else:
                valid = "incorrect input"

            valid = int(valid)

        except ValueError:
            print("ERROR! You must enter \"y\" for yes and \"n\" for no")
            continue

        else:
            break


def write_table():
    with open("meal_plan.csv", "w") as f:
        write = csv.writer(f)
        write.writerow(recipe)

# Need to ask if we're inputting a recipe or generating a meal plan
def mode_input():
    global rm
    while True:
        try:
            rm = input("What would you like to do? (r = input recipe, m = generate meal plan, q = quit): ")
            if rm == "r":
                rm = 0

            elif rm == "m":
                rm = 1

            elif rm == "q":
                quit()

            else:
                rm = "invalid input"

            rm = int(rm)

        except ValueError:
            print("ERROR! You must enter \"r\" for recipie, \"m\" for meal plan or \"q\" to quit \n")
            continue
        else:
            break

def recipe_input():
    recipe.append("+++")
    ele = input("What's the name of the recipe? ")
    recipe.append(ele)
    recipe.append("*")

    while True:
        try:
            r_m_ingredient = input("What's the main igredient? (v = veg, m = meat, f = fish, d = dairy, o = other) ")
            if r_m_ingredient == "v":
                recipe.append(r_m_ingredient)
                r_m_ingredient = 0

            elif r_m_ingredient == "m":
                recipe.append(r_m_ingredient)
                r_m_ingredient = 1

            elif r_m_ingredient == "f":
                recipe.append(r_m_ingredient)
                r_m_ingredient = 2

            elif r_m_ingredient == "d":
                recipe.append(r_m_ingredient)
                r_m_ingredient = 3

            elif r_m_ingredient == "o":
                recipe.append(r_m_ingredient)
                r_m_ingredient = 4

                r_m_ingredient = int(r_m_ingredient)

        except ValueError:
            print("ERROR! You must enter a valid main ingredient (v = veg, m = meat, f = fish, d = dairy, o = other) ")
            continue

        else:
            break


    while valid == 1:
        i = 0
        ing = input("Enter item: ")
        recipe.append(ing)
# add a star between ingredients and quantities to help with table formatting later
        recipe.append("*")
        quant = input("Enter quantity: ")
        recipe.append(quant)
        recipe.append("*")
# this will change valid to 1 for y and 0 for n
        cvr(response = input(("Another item? (y/n) ")))

#program starts here:
print("Meal plan generator v0.1")


while True:
    mode_input()
    if rm == 0:
        recipe_input()
        write_table()
# resets valid to 1 to allow while loop after main ingredient to run
        valid = 1

    elif rm == 1:
        print("you haven't written this part yet Sam")
        break
