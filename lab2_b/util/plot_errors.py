import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_errors(data_path, y_column, y_label, title, output_file, y_log_scale=False, y_min=None, y_max=None, y_ticks=None):
  """
  Plots errors based on the given column and saves the plot.

  Parameters:
    data_path (str): Path to the CSV file.
    y_column (str): Column name for the Y-axis values.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    output_file (str): File name to save the plot.
    y_log_scale (bool): Whether to use a logarithmic scale for the Y-axis.
    y_min (float): Minimum value for the Y-axis.
    y_max (float): Maximum value for the Y-axis.
    y_ticks (list): Custom tick marks for the Y-axis.
  """
  # Load the CSV file
  df = pd.read_csv(data_path)

  # Group data by node type
  node_types = df["Node Type"].unique()

  # Plot the data
  plt.figure()
  for node_type in node_types:
    subset = df[(df["Node Type"] == node_type) & 
          (df["Number of Nodes"] <= 80)]
    plt.plot(subset["Number of Nodes"], subset[y_column], label=f"Węzły {"Równoodległe" if node_type == "Linear" else "Wielomianu Czebyszewa"}")
  
  plt.xlabel("Liczba węzłów")
  plt.ylabel(y_label)
  plt.title(title)
  if y_log_scale:
    plt.yscale("log")
  else:
    plt.ylim(y_min, y_max)  # Set Y-axis limits
    plt.xlim(2,10)
  if y_ticks is not None:
    plt.yticks(y_ticks)  # Set uniform Y-axis ticks
  plt.legend()
  plt.grid()
  plt.savefig(output_file)
  plt.show()

# Example usage
data_path = r"c:\Users\Paweł\Desktop\MOWNiT\main\lab3\data\interpolation_errors.csv"

# Define common Y-axis limits and ticks
y_min = 0
y_max = 20
y_ticks = np.linspace(y_min, y_max, 6)  # 6 evenly spaced ticks

# Plot maximum error
plot_errors(
  data_path=data_path,
  y_column="Max Error",
  y_label="Maksymalny błąd",
  title="Maksymalny błąd interpolacji metodą Hermite'a",
  output_file="max_error_hermite.png",
  y_min=y_min,
  y_max=y_max,
  y_ticks=y_ticks
)

# Plot squared error
plot_errors(
  data_path=data_path,
  y_column="Squared Error",
  y_label="Błąd średniokwadratowy",
  title="Błąd średniokwadratowy interpolacji metodą Hermite'a",
  output_file="squared_error_hermite.png",
  y_min=y_min,
  y_max=y_max,
  y_ticks=y_ticks
)

# Plot maximum error with logarithmic scale
log_y_ticks = np.logspace(0, 24, 6)
print(log_y_ticks)
plot_errors(
  data_path=data_path,
  y_column="Max Error",
  y_label="Maksymalny błąd (skala logarytmiczna)",
  title="Maksymalny błąd interpolacji metodą Hermite'a (skala logarytmiczna)",
  output_file="max_error_hermite_log.png",
  y_log_scale=True,
  y_min=y_min,
  y_max=y_max,
  y_ticks=log_y_ticks
)

# Plot squared error with logarithmic scale
plot_errors(
  data_path=data_path,
  y_column="Squared Error",
  y_label="Błąd średniokwadratowy (skala logarytmiczna)",
  title="Błąd średniokwadratowy interpolacji metodą Hermite'a (skala logarytmiczna)",
  output_file="squared_error_hermite_log.png",
  y_log_scale=True,
  y_min=y_min,
  y_max=y_max,
  y_ticks=log_y_ticks
)
