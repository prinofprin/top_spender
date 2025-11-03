import pandas as pd


input_file_path = r"C:\Users\prino\Desktop\code\cyptro_2\Primo\generated_file.csv"
output_file_path = r"C:\Users\prino\Desktop\code\cyptro_2\Primo\result.csv"

df = pd.read_csv(input_file_path)

df["transaction_datetime"] = pd.to_datetime(df["transaction_datetime"])
df["month"] = df["transaction_datetime"].dt.month

monthly_spend = df.groupby(["month", "customer_no"])["amount"].sum()
monthly_spend = monthly_spend.reset_index()


monthly_spend = monthly_spend.sort_values(["month", "amount"], ascending=[True, False])
top_spenders = monthly_spend.groupby("month").head(10)

top_spenders.to_csv(output_file_path, index=False)

print("done")
