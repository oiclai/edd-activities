class Country:
    def __init__(self, name:str, borderContries:list, capital:str, areaKm2:float):
        self.__name = name
        self.__capital = capital
        self.__area = areaKm2
        self.__borderContries = borderContries