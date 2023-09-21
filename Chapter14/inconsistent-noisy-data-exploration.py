# inconsistent-noisy-data-exploration.py

import pandas as pd

dataset = {
    'product': ['productA', 'ProductA', 'productB', 'ProDuctB', 'productC', 'productA', 'productA', 'productC'],
    'date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-03', '2023-08-04', '2023-08-05', '2023-08-06', '2023-08-07'],
    'price': [10, 11, 6, 5.9, 9, 10, 1000, 9.5]
}

df = pd.DataFrame(dataset)
print(df)
