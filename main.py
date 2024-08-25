import pandas as pd
data = pd.read_csv("Lesson_2/titanic.csv")
print(data.head()) #This displays the first five passengers with given information about them.
print(data.shape)  #This displays the column and row(Number of passengers/rows, Number of info about passengers/columns)
print(data.info()) #This provides a concise summary of the DataFrame. It also includes Non-Null values and datatype.
print(data[["Name", "Age", "Survived"]])
col = data[["Name", "Age", "Survived"]]

#Filtering out the rows
above35 = data[(data["Age"] >= 30) & (data["Age"] <= 50)]  # & = and
print(above35.head())

pclass_23 = data[(data["Pclass"]==2) | (data["Pclass"]==3)]  # | = or
print(pclass_23)

print("Mean fare of the passengers who traveled in 2nd and 3rd class: ", pclass_23["Fare"].mean())

female_pass = data[(data["Pclass"]==1) & (data["Age"]>30) & (data["Sex"]=="female")]

print("Female passengers that traveled in first class and are above 30: ")
print(female_pass[["Name", "Age", "Pclass"]])