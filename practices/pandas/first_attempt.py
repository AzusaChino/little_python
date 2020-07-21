import pandas as pd
import numpy as np

if __name__ == '__main__':
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)
    dates = pd.date_range("20200202", periods=6)
    print(dates)
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)
