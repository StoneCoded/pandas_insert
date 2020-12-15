class insert():
    def init(self, df_origin, df_add, split_start = 0, split_end = 0):

        self.df_origin = df_origin
        self.df_add = df_add
        self.split_start = split_start
        self.split_end = split_end

    def split(self, input_index, split_end):

        if split_end == 0:
            df_origin = pd.concat([df_add, df_origin])
        elif split_end <0:
            raise ValueError('split_end must be integer of 0 or greater')
        else:
            df_split_1 = df_origin.iloc(0:(split_start), :).copy()
            df_split_2 = df_origin.iloc((split_end):, :).copy()
            df_origin = pd.concat([df_split_1, df_add, \
            df_origin]).reset_index(drop=True)
