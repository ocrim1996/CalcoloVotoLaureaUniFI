# Algoritmo per il Calcolo del Voto di Laurea Magistrale in Ingegneria Informatica UniFI

Si calcola:

![Schermata 2022-04-24 alle 19.07.38.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/76F5E83C-FAA6-4AE4-97DD-C56680C43B77/A6F0AD2E-C561-45ED-809C-DF22829E8A6E_2/kvAFy4xcwmOnvxenx3Gx30AEqhO2uRpoXnGepuJTh8Ez/Schermata%202022-04-24%20alle%2019.07.38.png)

dove:

- ***M_p*** è la media pesata degli esami con voto;
- ***N_cfu*** è il numero di CFU con voto (pari a 96 per CdLM in Ingegneria Informatica);
- ***V_tesi*** è il voto assegnato alla prova finale (tesi) in 30-esimi.

Il **voto finale di laurea** ***V_L*** (normalizzato a 110, con arrotondamento) si calcola dunque:

![Schermata 2022-04-24 alle 19.07.54.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/76F5E83C-FAA6-4AE4-97DD-C56680C43B77/E623348D-6D67-4E8C-A6DF-CCB2F6543C37_2/QbWRH3Ox9yPvExrGVLsgIB5XCIKR2mARhJvfzUxDXo8z/Schermata%202022-04-24%20alle%2019.07.54.png)

Dove gli **incrementi** ***Δ1*** e ***Δ2*** si calcolano come segue:

![Schermata 2022-04-24 alle 19.08.13.png](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/76F5E83C-FAA6-4AE4-97DD-C56680C43B77/9E5B48BC-1329-46E7-90F4-0071FF66317A_2/xKfP1xbl5QVi0DVCBeY700ITx7yWuYKBsuycacnTsy0z/Schermata%202022-04-24%20alle%2019.08.13.png)

L’**incremento** ***Δ2*** dipende dalla durata della carriera ***T*** (in mesi) definita come la differenza tra le date di verbalizzazione del primo e ultimo esame con voto.

**N.B.** L’incremento è comunque zero per chi non si laurea in corso.

# To Run

Per eseguire il progetto:

```shell
python3 calcolo_voto_di_laurea.py
```