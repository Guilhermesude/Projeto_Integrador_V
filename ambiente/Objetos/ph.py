class Ph:

    def __init__(self, set_point):
        self.__valor   = None
        self.set_point = set_point

    
    def __set_valor(self):
        # Algoritmo para litura do sensor de pH, inserido em uma Thread
        # self.__valor = novo_valor
        pass

    def get_valor(self):
        self.__set_valor()
        return self.__valor

