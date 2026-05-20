import pandas as pd

data_from_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df = pd.DataFrame(data_from_dict)

data_from_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_list = pd.DataFrame(data_from_list, columns=['Product', 'Price', 'Sales'])

print(df.head(5).to_string())
print(df.tail(5).to_string())

print(df.shape)

print(f"Index({list(df.columns)}, dtype='object')")

print(df.dtypes)

print(df.count())

summary = df.describe().round(2)
summary.to_csv('0520_stock2.csv')

pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(summary)