import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts['category'] = 0
    LC = 0
    AC = 0
    HC = 0
    for i in range(len(accounts)):
      salary = accounts['income'][i]

      if salary < 20000:
        accounts['category'][i] = "Low Salary"
        LC +=1
      elif (salary <= 50000 and salary >= 20000):
        accounts['category'][i] = "Average Salary"
        AC += 1
      else: 
        accounts['category'][i] = "High Salary"
        HC +=1
    
    DF = pd.DataFrame([
      ["Low Salary", LC], 
      ["Average Salary", AC], 
      ["High Salary", HC]
    ], columns= (["category", "accounts_count"]))
    return DF