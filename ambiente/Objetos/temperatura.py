class Temperatura:
    
    def __init__(self) -> None:

        self.__temperatura = None
        self.cod_sensor = None

    def set_temperatura(self):
        # Algoritmo utilizado para obter o valor da temperatura do sensor
        # Documentação da biblioteca utilizada: https://pypi.org/project/w1thermsensor/
        # Definir se será uma Thread
        # self.__temperatura = nova_temperatura
        pass    

    def get_temperatura(self):
        return self.__temperatura
        