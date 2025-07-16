# Burak Ayaeriş 2693653

import numpy as np
import pandas as pd
def randomize_dataset_ID2693653(df):
    np.random.seed(42)
    data_np = df.values
    df_size = len(df)
    df_indices = np.arange(df_size)
    i = df_size-1
    while i > 0:
        j = np.random.randint(0, i+1)
        copy_indices = df_indices[i]
        df_indices[i] = df_indices[j]
        df_indices[j] = copy_indices
        i -= 1
    randomized_data = data_np[df_indices]
    randomized_dataset = pd.DataFrame(randomized_data, columns=df.columns)
    return randomized_dataset


    

