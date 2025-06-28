# Metody Obliczeniowe w Nauce i Technice - Laboratorium 5
## Równania nieliniowe

Stosując metodę Newtona oraz metodę siecznych wyznacz pierwiastki równania $f(x)=0$ w zadanym przedziale.

$$ f(x) = x^n - (1 - x)^m $$
- $ n=12$, 
- $m=14$, 
- przedział: $[-1, 1] $  

Dla metody Newtona wybierz punkty startowe rozpoczynając od wartości końców przedziału, zmniejszając je o 0.1 w kolejnych eksperymentach numerycznych. Odpowiednio dla metody siecznej jeden z końców przedziału stanowić powinna wartość punktu startowego dla metody Newtona, a drugi – początek, a następnie koniec przedziału $[a, b]$.

Porównaj liczbę iteracji dla obu tych metod (dla różnych dokładności $\rho$), stosując jako kryterium stopu:
- $\left| x^{(i+1)} - x^{(i)} \right| < \rho$
- $\left| f(x^{(i)}) \right| < \rho$
