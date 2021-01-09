class FileTitleError(Exception):
    
    pass

class CSVFile:
    
    def __init__(self, filename):
        try:
            x = isinstance(filename, str)
            if(x is True):
                self.name = filename
            else:
                raise FileTitleError
        except FileTitleError:
            print('Filename does not correspond to a string')
            print('Automatically converting to str value..')
            self.name = str(filename)

    def test_sum(self):
        fres = self.get_data()  #Same object that has to be verified
                                #has to call the method!
        sres = self.get_data(1, 39)
        fres_sum = sum(fres)
        sres_sum = sum(sres)
        if(fres_sum == sres_sum):
            print('La 1a verifica sulla somma ha avuto esito positivo')
        else:
            print('La 1a verifica sulla somma ha avuto esito negativo')

        if(fres != sres):
            return print('Error implementazione funzione get_data ')
        else:
            return print('Funzione get_data implementata correttamente')

    def get_data(self, starting_line = None, ending_line = None):

        if(starting_line is None and ending_line is None):
            print('No Parameters passed - Printing Full file')

            values = [ ]

            try:
                afile = open(self.name, 'r')
            except:
                print('Error - No file with {} name found'.format(self.name))

                return None
            
            for line in afile:
                try:
                    elements = line.split(',')
                    if(elements[0] != 'Date'):
                        values.append(float(elements[1]))
                except:
                    print('Line empty/error - skipped ', end= line + '\n')
                    continue
                
            afile.close()
            return values

        else:
            line_counter = 0
            values = [ ]
            if(starting_line > ending_line):
                print('Invalid parameters indexes')
                return None

            try:
                afile = open(self.name, 'r')
            except:
                print('Error - No file with {} name found'.format(self.name))
                return None
            
            for line in afile:
                line_counter += 1

            afile.seek(0, 0)    #Resetting file "index" to the first line
            
            if(starting_line > line_counter or ending_line > line_counter):
                print('Parameters exceed file dimension')
                print("Printing Full file")

                for line in afile:
                    try:
                        elements = line.split(',')
                        if(elements[0] != 'Date'):
                            values.append(float(elements[1]))
                    except:
                        print('Line empty/error - skipped ', end= line + '\n')
                        continue
                
                afile.close()
                return values

            current_line = 0
            for line in afile:
                if(current_line >= starting_line and current_line <= ending_line):
                    try:
                        elements = line.split(',')
                        if(elements[0] != 'Date'):
                            values.append(float(elements[1]))
                    except:
                        print('Line empty/error - skipped ', end= line + '\n')

                        current_line += 1
                        continue

                current_line += 1

            afile.close()
            return values



newfile = CSVFile('shampoo_sales.csv')
print('')   #Empty line as a separator between skipped lines and values
newfile.test_sum()
