# Eserciziario SymPy - PySTEM Reference Card + Applicazioni Fisiche

Questo documento contiene mini-esercizi per fare pratica con le principali funzioni di SymPy e 3 esercizi finali applicati alla Fisica (Moto Rettilineo Uniforme e Moto Circolare Uniforme).

## 0. Setup Iniziale

```python
import sympy as sy
sy.init_printing()
```

## 1. Simboli, Numeri e Costanti
**Funzioni:** `Symbol`, `symbols`, `Rational`, `pi`, `E`, `oo`

* **Esercizio 1.1:** Crea le variabili simboliche `a`, `b`, `c` e un simbolo `t` definito come reale e positivo.
* **Esercizio 1.2:** Scrivi l'espressione per la somma del numero di Nepero ($e$) e la frazione esatta 5/2.

## 2. Manipolazione di Espressioni
**Funzioni:** `simplify`, `expand`, `factor`, `collect`, `apart`

* **Esercizio 2.1:** Espandi il cubo del binomio `(x + 3)**3`.
* **Esercizio 2.2:** Fattorizza il polinomio `x**2 - 16`.
* **Esercizio 2.3:** Scomponi in fratti semplici l'espressione `1 / (x**2 + 3*x + 2)`.

## 3. Sostituzione e Valutazione Numerica
**Funzioni:** `subs`, `evalf`, `N`, `lambdify`

* **Esercizio 3.1:** Sostituisci `x = 4` nell'espressione `sqrt(x) + 3*x`.
* **Esercizio 3.2:** Valuta numericamente il valore di $\pi$ con 30 cifre decimali.

## 4. Equazioni e Disequazioni
**Funzioni:** `Eq`, `solve`, `linsolve`

* **Esercizio 4.1:** Definisci l'equazione $2x - 8 = 0$ usando `sy.Eq` e risolvila con `solve`.
* **Esercizio 4.2:** Risolvi il sistema lineare: $x + y = 10$ e $x - y = 2$ usando `linsolve`.

## 5. Analisi Matematica
**Funzioni:** `diff`, `integrate`, `limit`, `Sum`

* **Esercizio 5.1:** Calcola la derivata rispetto a `x` della funzione $f(x) = \sin(x^2)$.
* **Esercizio 5.2:** Calcola l'integrale definito di $x^3$ valutato tra $0$ e $2$.
* **Esercizio 5.3:** Calcola il limite per $x \to \infty$ di $\frac{1}{x}$.

## 6. Matrici
**Funzioni:** `Matrix`, `inv`, `det`

* **Esercizio 6.1:** Crea una matrice $2 \times 2$ con i valori `[[2, 1], [1, 3]]` e calcolane il determinante.

---

## PARTE 2: Applicazioni alla Fisica (MRU e MCU)

In questi 3 esercizi applicheremo le potenzialità di calcolo simbolico di SymPy ai concetti di cinematica.

### Esercizio 1: Moto Rettilineo Uniforme (Legge Oraria)
Un ciclista si muove di moto rettilineo uniforme. Scegliamo un sistema di riferimento tale per cui la sua posizione iniziale sia $x_0 = 1000$ m e la sua velocità costante sia $v = 7$ m/s. 
* **Richiesta:** Scrivi la legge oraria $x(t) = x_0 + v \cdot t$ in forma simbolica. Successivamente, imposta un'equazione per trovare a quale istante di tempo $t$ il ciclista si troverà alla posizione $x = 4500$ m e risolvila con `sy.solve`.

```python
t = sy.Symbol('t', real=True, positive=True)
# Scrivi qui il codice per definire l'equazione e risolverla:

```

### Esercizio 2: Moto Circolare Uniforme (Accelerazione Centripeta)
Un'automobile percorre una curva circolare di raggio $r = 60$ m con una velocità tangenziale costante $v = 14$ m/s. 
* **Richiesta:** Usando SymPy, definisci simbolicamente le variabili $v$ ed $r$. Calcola il valore esatto della velocità angolare $\omega = v / r$ e dell'accelerazione centripeta $a_c = v^2 / r$. Infine, valuta il risultato numerico in virgola mobile usando `.evalf()`.

```python
v, r = sy.symbols('v r', positive=True)
# Scrivi qui il codice:

```

### Esercizio 3: Dal Moto Circolare Uniforme al Moto Armonico
Come spiegato nel testo di teoria, la proiezione su un diametro della posizione di un punto che si muove di moto circolare uniforme è un **moto armonico**, descritto dalla legge oraria: $x(t) = r \cos(\omega t)$.
* **Richiesta:**
  1. Definisci l'espressione simbolica $x(t)$.
  2. Calcola simbolicamente la velocità (derivata prima rispetto a $t$) e l'accelerazione (derivata seconda rispetto a $t$).
  3. Dimostra simbolicamente la relazione fondamentale del moto armonico, ovvero verifica che l'espressione $a(t) + \omega^2 x(t)$ si annulli, usando la funzione `sy.simplify()`.

```python
t, r, omega = sy.symbols('t r omega', real=True)
# 1. Definisci x_t:
# x_t = ...

# 2. Calcola v_t (derivata prima) e a_t (derivata seconda):
# v_t = ...
# a_t = ...

# 3. Verifica l'identità a(t) + omega^2 * x(t) == 0:
# identita = sy.simplify(...)
```