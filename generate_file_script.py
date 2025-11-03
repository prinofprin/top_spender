import pandas as pd
import random
from datetime import datetime, timedelta


input_file_path = r"C:\Users\original_file.csv"
output_file_path = r"C:\Users\generated_file.csv"


df = pd.read_csv(input_file_path)

all_branch = df['branch'].dropna().unique().tolist()


all_products_dic = {}
for index, row in df.iterrows():
    total_price = row['amount']
    brand = row['brand']
    sku = row['sku']
    quantity = row['quantity']
    unit_price = round(total_price / quantity)

    if sku not in all_products_dic:
        all_products_dic[sku] = {
            'brand': brand,
            'unit_price': unit_price
        }
all_sku_list = list(all_products_dic.keys())


def random_timestamp():
    start = datetime(2024, 1, 1, 0, 0, 0)
    end = datetime(2024, 12, 31, 23, 59, 59)
    total_seconds = int((end - start).total_seconds())
    random_seconds = random.randint(0, total_seconds)
    random_date = start + timedelta(seconds=random_seconds)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")


total_rows = (10_000_000 - len(df)) - 1
rows = []

for i in range(total_rows):
    sku = random.choice(all_sku_list)
    product = all_products_dic[sku]
    quantity = random.randint(1, 10)
    rows.append({
        'order_no': f"ORD{random.randint(100000, 999999)}",
        'customer_no': f"CUST{random.randint(1000, 9999)}",
        'branch': random.choice(all_branch),
        'brand': product['brand'],
        'sku': sku,
        'quantity': quantity,
        'amount': product['unit_price'] * quantity,
        'transaction_datetime': random_timestamp(),
    })


df_new = pd.DataFrame(rows)
df_combined = pd.concat([df, df_new], ignore_index=True)
df_combined.to_csv(output_file_path, index=False)

print("done")
