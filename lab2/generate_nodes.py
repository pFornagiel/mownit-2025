import numpy as np

def random_numbers(n,y_max):
  return [np.random.random() * y_max for _ in range(n)]

def generate_chebyshev_roots(n: int, a: np.float64, b: np.float64):
  return np.array([(a+b)/2 + (b-a)/2 * np.cos((2*k+1)/(2*n) * np.pi) for k  in range(n)], dtype=np.float64)

def generate_random_chebyshev_nodes(n: int, a: np.float64, b: np.float64, max_y: np.float64=10):
  return np.array(list(zip(generate_chebyshev_roots(n,a,b), random_numbers(n,max_y) )))
  
def generate_random_unform_nodes(n: int, a: np.float64, b: np.float64, max_y: np.float64=10):
  return np.array(list(zip( np.random.uniform(a,b, size=n), random_numbers(n,max_y) )))