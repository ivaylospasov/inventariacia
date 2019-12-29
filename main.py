#!/usr/bin/env python3
import pandas as pd

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

while True:
    inventaren = input("Въведете инвентарен номер: ")

    df = pd.read_csv('cmol.csv')
    inv_data = df[['inv', 'vidname', 'nameda', 'broi', 'molname']]
    df_cols = ['номер', 'вид', 'име', 'брой', 'МОЛ']
    inv_data.columns = df_cols
    booleans = []
    for inv_number in inv_data['номер']:
        #inv_number = inv_number.strip()
        #if inv_number == str(inventaren):
        if str(inv_number) == inventaren:
        # if int(inv_number) == int(inventaren):
             booleans.append(True)
        else:
            booleans.append(False)
    #is_long = inv_data['номер'] == str(inventaren)
    is_long = pd.Series(booleans)
    print(inv_data[is_long])
