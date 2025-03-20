import pandas as pd

url = "https://raw.githubusercontent.com/ritaafrica/data/main/network_traffic_data.csv"

df = pd.read_csv(url)

print(df.head()) # shows first five 

#print(df.shape()) # shows the number of rows and columns

print(df.info())   #shows info of the dataset

print(df.tail())   #shows last five

print(df.describe())   #shows descriptive stats

selected_columns = df[["Timestamp" ,"Source_IP" , "Protocol" , "Threat_Level"]]

print(selected_columns.columns)

blocked_traffic = df[df["Status"] == "Blocked"]

blocked_summary = blocked_traffic[["Timestamp", "Source_IP", "Destination_IP", "Status", "Threat_Level" ]]

print(blocked_traffic.info())

print(blocked_summary.shape)
print(blocked_summary.head())