from datetime import datetime

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

    def __str__(self):
        try:
            afile = open(self.name, 'r')
        except:
            print('Error - No file with {} name found'.format(self.name))

        header_file = afile.readline()
        print(header_file)


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

    def get_data_vendite(self):

        dates_to_return = [ ]

        try:
            afile = open(self.name, 'r')
        except:
            print('Error - No file with {} name found'.format(self.name))
            return None
        
        for line in afile:
            elements = line.split(',')
            if(elements[0] != 'Date'):
                temp_date = datetime.strptime(elements[0], "%d-%m-%Y")
                dates_to_return.append(temp_date)

        afile.close()
        return dates_to_return


newfile = CSVFile('shampoo_sales.csv')

file_content = newfile.get_data()
file_dates = newfile.get_data_vendite()
print(file_content)
print(25 * '-')
newfile.__str__()
print(25 * '-')
print(file_dates)