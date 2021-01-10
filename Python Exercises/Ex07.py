

class Model(object):

    def fit(self, data):
        pass

    def predict(self):
        pass

class IncrementModel(Model):

    def fit(self, data):

#data : full data set - values about all months

        self.global_avg_increment = 0   #Initialized
        temp_sum = 0
        item_counter = 0

        for i in range(0, len(data), 1):
            if(i == 0):
                continue
            else:
                temp_sum += data[i] - data[i-1]
                item_counter += 1
            
        global_increment = temp_sum / item_counter
        self.global_avg_increment = global_increment    #Value updated

    def predict(self, prev_months):

#prev_months : list of values about previous n months

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

        return prev_months[-1] + (self.global_avg_increment + increment_avg) / 2

#shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

shampoo_sales = [8, 19, 31, 41, 50, 52, 60]

prediction_object = IncrementModel()

prediction_object.fit(shampoo_sales)

n_months = int(input('Numero di mesi da considerare per il predict: '))

sliced_list = shampoo_sales[-n_months:]

prediction = prediction_object.predict(sliced_list)

print(prediction)

