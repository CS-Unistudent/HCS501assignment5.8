import pandas as pd

#pd reads the csv file and holds the DataFrame in the variable df
df = pd.read_csv('stockmarkpricetracker.csv')

#returns the number of records and stores it in record_no
record_no = len(df)

#prints the number of records
print("Number of records: ", record_no)