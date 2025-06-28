# Metody Obliczeniowe w Nauce i Technice - Laboratorium 7
## Rozwiązywanie układów równań liniowych metodami iteracyjnymi

Dany jest układ równań liniowych $Ax = b$.

Elementy macierzy $A$ są zadane wzorem:

$$a_{ij} = \begin{cases}
k & \text{dla } i = j \\
\frac{n}{m} & \text{dla } i \neq j \\
0.5 & \text{dla } |i - j| = 1
\end{cases}$$

- $i, j = 1, 2, \ldots, n$
- $k=11$
- $m=2$

Przyjmij wektor $x$ jako dowolną $n$-elementową permutację ze zbioru $\{1, -1\}$ i oblicz wektor $b$.

## Zadanie 1:

Metodą Jacobiego rozwiąż układ równań liniowych $Ax = b$ (przyjmując jako niewiadomą wektor $x$), przyjmując kolejno kryterium stopu:

1. $\|x^{(i+1)} - x^{(i)}\| < \varepsilon$

2. $\|Ax^{(i)} - b\| < \varepsilon$

Obliczenia wykonaj dla różnych rozmiarów układu $n$, dla różnych wektorów początkowych, a także różnych wartości $\varepsilon$ w kryteriach stopu. (Podaj, jak liczono normę.) Wyznacz liczbę iteracji oraz sprawdź różnicę w czasie obliczeń dla obu kryteriów stopu.

Sprawdź dokładność obliczeń.

## Zadanie 2:

Dowolną metodą znajdź promień spektralny macierzy iteracji (dla różnych rozmiarów układu – takich, dla których znajdowane były rozwiązania układu). Sprawdź, czy spełnione są założenia o zbieżności metody dla zadanego układu.

Opisz metodę znajdowania promienia spektralnego.