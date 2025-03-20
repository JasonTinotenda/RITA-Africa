import pandas as pd

url = "https://raw.githubusercontent.com/ritaafrica/data/main/network_traffic_data.csv"

df = pd.read_csv(url)

blocked_traffic = df[df["Status"] == "Blocked"] #Selects all IPs with blocked status

blocked_summary = blocked_traffic[["Timestamp", "Source_IP", "Destination_IP", "Status", "Threat_Level" ]] #

print(blocked_traffic.info())

print(blocked_summary.shape)
print(blocked_summary.head())