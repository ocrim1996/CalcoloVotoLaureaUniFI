# Algoritmo per il Calcolo del Voto di Laurea Magistrale in Ingegneria Informatica UniFI

Si calcola:

$$
V_{110} = \frac{M_p \cdot N_{cfu} + V_{tesi} \cdot (120 - N_{cfu})}{120} \cdot \frac{110}{30}
$$

dove:

- $$M_{p}$$ è la media pesata degli esami con voto;
- $$N_{cfu}$$ è il numero di CFU con voto (pari a 96 per CdLM in Ingegneria Informatica);
- $$V_{tesi}$$ è il voto assegnato alla prova finale (tesi) in 30-esimi.

Il **voto finale di laurea** $$V_{L}$$ (normalizzato a 110, con arrotondamento) si calcola dunque:

$$
V_{L} = V_{110} + \Delta_{1} + \Delta_{2}
$$

Dove gli **incrementi** $$\Delta_{1}$$ e $$\Delta_{2}$$ si calcolano come segue:

$$
\Delta_{1} = \begin{cases}
  0 & \text{se } V_{110} \leq 90\\
  \frac{V_{110} - 90}{4} & \text{se } 90 < V_{110} \leq 106 \\
  4 & \text{se } V_{110} > 106
\end{cases}
\\
\\
\\
\Delta_{2} = \begin{cases}
  1.5 & \text{se } T \leq 21\\
  1.0 & \text{se } 21 < T \leq 26\\
  0.5 & \text{se } 26 < T \leq 30\\
  0 & \text{se } T \geq 30
\end{cases}
$$

L’**incremento** $$\Delta_{2}$$ dipende dalla durata della carriera $$T\,$$ (in mesi) definita come la differenza tra le date di verbalizzazione del primo e ultimo esame con voto.

**N.B.** L’incremento è comunque zero per chi non si laurea in corso.

