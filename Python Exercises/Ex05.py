#Fifth Ex - Modificare l'oggetto CSVFile della lezione precedente
#in modo che alzi una eccezione se il nome del file non è una stringa.
#Modificare quindi la funzione get_data in modo da leggere solo un 
#intervallo di righe del file, aggiungendo gli argomenti start ed
#end opzionali, controllandone la correttezza e sanitizzandoli
#se necessario. Committare il lavoro

#Defining a class to raise custom Errors : FileTitleError
#N.b It has to extend Exception super class
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
                    print('Line {} empty/error - skipped'.format(line))
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
                        print('Line {} empty/error - skipped'.format(line))
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
                        print('Line {} empty/error - skipped'.format(line))

                        current_line += 1
                        continue

                current_line += 1

            afile.close()
            return values



newfile = CSVFile('shampoo_sales.csv')

file_content = newfile.get_data()
print(file_content)

--------------------------------------------------

#Defining a class to raise custom Errors : FileTitleError
#N.b It has to extend Exception super class
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

    def get_data(self, starting_line = None, ending_line = None):

        if(starting_line and ending_line is not None):
            if(starting_line > ending_line):
                print('Invalid parameters indexes')
                return None
            else:
                line_counter = 0
                values = [ ]
                try:
                    afile = open(self.name, 'r')
                except:
                    print('Error - No file with {} name found'.format(self.name))
                    return None
                
                file_read = [ ]
                for line in afile:
                    file_read.append(line)
                    line_counter += 1
                if(starting_line > line_counter):
                    print('Starter out of limits')
                    print('0 Assigned to starting_line')
                    starting_line = 0
                if(ending_line > line_counter):
                    print('Ender out of limits')
                    print('File len assigned to ending_line')
                    ending_line = line_counter

                for line in range(starting_line, ending_line, 1):
                    try:
                        elements = file_read[line].split(',')
                        if(elements[0] != 'Date'):
                            values.append(float(elements[1]))
                    except:
                        print('Line {} empty/error - skipped'.format(afile[line]))

                        continue 
                
                afile.close()
                return values
        
        else:
            print('No parameters initialized - printing full file')
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
                    print('Line {} empty/error - skipped'.format(line))

                    continue

            afile.close()
            return values



newfile = CSVFile('shampoo_sales.csv')

file_content = newfile.get_data()
print(file_content)
