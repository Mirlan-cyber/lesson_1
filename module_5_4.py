import module_5_3

class House(module_5_3.House):

    houses_history = []

    def __new__(cls, *args, **kwargs):
        #print('Я в нью')
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        #print('Я в ините')
        self.first = args[0]
        self.second = kwargs.get('second')
        self.third = kwargs.get('third')

    def __del__(self):
        print(f'{self.first} снесён, но он останется в истории')


if __name__ == "__main__":
    data = ['data']
    number = {'second': 25, 'third': 3.24}

    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3

    print(House.houses_history)
