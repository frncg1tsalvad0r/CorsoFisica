import sympy as sy
sy.init_printing(use_unicode=True)

# azoto  
# S area base del contenitore
# l = 8.02 cm altezza
# pressione sulla base 1N
#p= (Nm⟨v⟩^2)/3V 


m_N, v_qm, S, l, F, N= sy.symbols('m_N v_qm S l F N')
dati = {
    m_N : 4.65e-26,
    v_qm :5.20e2,
    l:0.0802,
    F: 1
}

equa = sy.Eq((N*m_N*v_qm**2)/(3*S*l), F/S)

sy.pretty_print(equa)
sols = sy.solve(equa, N) 
print(sols)
print(sols[0].subs(dati))


