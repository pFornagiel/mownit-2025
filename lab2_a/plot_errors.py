import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data_path = r"c:\Users\Paweł\Desktop\MOWNiT\main\lab2\data\interpolation_errors.csv"
df = pd.read_csv(data_path)

# Group data by interpolation type and node type
interpolation_types = df["Interpolation Type"].unique()
node_types = df["Node Type"].unique()

# Plot maximum error
for interp_type in interpolation_types:
  plt.figure()
  for node_type in node_types:
    subset = df[(df["Interpolation Type"] == interp_type) & 
          (df["Node Type"] == node_type) & 
          (df["Number of Nodes"] <= 80)]
    plt.plot(subset["Number of Nodes"], subset["Max Error"], label=f"Węzły {node_type}")
  plt.xlabel("Liczba węzłów")
  plt.ylabel("Maksymalny błąd")
  plt.title(f"Maksymalny błąd interpolacji metodą {interp_type.capitalize()}")
  plt.legend()
  plt.grid()
  plt.savefig(f"max_error_{interp_type}.png")
  plt.show()

# Plot squared error
for interp_type in interpolation_types:
  plt.figure()
  for node_type in node_types:
    subset = df[(df["Interpolation Type"] == interp_type) & 
          (df["Node Type"] == node_type) & 
          (df["Number of Nodes"] <= 80)]
    plt.plot(subset["Number of Nodes"], subset["Squared Error"], label=f"Węzły {node_type}")
  plt.xlabel("Liczba węzłów")
  plt.ylabel("Błąd średniokwadratowy")
  plt.title(f"Błąd średniokwadratowy interpolacji metodą {interp_type.capitalize()}")
  plt.legend()
  plt.grid()
  plt.savefig(f"squared_error_{interp_type}.png")
  plt.show()
