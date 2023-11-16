import pandas as pd

d = {'col 1': [1,2], 'col 2':[3,4]}
df = pd.DataFrame(d)

print(df)

print(df.dtypes)

print(df.head(1))

def selectFirstRow(d: pd.DataFrame) -> pd.DataFrame:
    return d.head(1)

print(selectFirstRow(df))