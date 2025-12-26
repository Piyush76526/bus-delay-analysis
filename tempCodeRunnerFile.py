import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
print("Bus Delay Data:")
print(data)

data["Time_Min"] = data["Time"].str.split(":").apply(
    lambda x: int(x[0]) * 60 + int(x[1])
)

plt.figure()
plt.bar(data["Time"], data["Delay"])
plt.xlabel("Time of Day")
plt.ylabel("Delay (Minutes)")
plt.title("City Bus Delay Trend (Bar Chart)")
plt.show()

correlation = data["Time_Min"].corr(data["Delay"])
print("\nCorrelation between Time and Delay:")
print(correlation)

plt.figure()
plt.scatter(data["Time_Min"], data["Delay"])
plt.xlabel("Time (in minutes)")
plt.ylabel("Delay (Minutes)")
plt.title("Correlation between Time and Delay")
plt.show()
