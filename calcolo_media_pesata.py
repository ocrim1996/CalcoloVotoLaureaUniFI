import sys
import numpy as np
from tabulate import tabulate


def option_menu():
    while True:
        print("\nCosa vuoi fare?")
        print("1) Aggiungere un esame")
        print("2) Termina e Calcola")
        try:
            chosen_function = int(input("\U0000270F Seleziona il numero dell'operazione da eseguire: "))
            if 1 <= chosen_function <= 2:
                return chosen_function
            else:
                print("\nDevi inserire 1 o 2\n")
        except ValueError:
            print("\nDevi inserire 1 o 2\n")


def list_exams(names, grades, weights):
    print()
    print("-" * 5 + " RIEPILOGO ESAMI " + "-" * 30)

    rows = []
    for i in range(len(names)):
        row = [names[i], grades[i], weights[i]]
        rows.append(row)

    print(tabulate(rows, headers=["Esame", "Voto", "CFU"]))


if __name__ == '__main__':
    exams_names = []
    exams_grades = []
    exams_weights = []
    print("--- Calcolatore Media Ponderata Universitaria " + "-" * 30)
    while True:
        choice = option_menu()

        if choice == 1:
            exam_name = input("\U0000270F Inserire il nome dell'esame: ").upper()
            exam_grade = int(input("\U0000270F Inserire il voto dell'esame: "))
            exams_weight = int(input("\U0000270F Inserire il numero di CFU dell'esame: "))
            exams_names.append(exam_name)
            exams_grades.append(exam_grade)
            exams_weights.append(exams_weight)

        elif choice == 2:
            list_exams(exams_names, exams_grades, exams_weights)
            weighted_avg = np.average(exams_grades, weights=exams_weights)
            print("\n· La tua Media Ponderata è:", round(weighted_avg, 3))
            sys.exit(0)

