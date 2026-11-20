import sympy as sy
sy.init_printing(use_unicode=True)

'''
contenitore vuoto
V_C = 3dm^3
m_C = 438.7g

v_qm = 4.40e2 
P = 243kPa
? massa contenitore
'''
V_C, m_C, v_qm, P, m = sy.symbols('V_C, m_C, v_qm, P, m')
dati = {
    V_C : 0.003,
    m_C : 0.4387,
    v_qm : 4.40e2,
    P: 243e3
}

equa = sy.Eq((m*v_qm**2)/(3*V_C), P)

print(sy.solve(equa, m)[0].subs(dati) + dati[m_C])

