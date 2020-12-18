import pandas as pd
class chunk_insert():
    def __init__(self, df):
        self.df = df

    def chunk(self, c_start, c_end):
        """
        Creates a 'chunk' of rows from a dataframe

        ARGS: df - Dataframe for rows to be inserted into
        new_rows - Dataframe with same columns as original DataFrame
        split_index - index where data will be inputted, default 0

        returns: orignal DataFrame with inserted rows, index is reset.

        """

        if c_start >= c_end:
            raise ValueError('c_end must be greater than c_start')
        else:
            self.df_chunk = self.df.iloc[(c_start):(c_end), :].copy()
        return self.df_chunk
    def row_insert(self, new_rows, split_index=0):
        """
            Inserts rows with indentical columns into a DataFrame

            ARGS: df - Dataframe for rows to be inserted into
                  new_rows - Dataframe with same columns as original DataFrame
                  split_index - index where data will be inputted, default 0

            returns: orignal DataFrame with inserted rows, index is reset.
        """

        if split_index == 0:
            self.df = pd.concat([new_rows, self.df]).reset_index(drop=True)
        elif split_index <0:
            raise ValueError('split_end must be integer of 0 or greater')
        else:
            df_split_1 = self.df.iloc[:(split_index), :].copy()
            df_split_2 = self.df.iloc[(split_index):, :].copy()
            self.df = pd.concat([df_split_1, new_rows, \
            df_split_2]).reset_index(drop=True)
        return self.df

    def multiply_row_chunks(self, c_start, c_end, split_index):
        self.df = (self.row_insert(new_chunk.chunk(c_start,c_end),\
                 split_index))
        return self.df




lst = [[1,2,3],[2,3,4],[3,3,3],[5,6,7]]
lst2 = [[9,9,9]]
df = pd.DataFrame(lst, columns = ['a','b','c'])
df_new = pd.DataFrame(lst2, columns = ['a','b','c'])

new_chunk = chunk_insert(df)
