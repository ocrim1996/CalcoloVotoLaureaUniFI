# Algoritmo per il Calcolo del Voto di Laurea Magistrale in Ingegneria Informatica UniFI

Si calcola:

<img src="http://www.sciweavers.org/tex2img.php?eq=V_%7B110%7D%20%3D%20%5Cfrac%7BM_p%20%5Ccdot%20N_%7Bcfu%7D%20%2B%20V_%7Btesi%7D%20%5Ccdot%20%28120%20-%20N_%7Bcfu%7D%29%7D%7B120%7D%20%5Ccdot%20%5Cfrac%7B110%7D%7B30%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="V_{110} = \frac{M_p \cdot N_{cfu} + V_{tesi} \cdot (120 - N_{cfu})}{120} \cdot \frac{110}{30}" width="351" height="43" />

dove:

- *M_p* è la media pesata degli esami con voto;
- *N_cfu* è il numero di CFU con voto (pari a 96 per CdLM in Ingegneria Informatica);
- *V_tesi* è il voto assegnato alla prova finale (tesi) in 30-esimi.

Il **voto finale di laurea** *V_L* (normalizzato a 110, con arrotondamento) si calcola dunque:

<img src="http://www.sciweavers.org/tex2img.php?eq=V_%7BL%7D%20%3D%20V_%7B110%7D%20%2B%20%5CDelta_%7B1%7D%20%2B%20%5CDelta_%7B2%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="V_{L} = V_{110} + \Delta_{1} + \Delta_{2}" width="161" height="18" />


Dove gli **incrementi** Δ_1 e Δ_2 si calcolano come segue:
<img src="http://www.sciweavers.org/tex2img.php?eq=%5CDelta_%7B1%7D%20%3D%20%5Cbegin%7Bcases%7D%0A%20%200%20%26%20%5Ctext%7Bse%20%7D%20V_%7B110%7D%20%5Cleq%2090%5C%5C%0A%20%20%5Cfrac%7BV_%7B110%7D%20-%2090%7D%7B4%7D%20%26%20%5Ctext%7Bse%20%7D%2090%20%3C%20V_%7B110%7D%20%5Cleq%20106%20%5C%5C%0A%20%204%20%26%20%5Ctext%7Bse%20%7D%20V_%7B110%7D%20%3E%20106%0A%5Cend%7Bcases%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\Delta_{1} = \begin{cases}  0 & \text{se } V_{110} \leq 90\\  \frac{V_{110} - 90}{4} & \text{se } 90 < V_{110} \leq 106 \\  4 & \text{se } V_{110} > 106\end{cases}" width="294" height="79" />

<img src="http://www.sciweavers.org/tex2img.php?eq=%5CDelta_%7B2%7D%20%3D%20%5Cbegin%7Bcases%7D%0A%20%201.5%20%26%20%5Ctext%7Bse%20%7D%20T%20%5Cleq%2021%5C%5C%0A%20%201.0%20%26%20%5Ctext%7Bse%20%7D%2021%20%3C%20T%20%5Cleq%2026%5C%5C%0A%20%200.5%20%26%20%5Ctext%7Bse%20%7D%2026%20%3C%20T%20%5Cleq%2030%5C%5C%0A%20%200%20%26%20%5Ctext%7Bse%20%7D%20T%20%5Cgeq%2030%0A%5Cend%7Bcases%7D&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0" align="center" border="0" alt="\Delta_{2} = \begin{cases}  1.5 & \text{se } T \leq 21\\  1.0 & \text{se } 21 < T \leq 26\\  0.5 & \text{se } 26 < T \leq 30\\  0 & \text{se } T \geq 30\end{cases}" width="226" height="101" />

L’**incremento** Δ_2 dipende dalla durata della carriera *T* (in mesi) definita come la differenza tra le date di verbalizzazione del primo e ultimo esame con voto.

**N.B.** L’incremento è comunque zero per chi non si laurea in corso.

