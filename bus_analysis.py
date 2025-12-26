import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

sns.set_theme(style="whitegrid")
np.random.seed(42)

n_trips = 500
data = {
    'trip_id': [f'BUS_{i:03d}' for i in range(n_trips)],
    'route': np.random.choice(['Route-A', 'Route-B', 'Route-C'], n_trips),
    'scheduled_time': [datetime(2025, 12, 1, 7, 0) + timedelta(minutes=np.random.randint(0, 720)) for _ in range(n_trips)],
    'distance_km': np.random.uniform(5, 40, n_trips),
    'traffic_level': np.random.randint(1, 11, n_trips)
}
df = pd.DataFrame(data)

df['delay_min'] = (df['traffic_level'] * 2.5) + (df['distance_km'] * 0.4) + np.random.normal(5, 3, n_trips)
df['delay_min'] = df['delay_min'].clip(lower=0).round(2)
df['hour'] = df['scheduled_time'].dt.hour

plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
sns.histplot(df['delay_min'], bins=20, kde=True, color='teal')
plt.title('Analysis of Delay Frequency', fontsize=14)
plt.xlabel('Delay (Minutes)')

plt.subplot(2, 2, 2)
hourly_avg = df.groupby('hour')['delay_min'].mean()
plt.plot(hourly_avg.index, hourly_avg.values, marker='o', color='red', linestyle='-', linewidth=2)
plt.title('Average Bus Delay Trend by Hour', fontsize=14)
plt.xlabel('Hour of Day (24hr)')
plt.ylabel('Avg Delay (Min)')

plt.subplot(2, 2, 3)
corr = df[['distance_km', 'traffic_level', 'delay_min']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation: Factors Affecting Delay', fontsize=14)

plt.subplot(2, 2, 4)
sns.boxplot(x='route', y='delay_min', data=df, palette='Set2')
plt.title('Delay Distribution by Route', fontsize=14)

plt.tight_layout()
plt.show()
