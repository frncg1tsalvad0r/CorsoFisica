import sympy as sy
import sympy.physics.units as spu
sy.init_printing(use_unicode=True)

print(spu.boltzmann_constant)

'''
V_C = 8L
2mol monoatomico
T=300K
m=6.65e-27
?= pressione
'''
V_C, m_C, v_qm, P, m, T, k_B = sy.symbols('V_C, m_C, v_qm, P, m, T, k_B')
dati = {
    V_C : 0.008,
    T : 300,
    m : 6.65e-27,
    k_B : spu.boltzmann_constant
}

P = 3*k_B
equa = sy.Eq((m*v_qm**2)/(3*V_C), P)

print(spu.convert_to(spu.boltzmann, spu.meter/spu.second).evalf())


c_val = spu.convert_to(spu.boltzmann_constant, spu.meter / spu.second)
a = c_val.evalf()
print(c_val)
