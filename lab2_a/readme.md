# Metody Obliczeniowe w Nauce i Technice - Laboratorium 2a
## Interpolacja - zagadnienie Lagrange'a

Dla poniższej funkcji wyznacz dla zagadnienia Lagrange’a wielomian interpolujący w postaci Lagrange’a i Newtona.

$$
f(x) = x^2 - m \cdot \cos\left(\frac{\pi x}{k}\right)
$$

Gdzie:  
- $k = 0.5$  
- $m = 5$  
- Przedział: $[-5, 5]$

Interpolację przeprowadź dla różnej liczby węzłów (np. $n = 3, 4, 5, 7, 10, 15, 20$).  
Dla każdego przypadku interpolacji porównaj wyniki otrzymane dla różnego rozmieszczenia węzłów:  
- równoodległe  
- Czebyszewa

Oceń dokładność, z jaką wielomian przybliża zadaną funkcję.  
Poszukaj wielomianu, który najlepiej przybliża zadaną funkcję.  
Wyszukaj stopień wielomianu, dla którego można zauważyć efekt Runge’go (dla równomiernego rozmieszczenia węzłów).  
Porównaj z wyznaczonym wielomianem dla węzłów Czebyszewa.