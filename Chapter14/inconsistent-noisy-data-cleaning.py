# inconsistent-noisy-data-cleaning.py

import pandas as pd
import matplotlib.pyplot as plt

dataset = {
    'product': ['productA', 'ProductA', 'productB', 'ProDuctB', 'productC', 'productA', 'productA', 'productC'],
    'date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-03', '2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07'],
    'price': [10, 11, 6, 5.9, 9, 10, 1000, 9.5]
}

df = pd.DataFrame(dataset)

df['product'] = df['product'].str.lower()

mean_price = df['price'].mean()
std_price = df['price'].std()

df = df[(df['price'] < mean_price + std_price) & (df['price'] > mean_price - std_price)]

print(df)
plt.boxplot(df['price'])
plt.title('Box plot of prices')
plt.show()
