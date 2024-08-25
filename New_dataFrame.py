import pandas as pd

details = {"Name": ["Johnny", "Daniel", "Mike"], "Age": [51, 49, 52], "City": ["Los Angeles", "San Francisco", "Las Vegas"]}
data = pd.DataFrame(details)
print(data.head())
print(data.info())