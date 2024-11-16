class Student:
    def __init__(self, matriculation:int, name:str, scores:list):
        self.matriculation = matriculation; self.name = name; self.scores = scores;

    def get_name(self):
        return self.name
    def get_matriculation(self):
        return self.matriculation
    def average(self): # calcula a media das media
        return sum(self.scores) / len(self.scores)
    def set_name(self):
        newName = input("Digite o novo nome: ")
        if isinstance(newName, str) and newName.strip():
            self.name = newName
        else:
            print("Error: Nome inválido.")
        return self.name

    def add_score(self,score:int, scores:list):
        self.scores = scores
        if isinstance (score, (int, float)) and (score >= 0 and score <= 10):
            self.scores.append(self.score)
        return self.scores
        

# Programa principal
program_student = Student(2856, 'Clara', [7.8, 9.1, 9.2, 9.8, 10, 10])
matriculation = program_student.get_matriculation()
print(matriculation)
name = program_student.set_name()
print(name)
