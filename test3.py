import csv
import model
import os
from datetime import *

filename = '17l.txt'
rows = model.FileHandler.read_csv_file(filename)

for day in model.InputConverter.pl_weekdays:
    print(model.InputConverter.get_week_day_index(day))



