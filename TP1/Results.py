import Athlete

def parse_line(line):
    elems = line.split(",")
    return elems

def parse_file(file,dict):
    lines = file.readlines()[1: ]
    for line in lines:
        elems = parse_line(line)
        dict[elems[0]] = Athlete.Athlete(elems[0],elems[1],elems[2],elems[3],elems[4],elems[5],elems[6],elems[7],elems[8],elems[9],elems[10],elems[11],elems[12].replace("\n",""))

def get_modalities(dict):
    modalities = []
    for key in dict:
        modalities.append(dict[key].get_modality())
    modalities = set(modalities) # converter para set para remover repetidos
    modalities = list(modalities) # converter para lista de volta para poder ordenar
    modalities.sort(key=str.lower)
    return modalities

def get_results(dict):
    total = 0
    availables = 0
    for key in dict:
        if (dict[key].get_result() == "true"):
            availables+=1
        total+=1
    return round((availables/total),2)*100

def get_age_range(athletes,age_dict):
    for athlete in athletes:
        age = athletes[athlete].get_age()
        age = int(age)
        for ages in age_dict:
            if age <= ages[1] and age >= ages[0]:
                age_dict[ages].append(athlete)

def generate_range(min, max):
    ranges = {}
    range_min = min - (min % 5)
    range_max = max - (max % 5)

    num_intervalos = (range_max - range_min) // 5 + 1

    for i in range(range_min, range_max + 1, 5):
        range_str = (i,i+4)
        ranges[range_str] = []

    return ranges

def get_min_max(athletes):
    min = 100
    max = 0
    for athlete in athletes:
        age = int(athletes[athlete].get_age())
        if age < min:
            min = age
        if age > max:
            max = age
    return min,max

if __name__ == "__main__":
    file = open("emd.csv")
    athletes = {}

    parse_file(file,athletes)

    modalities = get_modalities(athletes)

    for modality in modalities:
        print(modality)
    
    print(f"\nAptos: {get_results(athletes)}%\n")

    limit = get_min_max(athletes)

    ages = generate_range(limit[0],limit[1])

    get_age_range(athletes,ages)

    for age in ages:
        print(f"{age[0]}-{age[1]}: {len(ages[age])}")


        
        
    

