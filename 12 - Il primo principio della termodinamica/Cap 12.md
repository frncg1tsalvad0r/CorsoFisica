**Esercizio 1: Calcolo del calore con capacità termica variabile tramite integrazione simbolica (Problema 148)**

Il problema 148 richiede di determinare la quantità di calore necessaria per innalzare la temperatura di 2,000 mol di azoto a pressione atmosferica da 300,0 K a 500,0 K tramite una trasformazione isobara reversibile. La complessità risiede nel fatto che il calore specifico molare a pressione costante, $C_p$, non è un valore fisso, ma è espresso come una funzione a tratti della temperatura $T$:

* Per temperature inferiori a 432,0 K, $C_p$ è costante e pari a $14,57 J/(mol \cdot K)$.


* Per temperature superiori, $C_p$ cresce in modo lineare seguendo l'equazione $C_p = a + bT$, dove $a = 13,22 J/(mol \cdot K)$ e $b = 0,003124 J/(mol \cdot K^2)$.



**L'approccio con SymPy:**
Questo esercizio è perfetto per illustrare il modulo di calcolo infinitesimale (calcolo integrale) di SymPy. Per trovare il calore totale $Q = n \int C_p(T) dT$, è necessario impostare la somma di due integrali definiti.

* Usando il modulo `sympy`, si dichiara prima la variabile di integrazione con `T = sympy.Symbol('T')`.


* SymPy permette di valutare analiticamente gli integrali usando la funzione `sympy.integrate`. Si calcola il primo tratto con `integrate(14.57, (T, 300, 432))` e il secondo tratto lineare con `integrate(13.22 + 0.003124*T, (T, 432, 500))`.


* SymPy manterrà il risultato in forma esatta fino a quando non decideremo di convertirlo in un valore in virgola mobile per la risposta finale, applicando il metodo `.evalf()` per estrarre l'approssimazione numerica (5842 J). In questo modo eliminiamo del tutto il rischio di propagare errori di arrotondamento intermedi.



---

**Esercizio 2: Derivazione di espressioni analitiche in un ciclo termodinamico (Problema 145)**

In questo scenario, un gas perfetto monoatomico esegue un ciclo reversibile composto da tre trasformazioni consecutive:

1. Un'isocora dallo stato iniziale $A(V_A, p_A)$ a uno stato $B$ in cui la pressione raddoppia ($p_B = 2p_A$).


2. Un'espansione adiabatica dallo stato $B$ a uno stato $C$.


3. Una compressione isoterma che riporta il sistema dallo stato $C$ allo stato iniziale $A$.
La richiesta è determinare espressioni puramente algebriche: la pressione $p_C$ in funzione di $p_A$ e il volume $V_C$ in funzione di $V_A$.



**L'approccio con SymPy:**
Questo problema mette in luce le enormi potenzialità di SymPy come Computer Algebra System (CAS) per la manipolazione di equazioni senza alcun dato numerico.

* Si definiscono tutti i simboli coinvolti nel sistema con `sympy.symbols("p_A, V_A, p_B, V_B, p_C, V_C")`.


* Conoscendo le leggi delle trasformazioni termodinamiche, traduciamo la fisica in vincoli algebrici per SymPy. Per l'isocora, si imposta $V_B = V_A$ e $p_B = 2p_A$. Per l'adiabatica reversibile di un gas monoatomico ($\gamma = 5/3$), il programma gestirà l'espressione $p_B V_B^{5/3} = p_C V_C^{5/3}$. Per l'isoterma, vale $p_C V_C = p_A V_A$.


* Invece di risolvere i passaggi algebrici a mano (che richiederebbero manipolazioni tediose con potenze frazionarie), si passa l'intero sistema di equazioni alla funzione `sympy.solve`, specificando `[p_C, V_C]` come incognite da isolare.


* La libreria risolve automaticamente l'algebra dei sistemi non lineari e restituisce le espressioni chiuse esatte: $p_C = 2^{-3/2} p_A$ e $V_C = 2^{3/2} V_A$.