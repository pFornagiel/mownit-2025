import numpy as np
from collections.abc import Callable
from visualise import plot_function

def divided_difference_table(nodes: np.ndarray[(np.float64, np.float64)]) -> np.ndarray:
  n = len(nodes)
  nodes_x = nodes[:,0]
  nodes_y = nodes[:,1]
  dp = np.ndarray((n,n), dtype=np.float64)
  dp[:,0] = nodes_y
  for i in range(1,n):
    for j in range(1,i+1):
      dp[i,j] = (dp[i,j-1] - dp[i-1,j-1])/(nodes_x[i] - nodes_x[i-j])
  
  return dp

def newton_interpolation(nodes: np.ndarray[(np.float64, np.float64)], x: np.float64):
  n = len(nodes)
  nodes_x = nodes[:,0]
  dp = divided_difference_table(nodes)
    
  def polynomial_term(k):
    return np.prod([x-nodes_x[i] for i in range(k)])

  return dp[0,0] + np.sum([dp[k,k] * polynomial_term(k) for k in range(1,n)])

def newton_interpolation_horner(nodes: np.ndarray[(np.float64, np.float64)], x: np.float64):
  n = len(nodes)
  nodes_x = nodes[:,0]
  dp = divided_difference_table(nodes)

  result = dp[n-1,n-1]
  for i in range(n-2,-1,-1):
    result = result * (x-nodes_x[i]) + dp[i,i]
  
  return result

def get_newton_interpolation_func(nodes: np.ndarray[(np.float64, np.float64)]) -> Callable[[np.float64], np.float64]:
  n = len(nodes)
  nodes_x = nodes[:,0]
  dp = divided_difference_table(nodes)
  
  def func(x):
    result = dp[n-1,n-1]
    for i in range(n-2,-1,-1):
      result = result * (x-nodes_x[i]) + dp[i,i]
    return result

  return func
  
if(__name__ == '__main__'):
  nodes = np.array([[1, 1], [2, 10], [3, 10], [4, 10], [7,3]], dtype=np.float64)
  x_values = np.linspace(0,10,100)
  func = get_newton_interpolation_func(nodes)
  plot_function(x_values=x_values,func=func,nodes=nodes)