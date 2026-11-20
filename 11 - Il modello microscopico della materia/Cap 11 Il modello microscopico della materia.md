# D11 Il modello microscopico della materia

## Mappa dei fondamentali

### La teoria cinetica dei gas

La teoria cinetica dei gas mette in relazione:

* **La grandezza macroscopica pressione** $p$ con la **grandezza microscopica velocità quadratica media** tramite la formula:
  

  $$
  p = \frac{Nm\langle v\rangle^{2}}{3V}
  $$

  
  dove:

  * **Velocità quadratica media:**
    

    $$
    \langle v\rangle = \sqrt{\frac{v_{1}^{2} + v_{2}^{2} + \dots + v_{N}^{2}}{N}}
    $$

  * **Energia cinetica media di traslazione:**
    

    $$
    K_{m,\text{trasl}} = \frac{1}{2}m\langle v\rangle^{2}
    $$

* **La grandezza macroscopica temperatura assoluta** $T$ con la **grandezza microscopica energia cinetica media** tramite la formula:
  

  $$
  K_{m,\text{trasl}} = \frac{3}{2}k_{B}T
  $$

  
  in cui compare la **costante di Boltzmann**:
  

  $$
  k_{B} = 1,380649 \times 10^{-23} \ \frac{\text{J}}{\text{K}}
  $$

  
  dove:

  * **Energia cinetica media:**
    

    $$
    K_{m} = \frac{K_{\text{tot}}}{N} = \frac{K_{1} + K_{2} + \dots + K_{N}}{N}
    $$

### I gas reali

* Sono descritti dall'**equazione di stato di van der Waals**:
  

  $$
  \left(p + \frac{a}{V_{s}^{2}}\right)(V_{s} - b) = \frac{R}{M}T
  $$

* Possiedono una **energia interna** $U$, che:

  * **In generale**, è la somma di due termini:

    1. **Energia potenziale totale** $U_{\text{pot}}$, associata alle forze intermolecolari.

    2. **Energia cinetica totale** $K_{\text{tot}}$, con:
       

       $$
       K_{\text{tot}} = NK_{m}
       $$

       $$
       K_{m} = \frac{l}{2}k_{B}T
       $$

       
       *(dove* $l = 3$ *per molecole monoatomiche e* $l = 5$ *per molecole biatomiche)*

  * **Nell'approssimazione di gas perfetto**, coincide con la sola **energia cinetica totale** $K_{\text{tot}}$.

## Formule

| GRANDEZZA O LEGGE | A PAROLE | IN SIMBOLI | 
| ----- | ----- | ----- | 
| **Energia cinetica media** ($\text{J}$) | $\dfrac{\text{somma delle energie cinetiche delle molecole}}{\text{numero di molecole}}$ | $K_{m} = \dfrac{K_{\text{tot}}}{N} = \dfrac{K_{1} + K_{2} + \dots + K_{N}}{N}$ | 
| **Velocità quadratica media** ($\text{m/s}$) | $\sqrt{\dfrac{\text{somma dei quadrati delle velocità delle molecole}}{\text{numero di molecole}}}$ | $\langle v\rangle = \sqrt{\dfrac{v_{1}^{2} + v_{2}^{2} + \dots + v_{N}^{2}}{N}}$ | 
| **Energia cinetica media di traslazione** | $\dfrac{1}{2} \cdot (\text{massa della singola molecola}) \cdot (\text{velocità quadratica media})^{2}$ | $K_{m,\text{trasl}} = \dfrac{1}{2}m\langle v\rangle^{2}$ | 
| **Pressione di un gas perfetto in funzione della velocità quadratica media** | $\dfrac{(\text{numero di molecole}) \cdot (\text{massa della molecola}) \cdot (\text{velocità quadratica media})^{2}}{3 \cdot (\text{volume del gas})}$ | $p = \dfrac{Nm\langle v\rangle^{2}}{3V}$ | 
| **Costante di Boltzmann** ($\text{J/K}$) | $\dfrac{\text{costante universale dei gas}}{\text{costante di Avogadro}}$  *(è fissata a un valore esatto)* | $k_{B} = \dfrac{R}{N_{A}} = 1,380649 \times 10^{-23} \ \dfrac{\text{J}}{\text{K}}$ | 
| **Energia cinetica media di traslazione in funzione della temperatura assoluta** | Le due grandezze sono direttamente proporzionali. | $K_{m,\text{trasl}} = \dfrac{3}{2}k_{B}T$ | 
| **Velocità quadratica media in funzione della temperatura assoluta** | $\sqrt{\dfrac{3 \cdot (\text{costante di Boltzmann}) \cdot (\text{temperatura assoluta})}{\text{massa della molecola}}}$ | $\langle v\rangle = \sqrt{\dfrac{3k_{B}T}{m}}$ | 
| **Volume specifico di un gas** ($\text{m}^{3}\text{/kg}$) | $\dfrac{\text{volume}}{\text{massa del gas}}$ | $V_{s} = \dfrac{V}{M}$ | 
| **Equazione di stato di van der Waals** | Corregge l'equazione di stato del gas perfetto tenendo conto delle interazioni tra molecole e del volume delle molecole stesse. In essa figurano due coefficienti costanti $a$ e $b$ (che dipendono dal tipo di gas) e la massa molare $M$ del gas (in $\text{kg/mol}$). | $\left(p + \dfrac{a}{V_{s}^{2}}\right)(V_{s} - b) = \dfrac{R}{M}T$ | 
| **Teorema di equipartizione dell'energia** | L'energia cinetica media di un sistema di molecole alla temperatura assoluta $T$ è uguale al numero di gradi di libertà $l$ (numero di coordinate necessarie per descrivere i moti della singola molecola) moltiplicato per $\dfrac{k_{B}T}{2}$. | $K_{m} = \dfrac{l}{2}k_{B}T$ | 
| **Energia interna di** $N$ **molecole o di** $n$ **moli di un gas perfetto** | È l'energia cinetica totale dell'insieme delle molecole, uguale a $N$ volte l'energia cinetica media. Può essere espressa in funzione delle moli $n$ sfruttando l'uguaglianza $Nk_{B} = nR$. | $U = \dfrac{l}{2}Nk_{B}T = \dfrac{l}{2}nRT$ | 
