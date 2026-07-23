import os
import tabula
import pandas as pd

# ==== CONFIG =====
input_folder = r"/PATH"
output_folder = r"/PATH"

os.makedirs(output_folder, exist_ok=True)

# RETRIEVE PDF FILES
pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

for pdf_file in pdf_files:
    input_path = os.path.join(input_folder, pdf_file)
    output_path = os.path.join(output_folder, os.path.splitext(pdf_file)[0] + ".xlsx")

    print(f"Converting: {pdf_file} → {os.path.basename(output_path)}")

    try:
        #READ TABLES
        dfs = tabula.read_pdf(input_path, pages='all', multiple_tables=True)

        if not dfs:
            print(f"No Tables Found In {pdf_file}")
            continue

        #WRITE EACH TABLE
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            for i, df in enumerate(dfs):
                sheet_name = f"Table_{i+1}"
                df.to_excel(writer, index=False, sheet_name=sheet_name)

        print(f"Saved To {output_path}")

    except Exception as e:
        print(f"Error Converting {pdf_file}: {e}")

print("\nAll Done!")
