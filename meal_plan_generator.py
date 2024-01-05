#!/usr/bin/env python3
# Meal plan generator - a work in progress
import csv

kg = True
more = 0
# Need to ask if we're inputting a recipe or generating a meal plan
#
def cvr()
    while True:
        valid = input("")
            if valid == "y":



def mode_input():
    while True:
        try:
            global rm
            rm = input("What would you like to do? (r = input recipe, m = generate meal plan): ")
            if rm == "r":
                rm = 0
            elif rm == "m":
                rm = 1
            else:
                rm = "invalid input"
            rm = int(rm)
        except ValueError:
            print("ERROR! You must enter \"r\" for recipie or \"m\" for meal plan\n")
            continue
        else:
            break

def recipe_input():
    more_recipes = 0
    recipe = []

    while (more_recipes < 1):
        ele = input("What's the name of the recipe? ")
        recipe.append(ele)
        recipe.append("+++")

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

# this will append the main ingredient to the list. It's messy and can probably be done in an array or something
#                if r_m_ingredient == 0:
#                   recipe.append("v")
#                elif r_m_ingredient == 1:
#                     recipe.append("m")
#                elif r_m_ingredient == 2:
#                    recipe.append("f")
#                elif r_m_ingredient == 3:
#                    recipe.append("d")
#                elif r_m_ingredient == 4:
#                    recipe.append("o")
            except ValueError:
                print("ERROR! You must enter a valid main ingredient (v = veg, m = meat, f = fish, d = dairy, o = other) ")
                continue
            else:
                break


        while kg == True:
            i = 0
            print("Enter item", i, "= ")
            ing = input()
            recipe.append(ing)
# add a star between ingredients and quantities to help with table formatting later
            recipe,append("*")
            print("Enter quantity of", ing, "=")
            quant = input()
            recipe.append(quant)
            recipe.append("*")

            try:






        while True:
            try:
                cvr = input("Would you like to enter another recipe (y/n)\n")
                if cvr == "y":
                    more_recipes = 0
                elif cvr == "n":
                    more_recipes = 1
                else:
                    cvr = "invalid input"
                    cvr = int(yn)
            except ValueError:
                print("ERROR! You must enter \"y\" for yes and \"n\" for no")
                continue
            else:
                break

# set number of items in the list
        n = int(input("How many items do you have? "))

# Iterate until through the range
        for i in range (0, n):
            print("Enter item",i,"=")
            ele = input()
            recipe.append(ele)
        recipe.append("+++")
        print(recipe)

#program starts here:
print("Meal plan generator v0.1")

mode_input()
if rm == 0:
    recipe_input()
if rm == 1:
   print("you haven't written this part yet Sam")
