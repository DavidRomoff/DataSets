

import pandas as pd
import pip
pip.main(["install", "openpyxl"])

starwars = \ 
pd.read_csv('https://github.com/DavidRomoff/DataSets/raw/main/starwars.csv')

cars = \
pd.read_csv('https://github.com/DavidRomoff/DataSets/raw/main/cars.csv')

houseprices = \
pd.read_excel('https://github.com/DavidRomoff/DataSets/raw/main/IOWA_House_Prices.xlsx')

lendingclub = \
pd.read_excel('https://github.com/DavidRomoff/DataSets/raw/main/Lending_Club.xlsx')

