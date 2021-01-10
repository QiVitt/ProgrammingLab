

class Model(object):

    def fit(self, data):
        pass

    def predict(self):
        pass

class IncrementModel(Model):

    def fit(self, data):

        raise NotImplementedError('Questo modello non prevede un fit')

    def predict(self, prev_months):

#prev_months : list of values about previous months

        increment_avg = 0
        temp_sum = 0
        item_counter = 0

        for i in range(0, len(prev_months), 1):
            if(i == 0):
                continue
            else:
                temp_sum += prev_months[i] - prev_months[i-1]
                item_counter += 1
        
        increment_avg = temp_sum / (item_counter)

        return prev_months[-1] + increment_avg


shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

prediction_object = IncrementModel()

prediction = prediction_object.predict(shampoo_sales)

print(prediction)

