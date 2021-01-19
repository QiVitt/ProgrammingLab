

class ExamException(Exception):
    pass

class Diff:

    def __init__(self, ratio = 1):
        self.ratio = ratio

    def compute(self, lista):

        computed_list = [ ]
        temp_difference = 0

        while(len(lista) >= 2):
            temp_difference = 0

            temp_difference = lista[1] - lista[0]

            temp_difference = temp_difference / self.ratio

            computed_list.append(temp_difference)

            del lista[0]
        
        return computed_list

diff = Diff()
#diff = Diff(2)

result = diff.compute([2, 4, 8, 16])

print(result)