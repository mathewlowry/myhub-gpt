import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Your new data
data = {
    'Production_Date': ['Jul-19', 'Sep-21', 'May-21', 'Jul-19', 'Oct, 2019', 'Jul-20', 'May-21', 'Oct, 2019', 'Nov, 2019', 'Jun-20', 'May-18', 'Mar-21', 'Feb-18', 'Jul-21', 'May-21', 'Aug-20'],
    'Kilometres': [11106, 24300, 25000, 30556, 32000, 33500, 33652, 34212, 34250, 34462, 36000, 38000, 17500, 21152, 20041, 40000],
    'Trim_Level': ['comfort', 'united', 'style', 'comfort', 'comfort', 'highline', 'highline', 'comfort', 'life', 'life', 'comfort', 'comfort', 'comfort', 'comfort', 'comfort', 'comfort'],
    'T_O': ['n', 'n', 'n', 'y', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    'Price': [18000, 17500, 17000, 16215, 18500, 18000, 19000, 17000, 17500, 18500, 15500, 17900, 18490, 18890, 18890, 19000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Production_Date to datetime
df['Production_Date'] = pd.to_datetime(df['Production_Date'], format='%b-%y', errors='coerce')

# Calculate car age
current_date = pd.to_datetime('now')
df['Car_Age'] = (current_date - df['Production_Date']).dt.days / 365.25

# Adding the additional car
additional_car = pd.DataFrame({'Car_Age': [6], 'Kilometres': [30556], 'Price': [16215.03]})
df = pd.concat([df, additional_car], ignore_index=True)

# Create the scatter plot
plt.figure(figsize=(10, 7))

scatter = plt.scatter(df['Car_Age'], df['Kilometres'], alpha=0.6, edgecolors='w', linewidth=0.5, label='Existing Cars')
plt.scatter(additional_car['Car_Age'], additional_car['Kilometres'], color='red', edgecolors='w', linewidth=0.5, label='Predicted Car')
plt.title('Car Age vs. Kilometres with Price Labels')
plt.xlabel('Car Age (years)')
plt.ylabel('Kilometres')

# Annotate each point with its price
for i, row in df.iterrows():
    plt.annotate(f"{row['Price']:.0f}", (row['Car_Age'], row['Kilometres']),
                 textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.legend()
plt.tight_layout()
plt.show()
