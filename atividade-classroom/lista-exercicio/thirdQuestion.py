class Country:
    def __init__(self, name:str, borderContries:list, capital:str, areaKm2:float):
        self.__name = name
        self.__capital = capital
        self.__area = areaKm2
        self.__borderContries = borderContries
    def __str__(self):
        return f'Nome: {self.__name} | Capital: {self.__capital} | Area: {self.__area} | Contries: {self.__borderContries}'
    def getName(self):
        return self.__name
    def getCapital(self):
        return self.__capital
    def getArea(self):
        return self.__area
    def getBorderContries(self):
        return self.__borderContries
    def addBorderContries(self, borderContries:list, borderContrie:str):
        self.__borderContries = borderContries
        if isinstance(borderContrie, str) and borderContrie.strip():
            if borderContrie not in self.__borderContries:
                self.__borderContries.append(borderContrie)
        return self.__borderContries
    
# programa principal (teste)
pais = Country('Brasil', ['Argentina', 'Paraguay', 'Uruguay'], 'Brasilia', 8.516)
print(pais)
pais.addBorderContries(pais.getBorderContries(), 'Colombia')
print(pais)