#!/usr/bin/env python3

recipe = []

n = int(input("how many items"))

for i in range (0, n):
    print("enter item", i, "=")
    ele = input()
    recipe.append(ele)
print(recipe)
