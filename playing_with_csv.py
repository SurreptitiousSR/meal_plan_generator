#!/usr/bin/env python3
import csv

def data_table():
    fields = ["Category", "Ingredients", "Quantity"]
    with open("recipes.csv","w") as f:
        write = csv.writer(f)
        write.writerow(fields)

data_table()
