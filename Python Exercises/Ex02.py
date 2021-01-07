#Second Ex - Scrivere uno script che sommi tutti i valori
#delle vendite degli shampoo del file 'shampoo_sales.csv'

afile = open('shampoo_sales.csv', 'r')

values_to_sum = [ ]
final_sum = 0

for line in afile:
    elements = line.split(',')
    if(elements[0] != 'Date'):
        values_to_sum.append(float(elements[1]))

for item in values_to_sum:
    final_sum += item

print("La somma computata e' {} ".format(final_sum))

afile.close()
