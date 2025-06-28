import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv(
  'c:\\Users\\Paweł\\Desktop\\MOWNiT\\lab1\\data\\data.csv', 
  delimiter=';',
  dtype={'float': np.float32, 
         'double': np.double, 
         'long double': np.longdouble, 
         'float error': np.longdouble,
         'double error': np.longdouble,
         'long double error': np.longdouble,
        }  
)

oneplus_data = pd.read_csv(
  'c:\\Users\\Paweł\\Desktop\\MOWNiT\\lab1\\data\\oneplus.csv', 
  delimiter=';',
  dtype={'float': np.float32, 
         'double': np.double, 
         'long double': np.longdouble,
         'float error': np.longdouble
         }  
)

def plot_values(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['float'], label='Float')
    plt.plot(data['i'], data['double'], label='Double')
    plt.plot(data['i'], data['long double'], label='Long Double')
    plt.xlabel('i')
    plt.ylabel('Wartości')
    plt.title('Wizualizacja wartości Float, Double i Long Double')
    plt.legend()
    plt.show()

def plot_errors(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['float_error'], label='Błąd Float')
    plt.plot(data['i'], data['double_error'], label='Błąd Double')
    plt.plot(data['i'], data['long_double_error'], label='Błąd Long Double')
    plt.xlabel('i')
    plt.ylabel('Błędy względne')
    plt.title('Wizualizacja błędów bezwzględnych')
    plt.legend()
    plt.show()

def plot_float(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['float'], label='Float')
    plt.xlabel('i')
    plt.ylabel('Wartości Float')
    plt.title('Wizualizacja wartości Float')
    plt.legend()
    plt.show()

def plot_double(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['double'], label='Double', color='orange')
    plt.xlabel('i')
    plt.ylabel('Wartości Double')
    plt.title('Wizualizacja wartości Double')
    plt.legend()
    plt.show()

def plot_long_double(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['long double'], label='Long Double', color='green')
    plt.xlabel('i')
    plt.ylabel('Wartości Long Double')
    plt.title('Wizualizacja wartości Long Double')
    plt.legend()
    plt.show()

def plot_oneplus(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['float'], label='Float')
    plt.plot(data['i'], data['double'], label='Double')
    plt.plot(data['i'], data['long double'], label='Long Double')
    plt.xlabel('i')
    plt.ylabel('Wartości')
    plt.title('Wizualizacja wartości 1 + h dla Float, Double i Long Double')
    plt.legend()
    plt.show()

def plot_oneplus_float(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['float'], label='Float')
    plt.xlabel('i')
    plt.ylabel('Wartości Float')
    plt.title('Wizualizacja wartości 1 + h dla Float')
    plt.legend()
    plt.show()

def plot_oneplus_double(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['double'], label='Double', color='orange')
    plt.xlabel('i')
    plt.ylabel('Wartości Double')
    plt.title('Wizualizacja wartości 1 + h dla Double')
    plt.legend()
    plt.show()

def plot_oneplus_long_double(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['long double'], label='Long Double', color='green')
    plt.xlabel('i')
    plt.ylabel('Wartości Long Double')
    plt.title('Wizualizacja wartości 1 + h dla Long Double')
    plt.legend()
    plt.show()

def plot_oneplus_float_error(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['i'], data['error float'], label='Błąd Float')
    plt.xlabel('i')
    plt.ylabel('Błąd Float')
    plt.title('Wizualizacja różnicy wartości Float i Long Double dla 1 + h')
    plt.legend()
    plt.show()

# Call the plotting functions
plot_values(data)
plot_errors(data)
plot_float(data)
plot_double(data)
plot_long_double(data)
plot_oneplus(oneplus_data)
plot_oneplus_float(oneplus_data)
plot_oneplus_double(oneplus_data)
plot_oneplus_long_double(oneplus_data)
plot_oneplus_float_error(oneplus_data)
