import pandas as pd

# Read the CSV
df = pd.read_csv('spectral_radius_results.csv')

# Round the spectral_radius column to 5 decimal places
df['spectral_radius'] = df['spectral_radius']

# Save to new file
df.to_csv('output_rounded.csv', index=False, float_format='%.5f')