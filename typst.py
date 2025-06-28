import pandas as pd
import numpy as np

def csv_to_typst(csv_file: str, df: pd.DataFrame):
    # Read CSV file
    
    col_amount = len(df.keys())
    
    # Define column widths
    
    # Define table header
    header = "    [*" + "*], [*".join(df.columns) + "*],\n"
    
    # Define table rows
    rows = "".join(["    [" + "], [".join(map(str, row)) + "],\n" for row in df.values])
    
    # Combine everything into the Typst table format
    typst_table = f"""#table(
    columns: {col_amount},
    inset: 4pt,
    align: center,
    table.header(
    {header}),
    {rows}  )"""
    
    return typst_table

# Example usage
csv_file = "chebyshev.csv"  # Change this to the path of your CSV file
df = pd.read_csv(csv_file, delimiter=',' )
typst_output = csv_to_typst(csv_file, df)
print(df)
with open('typst_table.txt', 'r+') as file:
  file.write(typst_output)  
# print(typst_output)
