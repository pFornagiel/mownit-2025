import os
import pandas as pd

# Directory containing the CSV files
data_dir = 'data'

# Metrics to compare
metrics = ['error', 'time', 'mem']
output_files = {metric: f'comparison_{metric}.csv' for metric in metrics}

# Prepare a dictionary to hold DataFrames for each metric
metric_data = {metric: pd.DataFrame() for metric in metrics}

# Iterate through each CSV file in the directory
for filename in sorted(os.listdir(data_dir)):
  if filename.endswith('.csv'):
    filepath = os.path.join(data_dir, filename)
    df = pd.read_csv(filepath)
    tag = filename.replace('.csv', '') 
    
    for metric in metrics:
      col_name = f'{metric}_{tag}'
      if metric_data[metric].empty:
        metric_data[metric]['n'] = df['n']
      metric_data[metric][col_name] = df[metric]

# Save each metric DataFrame to a separate CSV file
for metric, df in metric_data.items():
  df.to_csv(output_files[metric], index=False, float_format='%.4e')
