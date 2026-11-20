import sympy as sy

sy.init_printing(use_unicode=True)

# 1. Definizione delle variabili simboliche
L, v, dt_tot = sy.symbols('L v dt_tot', positive=True)

# 2. Definizione delle formule fisiche
# Distanza percorsa tra due urti successivi sulla stessa base (andata e ritorno)
ds = 2 * L

# Intervallo di tempo tra due urti successivi sulla base destra
dt = ds / v

# Numero di urti nell'intervallo di tempo totale
N = dt_tot / dt

# 3. Dizionario con i dati numerici del problema (convertiti nel Sistema Internazionale)
dati = {
    L: 0.12,        # 12 cm -> 0.12 m
    v: 5.0e2,       # 5,0 * 10^2 m/s
    dt_tot: 12      # 12 s
}

# 4. Sostituzione dei valori e calcolo dei risultati
dt_val = dt.subs(dati)
N_val = N.subs(dati)

# 5. Stampa delle espressioni simboliche e dei risultati numerici
print(f"Formula intervallo di tempo (dt): {dt}")
print(f"Formula numero di urti (N): {N}\n")

print(f"Intervallo di tempo tra due urti: {dt_val:.2e} s")
print(f"Numero di urti in 12 s: {N_val:.2e} (ovvero {int(N_val)} urti)")