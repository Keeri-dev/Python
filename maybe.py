import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

# Sample data

data = {
    'Report': [1583, 7562, 10370, 5641, 5246, 51103, 67335, 98622, 47181, 46100, 45339, 34653, 43742, 20203, 6710, 4214, 1906, 1102],
    'Time': ["2024-11-11 7:55", "2024-11-11 8:25", "2024-11-11 8:55", "2024-11-11 9:10", "2024-11-11 9:40", "2024-11-11 10:10",
             "2024-11-11 10:25", "2024-11-11 10:40", "2024-11-11 10:55", "2024-11-11 11:10", "2024-11-11 11:25", "2024-11-11 11:40", "2024-11-11 11:55",
             "2024-11-11 12:10", "2024-11-11 12:25", "2024-11-11 12:40", "2024-11-11 12:55", "2024-11-11 1:10"]
}

df = pd.DataFrame(data)
df['Time'] = pd.to_datetime(df['Time'])

    # Count the number of reports per day
report_counts = df.groupby(df['Time'].dt.date)['Report'].count()

    # Create a bar chart
plt.bar(report_counts.index, report_counts.values)
plt.xlabel('Date')
plt.ylabel('Number of Reports')
plt.title('Number of Reports per Day')
plt.xticks(rotation=45)
plt.show()
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)

