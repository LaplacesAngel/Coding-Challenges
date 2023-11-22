import pandas as pd

loansData = pd.read_csv(r"C:\Users\paule\Documents\Coding\Brittany_Student_Loans\MyStudentData.txt", sep=":")

print(loansData.head(500))