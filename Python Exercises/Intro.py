#First Ex - Scrivere una funzione che sommi tutti gli elementi
#di una lista quindi committare il file

def sum_in_list(gen_list):
    somma = 0
    for item in gen_list:
        somma += item
    return somma



my_list = [ ]
final_sum = 0

dim = int(input('Dimensione della lista: '))

for item in range(0, dim, 1):
    my_list = my_list + [int(input('Numero da inserire nella lista: '))]

final_sum = sum_in_list(my_list)
print("La somma computata e' {} ".format(final_sum))
