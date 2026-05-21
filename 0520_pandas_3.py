import pandas as pd

df = pd.read_csv("SuperMarket Analysis.csv")

print("==== 1. 資料筆數與基本資訊 ====")
print(f"資料筆數: {df.shape[0]} 筆")
print(f"欄位數量: {df.shape[1]} 個")
print("\n前幾筆資料內容:")
print(df.head())
print("-" * 50)

branch_condition = df['Branch'].isin(['A', 'Alex'])
member_condition = df['Customer type'] == 'Member'
df_filtered = df[branch_condition & member_condition]

print("==== 2. 篩選條件結果 (Branch為A且客戶為Member) ====")
print(f"篩選後的交易筆數: {len(df_filtered)} 筆")
print("-" * 50)

prod_summary_whole = df.groupby('Product line').agg(
    Sales=('Sales', 'sum'),
    Rating=('Rating', 'mean')
).round(2).reset_index()

city_gender_whole = df.groupby(['City', 'Gender']).agg(
    Avg_Sales=('Sales', 'mean'),
    Transaction_Count=('Sales', 'count')
).round(2)

max_sales_row_whole = prod_summary_whole.loc[prod_summary_whole['Sales'].idxmax()]

print("==== 3. 產品線彙總結果 (完整資料版本) ====")
print(prod_summary_whole.to_string(index=False))
print(f"\n👉 總銷售額最高的產品線為: {max_sales_row_whole['Product line']} (總銷售額: {max_sales_row_whole['Sales']})")
print("-" * 50)

print("==== 4. 依 City 與 Gender 分組結果 (完整資料版本) ====")
print(city_gender_whole)
print("-" * 50)

prod_summary_whole.to_csv('0520_pandas_3OK.CSV', index=False)
print("系統提示：已成功產生匯出檔案 '0520_pandas_3OK.CSV'")