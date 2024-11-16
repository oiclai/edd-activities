class Date:
    def __init__(self, day:int, month:int, year:int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f'{self.__day}/{self.__month}/{self.__year}'
    
# Programa Principal
program_date = Date(28, 5, 2024)
print(program_date)