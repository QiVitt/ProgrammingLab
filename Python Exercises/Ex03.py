#Third Ex - Creare un oggetto CSVFile che rappresenti un file CSV e
# - venga inizializzato sul nome del file csv
# - abbia un attributo 'name' che ne contenga il nome
# - abbia un metodo 'get_data' che torni i dati dal file CSV
#come numeri di una lista

#Testare sul file 'shampoo_sales.csv'

class CSVFile:

    def __init__(self, filename):
        self.name = filename

    def get_data(self):

        values = [ ]
        afile = open(self.name, 'r')

        for line in afile:
            elements = line.split(',')
            if(elements[0] != 'Date'):
                values.append(float(elements[1]))

        return values

newfile = CSVFile('shampoo_sales.csv')

file_content = newfile.get_data()
print(file_content)
