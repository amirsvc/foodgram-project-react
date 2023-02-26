import csv
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
print(os.getcwd())
from recipes.models import Ingredient


with open('../../foodgram-project-react/data/ingredients.csv') as f:
    records = 0
    reader = csv.reader(f)
    for row in reader:
        name, measurement_unit = row
        Ingredient.objects.get_or_create(
            name=name, measurement_unit=measurement_unit
        )
        records += 1

print(f'{records} was transferred!')
