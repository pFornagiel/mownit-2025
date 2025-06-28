# Metody Obliczeniowe w Nauce i Technice - Laboratorium 1
## Arytmetyka komputerowa

## Zadanie

Przybliżoną wartość pochodnej funkcji $f(x)$ w punkcie $x$ można obliczyć ze wzoru:

$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}
$$

Wykorzystać ten wzór do obliczenia pochodnej funkcji:

$$
f(x) = \sin(x) + \cos(3x)
$$

w punkcie $x = 1$ dla $h = 2^{-n}$ ($n = 0, 1, 2, \ldots, 40$). Wykonać obliczenia dla różnej precyzji zmiennych. Zwrócić uwagę na typ argumentów i wyników dla funkcji bibliotecznych wykorzystywanych w obliczeniach.

- Jak wytłumaczyć, że od pewnego momentu zmniejszenie wartości $h$ nie poprawia przybliżenia wartości pochodnej?
- Jak zachowują się wartości $1+h$?
- Obliczone przybliżenia pochodnej porównać z dokładną wartością pochodnej.

Obliczenia wykonać dla zmiennych typu `float`, `double`, `long double`.

# Uruchomienie

## Wymagania

- Kompilator G++ ze wsparciem dla C++17
- Make (opcjonalnie, ale zalecane)

## Kompilacja

### Użycie Make

```bash
make
```
dla windows używając mingw32-make
```bash
mingw32-make
```

### Kompilacja ręczna


```bash
g++ -std=c++17 -Wall -Wextra -pedantic -o derivative_test test.cpp
```

## Uruchomienie

```bash
./derivative_test
```

## Pliki wyjściowe

Program generuje następujące pliki:

- `type_info.txt` - Informacje o typach zmiennoprzecinkowych
- `data.csv` - Wyniki obliczeń pochodnych
- `oneplus.csv` - Wyniki obliczeń 1+h
- `actual.txt` - Dokładne wartości pochodnych

## Wizualizacja w Pythonie

Aby zwizualizować wyniki, uruchom:

```bash
python visualize_data.py
```
bądź na systemie windows
```bash
py visualiza_data.py
```

Program wygeneruje wykresy pokazujące porównanie różnych precyzji typów zmiennoprzecinkowych.
