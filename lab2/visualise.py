import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Callable

def plot_function(x_values: np.ndarray[np.float64], func: Callable[[np.float64], np.float64], nodes: np.ndarray[(np.float64, np.float64)] | None):
  y_values = np.array([func(x) for x in x_values])

  plt.plot(x_values, y_values, label='Lagrange Interpolation')
  if(nodes is not None):
    plt.scatter(nodes[:, 0], nodes[:, 1], color='red', label='Data Points')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.legend()
  plt.title('Function visualisation')
  plt.show()