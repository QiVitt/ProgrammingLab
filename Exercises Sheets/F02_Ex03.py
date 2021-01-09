

class Calcolatrice:

    def somma(a = None, b = None):
        if(a == None and b == None):
            flag = 0
            numbers_to_compute = [ ]
            while(flag != 1):
                number = input('Inserire un numero _ -1 per terminare: ')
                try:
                    number = float(number)
                except:
                    print('Invalid number')
                    continue
                if(number == -1):
                    flag = 1
                    continue
                numbers_to_compute.append(number)
            
            returned_sum = 0
            for item in numbers_to_compute:
                returned_sum += item

            return returned_sum

        else:
            return a + b

    def sottrazione(a = None, b = None):
        if(a == None and b == None):
            flag = 0
            numbers_to_compute = [ ]
            while(flag != 1):
                number = input('Inserire un numero _ -1 per terminare: ')
                try:
                    number = float(number)
                except:
                    print('Invalid number')
                    continue
                if(number == -1):
                    flag = 1
                    continue
                numbers_to_compute.append(number)
            
            returned_difference = numbers_to_compute[0]
            first_skipper = 0
            for item in numbers_to_compute:
                if(item is not numbers_to_compute[0]):
                    returned_difference -= item
        
            return returned_difference

        else:
            return a - b

    def moltiplicazione(a = None, b = None):
        if(a == None and b == None):
            flag = 0
            numbers_to_compute = [ ]
            while(flag != 1):
                number = input('Inserire un numero _ -1 per terminare: ')
                try:
                    number = float(number)
                except:
                    print('Invalid number')
                    continue
                if(number == -1):
                    flag = 1
                    continue
                numbers_to_compute.append(number)
            
            returned_product = 1
            for item in numbers_to_compute:
                returned_product = returned_product*item

            return returned_product

        else:
            return a * b

    def divisione(a = None, b = None):
        if(a == None and b == None):
            flag = 0
            numbers_to_compute = [ ]
            while(flag != 1):
                number = input('Inserire un numero _ -1 per terminare: ')
                try:
                    number = float(number)
                except:
                    print('Invalid number')
                    continue
                if(number == -1):
                    flag = 1
                    continue
                if(number == 0):
                    print('Invalid number - Impossible to divide by 0')
                    continue
                numbers_to_compute.append(number)
            
            returned_division = numbers_to_compute[0]
            first_skipper = 0
            for item in numbers_to_compute:
                if(item is not numbers_to_compute[0]):
                    returned_division = returned_division / item

            return returned_division

        else:
            try:
                return a / b
            except:
                print("Errore nel modulo divisione class Calcolatrice")

    def potenza(a = None, b = None):
        pass

    def modulo(a = None):
        pass

    def radice(self, a = None):
        pass

    def conversione_di_base(self, a = None, b = None):
        pass

class Test:

    try:
        result = Calcolatrice.somma(2, 3)
        if(result != 5):
            raise Exception
    except:
        print('Test somma Non passato!')

# BELOW: HAVING TEST CLASS AS CALCOLATRICE EXTENSION
# Why does it not work (1st comment block)
# While having sum_test defined in a method goes fine (2nd comment block)

#   try:
#       result = super().somma(2, 3)
#       if(result != 5):
#           raise Exception
#   except:
#       print('Test somma Non passato!')

#   def testing_somma(self):
#       try:
#           result = super().somma(2, 3)
#           if(result != 5):
#               raise Exception
#       except:
#           print('Test somma Non passato!')

    try:
        if(Calcolatrice.sottrazione(7, 5) != 2):
            raise Exception
    except:
        print('Test differenza Non passato!')

    try:
        if(Calcolatrice.moltiplicazione(2, 3) != 6):
            raise Exception
    except:
        print('Test moltiplicazione Non passato!')

    try:
        if(Calcolatrice.divisione(10, 5) != 2):
            raise Exception
    except:
        print('Test divisione Non passato!')

testingsum = Calcolatrice.somma(2, 3)
testingdifference = Calcolatrice.divisione(40, 2)
print(testingsum)
print(testingdifference)

#To complete..