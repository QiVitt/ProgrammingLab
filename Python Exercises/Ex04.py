#Fourth Ex - Modificare l'oggetto CSVFile della lezione precedente
#in modo che dia un messaggio d'errore se si cerca di aprire un file
#non esistente. Aggiungere quindi due campi al file shampoo_sales.csv
#Gestire gli errori che verranno generati in modo che le linee
#vengano saltate e venga stampato a schermo l'errore. Committare
#N.b I due campi vanno aggiunti alla fine del file

class CSVFile:

    def __init__(self, filename):
        self.name = filename

    def get_data(self):

        values = [ ]
        try:
            afile = open(self.name, 'r')
        except:
            print('Generic Error - Could not open file correctly.')

            return None

        for line in afile:
            try:
                elements = line.split(',')
                if(elements[0] != 'Date'):
                    values.append(float(elements[1]))
            except:
                print('Line {} empty/error - skipped'.format(line))

                continue


        afile.close()
        return values

newfile = CSVFile('shampoo_sales.csv')

file_content = newfile.get_data()
print(file_content)