import pandas as pd

def insert(self, df_origin, df_add, split_start = 0, split_end = 0):

    if split_end == 0:
        df_origin = pd.concat([df_add, df_origin])
    elif split_end <0:
        raise ValueError('split_end must be integer of 0 or greater')
    else:
        df_split_1 = df_origin.iloc(0:(split_start), :).copy()
        df_split_2 = df_origin.iloc((split_end):, :).copy()
        df_origin = pd.concat([df_split_1, df_add, \
        df_origin]).reset_index(drop=True)
