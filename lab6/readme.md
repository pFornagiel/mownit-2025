# Metody Obliczeniowe w Nauce i Technice - Laboratorium 6
## Rozwiązywanie układów równań liniowych metodami bezpośrednimi

Dany jest układ równań liniowych $Ax = b$.

### 1) Pierwsza macierz

Elementy macierzy $A$ o wymiarze $n \times n$ są określone wzorem:

$$a_{ij} = \begin{cases}
1 & \text{dla } i = j \\
\frac{1}{i + j - 1} & \text{dla } i \neq j
\end{cases}$$

gdzie $i, j = 1, \ldots, n$

Przyjmij wektor $x$ jako dowolną $n$-elementową permutację ze zbioru $\{1, -1\}$ i oblicz wektor $b$.

Następnie metodą eliminacji Gaussa rozwiąż układ równań liniowych $Ax = b$ (przyjmując jako niewiadomą wektor $x$). Przyjmij różną precyzję dla znanych wartości macierzy $A$ i wektora $b$.

Sprawdź, jak błędy zaokrągleń zaburzają rozwiązanie dla różnych rozmiarów układu (porównaj – zgodnie z wybraną normą – wektory $x$ obliczony z $x$ zadany). Przeprowadź eksperymenty dla różnych rozmiarów układu.

### 2) Druga macierz

Powtórz eksperyment dla macierzy zadanej wzorem:

$$a_{ij} = \begin{cases}
2^i & \text{dla } i \geq j \\
a_i \cdot a_j & \text{dla } i < j
\end{cases}$$

gdzie $i, j = 1, \ldots, n$

Porównaj wyniki z tym, co otrzymano w przypadku układu z punktu 1). Spróbuj uzasadnić, skąd biorą się różnice w wynikach. Sprawdź uwarunkowanie obu układów.

### 3) Macierze trójdiagonalne

Powtórz eksperyment dla jednej z macierzy zadanej wzorem poniżej. Następnie rozwiąż układ metodą przeznaczoną do rozwiązywania układów z macierzą trójdiagonalną. Porównaj wyniki otrzymane dwoma metodami (czas, dokładność obliczeń i zajętość pamięci) dla różnych rozmiarów układu. Przy porównywaniu czasów należy pominąć czas tworzenia układu. Opisz, jak w metodzie dla układów z macierzą trójdiagonalną przechowywano i wykorzystywano macierz $A$.


$$a_{ij} = \begin{cases}
k & \text{dla } i = 1 \\
\frac{m + i}{i + 1} & \text{dla } i = i \\
\frac{k}{m + i} & \text{dla } i = i + 1 \\
0 & \text{dla } |i - j| > 1 \text{ oraz } i \neq 1
\end{cases}$$

 
- $i, j = 1, \ldots, n$, 
- $k=7$, 
- $m=3$