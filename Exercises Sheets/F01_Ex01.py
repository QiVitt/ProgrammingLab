import math

def stampa(lista):
    print(lista)

def statistiche(lista):
    flag = 0
    somma = 0
    media = 0
    for item in lista:
        x = isinstance(item, int)
        if(x != True):
            flag = 1
            print('La lista inserita contiene elementi non int')
            return None
    
    item_counter = 0
    minimo = lista[0]
    massimo = lista[0]
    if(flag == 0):
        for item in lista:
            somma += item 
            if(item < minimo):
                minimo = item
            if(item > massimo):
                massimo = item 
            item_counter += 1

        media = somma / item_counter
        print('Valori computati:')
        print('Somma: {}'.format(somma))
        print('Media: {}'.format(media))
        print('Massimo: {}'.format(massimo))
        print('Minimo: {}'.format(minimo))

def somma_vettoriale(lista1, lista2):
    flag = 0
    computed_list = [ ]
    for item in lista1:
        x = isinstance(item, int)
        if(x != True):
            flag = 1
            print('La prima lista inserita contiene elementi non int')
            return computed_list

    flag = 0
    for item in lista2:
        x = isinstance(item, int)
        if(x != True):
            flag = 1
            print('La seconda lista inserita contiene elementi non int')
            return computed_list

    item_counter_flist = 0
    item_counter_slist = 0

    for item in lista1:
        item_counter_flist += 1

    for item in lista2:
        item_counter_slist += 1

    if(item_counter_flist != item_counter_slist):
        print("Sum List dimensions Error")
        return computed_list

    position_counter = 0
    for item in lista1:    #Iter on a generic list / lista1 - lista2
        vect_sum = int(math.sqrt( (lista1[position_counter]**2)*(lista2[position_counter]**2) ) )
        computed_list.append(vect_sum)
        position_counter += 1
    
#    while(len(lista1) != 0):   AA This operation works on the original list!
#        vect_sum = int(math.sqrt( (lista1[0]**2)*(lista2[0]**2) ) )
#        computed_list.append(vect_sum)
#        del lista1[0]
#        del lista2[0]
    
    return computed_list

def prodotto_vettoriale(lista1, lista2):
    flag = 0
    computed_list = [ ]
    for item in lista1:
        x = isinstance(item, int)
        if(x != True):
            flag = 1
            print('La prima lista inserita contiene elementi non int')
            print('ATTENZIONE: Non sono riuscito a calcolare il prodotto vettoriale')
            return 

    flag = 0
    for item in lista2:
        x = isinstance(item, int)
        if(x != True):
            flag = 1
            print('La seconda lista inserita contiene elementi non int')
            print('ATTENZIONE: Non sono riuscito a calcolare il prodotto vettoriale')
            return

    item_counter_flist = 0
    item_counter_slist = 0

    for item in lista1:
        item_counter_flist += 1

    for item in lista2:
        item_counter_slist += 1

    if(item_counter_flist != item_counter_slist):
        print("Product List dimensions Error")
        print('ATTENZIONE: Non sono riuscito a calcolare il prodotto vettoriale')
        return

    vect_product = 0
    position_counter = 0
    for item in lista1:
        temp_value = lista1[position_counter] * lista2[position_counter]
        vect_product += temp_value
        position_counter += 1

    return vect_product

first_trial_list = [1, 2, 3, 4, 5]
second_trial_list = [6, 7, 8, 9, 10]

stampa(first_trial_list)
stampa(second_trial_list)

statistiche(first_trial_list)
statistiche(second_trial_list)

trial_sum_list = somma_vettoriale(first_trial_list, second_trial_list)
trial_product = prodotto_vettoriale(first_trial_list, second_trial_list)
print(trial_sum_list)
print(trial_product)





