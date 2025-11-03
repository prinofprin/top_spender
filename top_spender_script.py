import pandas as pd
import random
from datetime import datetime, timedelta


input_file_path = r"C:\Users\generated_file.csv"
output_file_path = r"C:\Users\prino\result.csv"

df = pd.read_csv(input_file_path)

df["transaction_datetime"] = pd.to_datetime(df["transaction_datetime"])
df["month"] = df["transaction_datetime"].dt.month

monthly_spend = (
    df.groupby(["month", "customer_no"])["amount"]
    .sum()
    .reset_index()
)


top_spenders = (
    monthly_spend
    .sort_values(["month", "amount"], ascending=[True, False])
    .groupby("month")
    .head(10)
)



top_spenders.to_csv(output_file_path, index=False)

print("done")













