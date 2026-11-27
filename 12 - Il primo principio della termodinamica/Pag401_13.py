import sympy as sy
import physical_constants as pc
sy.init_printing(use_unicode=True)


'''
h_C = 20cm = 0.2m
r_C = 5cm = 0.05m
n = 0.7 mol monoatomico
T = 20 C = 273.15+20K = 293.15K
V_f = 0.5L = 0.5dm^3 = 0.0005m^3
'''

T = sy.symbols('T')

h_C = 0.2
r_C = 0.05
dV = 0.0005
T = 293.15
n = 0.7

V_i = sy.pi * r_C**2 * h_C
V_f = V_i - dV

print(f"Volume iniziale {V_i.evalf()}")


#CALCOLO IL LAVORO
W = n*pc.R*T*sy.ln(V_f/V_i)

print(f"Potenza scambiata dal sistema {W.evalf():.2e}")


'''
import sympy as sp

# 1. Definizione delle variabili simboliche
r, h, n, T_C, R = sp.symbols('r h n T_C R', positive=True)
dV1, dV2 = sp.symbols('dV1 dV2', positive=True)

# 2. Formule simboliche
# Volume iniziale del cilindro: V1 = pi * r^2 * h
V1 = sp.pi * r**2 * h

# Temperatura in Kelvin
T1 = T_C + sp.Rational(27315, 100)  # 273.15 K

# Volume dopo la compressione isoterma (ridotto di dV1)
V2 = V1 - dV1

# Punto 1: Lavoro compiuto dal sistema nella compressione isoterma reversibile
W1 = n * R * T1 * sp.ln(V2 / V1)

# Punto 2: Calore scambiato nella compressione isoterma (Delta U = 0 => Q1 = W1)
Q1 = W1

# Punto 3: Riscaldamento isobaro (pressione costante) con aumento di volume dV2
# Volume finale V3 = V2 + dV2
V3 = V2 + dV2
# Dall'equazione di stato: P2 * V2 = n * R * T1  =>  P2 = (n * R * T1) / V2
P2 = (n * R * T1) / V2
# Per un gas perfetto monoatomico, cp = 5/2 R, quindi Q2 = n * cp * DeltaT = 5/2 * P2 * dV2
Q2 = sp.Rational(5, 2) * P2 * dV2

# Calore totale scambiato nella trasformazione complessiva
Q_tot = Q1 + Q2

# 3. Sostituzione dei dati numerici (in unità del Sistema Internazionale)
dati = {
    r: 0.050,  # 5,0 cm = 0,050 m
    h: 0.20,  # 20 cm = 0,20 m
    n: 0.70,  # 0,70 mol
    T_C: 20,  # 20 °C
    R: 8.314,  # J / (mol * K)
    dV1: 0.50e-3,  # 0,50 L = 0,50 * 10^-3 m^3
    dV2: 0.30e-3,  # 0,30 L = 0,30 * 10^-3 m^3
}

# Valutazione numerica e conversione in kJ (dividendo per 1000)
W1_kJ = (W1.subs(dati) / 1000).evalf(2)
Q1_kJ = (Q1.subs(dati) / 1000).evalf(2)
Q_tot_kJ = (Q_tot.subs(dati) / 1000).evalf(2)

print(f'1. Lavoro nella compressione (W1): {W1_kJ} kJ')
print(f'2. Calore nella compressione (Q1): {Q1_kJ} kJ')
print(f'3. Calore totale scambiato (Q_tot): {Q_tot_kJ} kJ')
'''
