import sympy as sy
import physical_constants as pc

sy.init_printing(use_unicode=True)


'''
V_C = 8L
2mol monoatomico
T=300K
m=6.65e-27 massa molecola
?= pressione
'''

F, V_C, v_rms, P, m, T, N = sy.symbols('F V_C, v_rms, P, m, T, N')
known = {
    V_C : 0.008,
    T : 300,
    m : 6.65e-27
}

N = pc.N_A*2 #2 numero moli
v_rms = sy.sqrt((3*pc.k_B*T)/m)
P = (N*m*v_rms**2)/(3*V_C)
sy.pprint(P)
sy.pprint(known)

#CALCOLO LA PRESSIONE
known_P = P.subs(known)

print(f'Valore Pressione: {known_P.evalf():.2e}')

#CALCOLO RMS
sy.pprint(v_rms)
known_v_rms = v_rms.subs(known)

print(f'Velocità Quadratica Media: {known_v_rms.evalf():.2e}')

#CALCOLO LA FORZA
F = P*sy.cbrt(V_C)**2
known_F = F.subs(known)
print(f'Forza esercitata: {known_F.evalf():.2e}')

