class Request:
    def __init__(self, data):
        converted_data = data.split(' ')

        self.from_ = converted_data[4]
        self.to = converted_data[6]
        self.amount = int(converted_data[1])
        self.product = converted_data[2]
