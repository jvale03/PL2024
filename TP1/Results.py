import Athlete

def parse_line(line):
    elems = line.split(",")
    return elems

def parse_file(file,dict):
    lines = file.readlines()[1: ]
    for line in lines:
        elems = parse_line(line)
        dict[elems[0]] = Athlete.Athlete(elems[0],elems[1],elems[2],elems[3],elems[4],elems[5],elems[6],elems[7],elems[8],elems[9],elems[10],elems[11],elems[12])

def get_modalities(dict):
    modalities = []
    for key in dict:
        modalities.append(dict[key].get_modality())
    modalities = set(modalities) # converter para set para remover repetidos
    modalities = list(modalities) # converter para lista de volta para poder ordenar
    modalities.sort()
    return modalities

def get_results(dict):
    total = 0
    availables = 0
    for key in dict:
        if (dict[key].get_result() == "true\n"):
            availables+=1
        total+=1
    return round((availables/total),2)*100

def get_age_range(athletes,age_dict):
    for athlete in athletes:
        age = athletes[athlete].get_age()
        age = int(age)
        if(age > 20 and age <= 25):
            age_dict["20-25"].append(athletes[athlete])
        elif(age > 25 and age <= 30):
            age_dict["25-30"].append(athletes[athlete])
        elif(age > 30 and age <= 35):
            age_dict["30-35"].append(athletes[athlete])





if __name__ == "__main__":
    file = open("emd.csv")
    athletes = {}
    ages = {"20-25":[],"25-30":[],"30-35":[]}

    parse_file(file,athletes)

    modalities = get_modalities(athletes)

    for modality in modalities:
        print(modality)
    
    print(f"\nAptos: {get_results(athletes)}%")

    get_age_range(athletes,ages)

    for age in ages:
        print("\n")
        print(age)
        for athlete in ages[age]:
            print(athlete)

    
    
    

