import pandas as pd


stock1 = pd.Series([120, 80, None, 60, 95, None, 110])


index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series([120, 80, None, 60, 95, None, 110], index=index_labels)


stock3 = stock2.to_dict()


stock2.to_csv('0520_stock.csv', header=False)


print("stock1")
print(stock1)
print("\nstock2")
print(stock2)
print("\nstock3")
print(stock3)
print(f"\nBanana 庫存： {stock2['Banana']}")
print("\n缺失值檢查：")
print(stock2.isna())
print(f"\n缺失值數量： {stock2.isna().sum()}")