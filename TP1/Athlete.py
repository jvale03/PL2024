class Athlete:
    def __init__(self,id,index,date,first_name,last_name,age,gender,address,modality,team,email,federated,result):
        self.id = id
        self.index = index
        self.date = date
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address
        self.modality = modality
        self.team = team
        self.email = email
        self.federated = federated
        self.result = result

    def get_age(self):
        return self.age

    def get_result(self):
        return self.result

    def get_modality(self):
        return self.modality
    
    def __str__(self):
        return f'Id: {self.id}\nName: {self.first_name} {self.last_name}, {self.age} years old\nTeam: {self.team}, Status: {self.result}'