# Burak Ayaeriş 2693653

import pandas as pd
import numpy as np

winconsin_df = pd.read_excel('Wisconsin Diagnostic Breast Cancer.xlsx')

# min-max normalization
winconsin_df_normal = (winconsin_df - winconsin_df.min()) / (winconsin_df.max() - winconsin_df.min())

