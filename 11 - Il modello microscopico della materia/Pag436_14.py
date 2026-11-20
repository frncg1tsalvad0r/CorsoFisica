import sympy as sy
sy.init_printing(use_unicode=True)

m, E_ctr, v = sy.symbols('m E_ctr v')
dati = {
    m : 6.64e-27,
    E_ctr : 6.21e-21
}

# Una particella che urta su una parete rimbalza di urto elastico
# quindi la velocità varia e quella precedente è esattamente in verso
# opposto quindi la varizaione è 2*v
eq1 = E_ctr - sy.Rational(1,2)*m*v**2

sy.pretty_print(eq1)

sols = sy.solve(eq1, v, dict=True)

print((sols[0][v].subs(dati)*dati[m]*2).evalf())
