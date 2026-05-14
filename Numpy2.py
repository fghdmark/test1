import numpy as np
import csv

# 初始化列表來儲存資料
products = []
unit_prices = []
stocks = []
sales_volumes = []

# (1) 讀取資料檔案
with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row["Product_Name"])
        # 清理 Unit_Price 的錢字號並轉為浮點數
        price_str = row["Unit_Price"].replace('$', '').replace(',', '').strip()
        unit_prices.append(float(price_str))
        stocks.append(float(row["Stock_Quantity"]))
        sales_volumes.append(float(row["Sales_Volume"]))

# 轉換為 numpy 陣列以便計算
products = np.array(products)
unit_prices = np.array(unit_prices)
stocks = np.array(stocks)
sales_volumes = np.array(sales_volumes)

# (1) 計算每個商品的總庫存價值 (Stock * Price)
total_inventory_value = stocks * unit_prices

# (2) 找出最暢銷 (依據 Sales_Volume)
# 找出銷量最高的索引
hot_idx = np.argmax(sales_volumes)
best_selling_product = products[hot_idx]
max_sales = sales_volumes[hot_idx]

# (3) 計算 9 折後的收入 (Sales_Volume * Price * 0.9)
discount_revenue = sales_volumes * unit_prices * 0.9

# 將結果寫入新的 CSV 檔案 (參考您的格式)
with open("Processed_Results_Numpy.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    # 定義標題
    w.writerow(["Product_Name", "Total_Inventory_Value", "Best_Selling_Mark", "Discounted_Revenue"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            round(total_inventory_value[i], 2),
            i == hot_idx,  # 標註是否為最暢銷商品
            round(discount_revenue[i], 2)
        ])

# 輸出摘要供確認
print(f"最暢銷商品: {best_selling_product} (銷量: {max_sales})")
print(f"前五個商品的庫存價值: {total_inventory_value[:5]}")
print(f"前五個商品的 9 折後收入: {discount_revenue[:5]}")