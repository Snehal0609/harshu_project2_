# ✅ Install these first (only once)
# pip install kagglehub pandas openpyxl

import kagglehub
import pandas as pd
import os

# 1️⃣ Download dataset
dataset_path = kagglehub.dataset_download("agungpambudi/property-sales-data-real-estate-trends")

# 2️⃣ List available files
print("Files found in dataset:")
for f in os.listdir(dataset_path):
    print("📁", f)

# 3️⃣ Pick one file (you can change to another year if you want)
file_path = os.path.join(dataset_path, "2022-property-sales-data.csv")

# 4️⃣ Load the CSV
df = pd.read_csv(file_path)
print("\n✅ Data Loaded! Columns available:\n", df.columns.tolist())

# 5️⃣ Select only 3 columns (exact names)
selected_columns = ['Address', 'Sale_price', 'District']
df_small = df[selected_columns].copy()

# Rename for Power BI clarity
df_small.columns = ['Property_Name', 'Price', 'Location']

# 6️⃣ Save to Excel
output_path = os.path.join(os.getcwd(), "property_data.xlsx")
df_small.to_excel(output_path, index=False)

print(f"\n✅ Excel file saved successfully → {output_path}")
print("Columns saved: Property_Name, Price, Location")
