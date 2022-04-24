# Calcolo per l'incremento Δ1 (basato sui voti)
def incremento1(V_110):
    if V_110 <= 90:
        delta_1 = 0
    elif 90 < V_110 <= 106:
        delta_1 = (V_110 - 90) / 4
    else:
        delta_1 = 4

    return delta_1


# Calcolo per l'incremento Δ2 (basato sul tempo in mesi)
def incremento2(T):
    if T <= 21:
        delta_2 = 1.5
    elif 21 < T <= 26:
        delta_2 = 1.0
    elif 26 < T <= 30:
        delta_2 = 0.5
    else:
        delta_2 = 0

    return delta_2


# Calcolo per la variabile V_100
def calcola_V_110(media_pesata, n_cfu, voto_tesi):
    V_100 = ((media_pesata * n_cfu + voto_tesi * (120 - n_cfu)) / (120)) * (110 / 30)

    return V_100


if __name__ == "__main__":
    """
    Parametri da impostare:
        - media_pesata: inserire la media pesata
        - n_cfu: inserire il numero di CFU (pari a 96 per CdLM in Ingegneria Informatica)
        - T: inserire la durata della carriera in mesi definita come la differenza tra le date di verbalizzazione del 
            primo ed ultimo esame con voto.
    """
    # Inserire i tuoi dati
    media_pesata = 28.53
    n_cfu = 96
    T = 32

    # Si calcola il voto finale con tutti i possibili voti della tesi (da 18 a 30)
    for voto_tesi in range(18, 31):
        V_110 = calcola_V_110(media_pesata, n_cfu, voto_tesi)

        delta_1 = incremento1(V_110)
        delta_2 = incremento2(T)

        # Calcolo del Voto Finale di Laurea ( V_f = V_110 + delta_1 + delta_2 )
        V_L = V_110 + delta_1 + delta_2

        print("·Voto Tesi -> " + str(voto_tesi) + ", Il Voto Finale di Laurea è: " + str(round(V_L)))