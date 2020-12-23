import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}
d2 = {'col1': [5, 6], 'col2': [7, 8]}

df_origin = pd.DataFrame(data=d)
df_add = pd.DataFrame(data=d2)

split_start = 1


df_split_1 = df_origin.iloc[0: split_start, :].copy()
df_split_2 = df_origin.iloc[split_start:, :].copy()
df_origin = pd.concat([df_split_1, df_add, df_split_2]).reset_index(drop=True)

df_origin
