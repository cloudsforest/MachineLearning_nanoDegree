import pandas as pd

tita_df = pd.read_csv('titanic.csv')

bins = [0, 11, 21, 31, 41, 51, 61, 120]

group_names = ['< 11', "11 to 20", "21 to 30", "31 to 40", "41 to 50", "51 to 60", "61 to 80"]
tita_df['age_bin'] =  pd.cut(tita_df['age'], bins, labels=group_names)

tita_df.to_csv('tita_data.csv',  index=False)