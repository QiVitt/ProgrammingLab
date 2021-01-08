from datetime import datetime

def date_values():
    date_elements_to_return = [ ]

    afile = open('shampoo_sales.csv', 'r')

    for line in afile:
        elements = line.split(',')
        if(elements[0] != 'Date'):
            temp_date = datetime.strptime(elements[0], "%d-%m-%Y")
            date_elements_to_return.append(temp_date)
            
    afile.close()
    return date_elements_to_return

list_trial = [ ]

list_trial = date_values()

for date in list_trial:
    print(date.strftime("%d-%m-%Y"))


