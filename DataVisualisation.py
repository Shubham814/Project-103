import pandas as pd
import plotly.express as px
import time

# array = [[1,2,3,6,5,5,2,55],["a","b","shubham"]]
# df = pd.DataFrame(array)

print(f"\nWelcome to the fUTURe\n\n")
time.sleep(2)
print("Getting the data...")
time.sleep(3)
df = pd.read_csv("Covid_Data.csv")
print("Data read Successfully. Starting the graph formation...")
time.sleep(5)
fig = px.scatter(df,x = "Date",y = "Cases", title="Covid data for Different Countries", color="Country",size_max= 100)

fig.show()
print("Successfully made the Graph.")