

class ExamException(Exception):
    pass

class MovingAverage:

    def __init__(self, dimension):
        self.windowdim = dimension

    def compute(self, lista):

        computed_list = [ ]
        temp_sum = 0
        temp_result = 0
        flag = 0

        while(len(lista) >= self.windowdim):
            temp_sum = 0
            for index in range(0, self.windowdim, 1):
                temp_sum += lista[index]

            temp_result = temp_sum / self.windowdim
            computed_list.append(temp_result)
            del lista[0]

        return computed_list


moving_average = MovingAverage(2)

result = moving_average.compute([2, 4, 8, 16])

print(result)

