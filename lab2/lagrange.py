import numpy as np
from collections.abc import Callable
from visualise import plot_function
from generate_nodes import generate_random_chebyshev_nodes, generate_chebyshev_roots
  
def lagrange_interpolation(nodes: np.ndarray[(np.float64, np.float64)], x: np.float64):
  n = len(nodes)
  x_nodes = nodes[:, 0]
  y_nodes = nodes[:, 1]

  def polynomial(k):
    terms = np.array([(x-x_nodes[i])/(x_nodes[k] - x_nodes[i]) for i in range(n) if i != k])
    return np.prod(terms)
  
  return np.sum(y_nodes * np.array([polynomial(k) for k in range(n)]))

def get_lagrange_interpolation_func(nodes: np.ndarray[(np.float64, np.float64)]) -> Callable[[np.float64], np.float64]:
  n = len(nodes)
  x_nodes = nodes[:, 0]
  y_nodes = nodes[:, 1]
  def coefficient(k):
    return np.prod([1/(x_nodes[k] - x_nodes[i]) for i in range(n) if i != k])
  coefficients = np.array([coefficient(k) for k in range(n)])
  
  def polymial_term(x,k):
    return np.prod([(x - x_nodes[i]) for i in range(n) if i!=k])
  
  return lambda x: np.sum(y_nodes * coefficients * np.array([polymial_term(x,k) for k in range(n)]))

# Example usage
if(__name__ == '__main__'):
  nodes = np.array([[1, 1], [2, 10], [3, 10], [4, 10], [7,3]], dtype=np.float64)
  x_values = np.linspace(0,10,100)
  func = get_lagrange_interpolation_func(nodes)
  plot_function(x_values=x_values,func=func,nodes=nodes)