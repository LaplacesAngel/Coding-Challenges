import pandas as pd

titanic = pd.read_csv("PANDAS/resources/titanic.csv")

print(titanic.head(8))

def printTail(thing: pd.DataFrame) -> pd.DataFrame:
    print(f"the last ten rows are: \n", thing.tail(10))

printTail(titanic)

print(f"\n\n\n\n", titanic.dtypes, "\n\n\n\n", titanic.describe())

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

printTail(titanic)