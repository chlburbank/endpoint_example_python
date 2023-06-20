# Import the dependencies
import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/users/')
response = response.json()

# Create the DataFrame
df = pd.DataFrame(columns=["id","name","username","email"])

# Inserting the data into the df variable 
for i in range(0, len(response)):
    currentItem = response[i]
    df.loc[i] = [response[i]["id"], response[i]["name"], response[i]["username"], response[i]["email"]]

# Placing the Data inside df into an Excel
with pd.ExcelWriter('lorem.xlsx') as writer:
    df.to_excel(writer, sheet_name='page')