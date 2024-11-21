import pandas as pd

# Step 1: Read the data from the Excel file
n = 2000  # Number of rows to read
df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', header=0, nrows=n)

# Step 2: Prepare the data
reasons = df["Reason"].unique()
reasons_dict = {reason: i for i, reason in enumerate(reasons)}

df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"
df["Reason"] = " " + df["Reason"].apply(lambda x: str(reasons_dict[x]))
df.drop(["Description"], axis=1, inplace=True)
df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"}, inplace=True)

# Step 3: Save as JSONL
jsonl_data = df.to_json(orient="records", indent=0, lines=True)
with open("drug_malady_data.jsonl", "w") as f:
    f.write(jsonl_data)

print("Data preparation complete. Saved to drug_malady_data.jsonl.")
