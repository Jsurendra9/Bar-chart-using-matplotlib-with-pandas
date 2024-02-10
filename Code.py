#Importing moduals
import matplotlib.pyplot as plt
import pandas as pd

#Reading Exccel file
df = pd.read_excel("Employee Sample Data.xlsx", sheet_name="Raw Data")

#Grouping data
group = df.groupby(["Department", "Ethnicity", "Gender"]).agg({"Full Name": "count"}).reset_index()

#Pivot table using grouped data.
pivot = group.pivot_table(index="Department", columns=["Gender", "Ethnicity"], values="Full Name")
print(pivot)

#Creating Bar chart using Pivot Table.
pivot.plot(kind="bar", stacked=True)
plt.xlabel("Department")
plt.ylabel("Count of Employees")
plt.title("Department Vs CCount of Employees by Ethnicity and Gender")
plt.show()