import numpy as np
import csv


products = []
unit_prices = []
stocks = []
sales_volumes = []


with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row["Product_Name"])
        price_str = row["Unit_Price"].replace('$', '').replace(',', '').strip()
        unit_prices.append(float(price_str))
        stocks.append(float(row["Stock_Quantity"]))
        sales_volumes.append(float(row["Sales_Volume"]))

products = np.array(products)
unit_prices = np.array(unit_prices)
stocks = np.array(stocks)
sales_volumes = np.array(sales_volumes)

total_inventory_value = stocks * unit_prices


hot_idx = np.argmax(sales_volumes)
best_selling_product = products[hot_idx]
max_sales = sales_volumes[hot_idx]


discount_revenue = sales_volumes * unit_prices * 0.9


with open("Processed_Results_Numpy.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)

    w.writerow(["Product_Name", "Total_Inventory_Value", "Best_Selling_Mark", "Discounted_Revenue"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            round(total_inventory_value[i], 2),
            i == hot_idx,
            round(discount_revenue[i], 2)
        ])

print(f"最暢銷商品: {best_selling_product} (銷量: {max_sales})")
print(f"前五個商品的庫存價值: {total_inventory_value[:5]}")
print(f"前五個商品的 9 折後收入: {discount_revenue[:5]}")