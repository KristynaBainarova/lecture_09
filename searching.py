import os
import json

# get current working directory path
cwd_path = os.getcwd()
# git gui je alternativa příkazů

def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    #absolutní cesta
    #nebo celá cesta

    #relativní by byla: file = "sequentional.json"
    with open("sequential.json") as data:
        data = json.load(data)
        print(data)
    if field in data.keys():
        return data[field]
    else:
        return None
data = read_data("sequential.json", "unordered_numbers")



def linear_search(numbers, wanted_num):
    found_pos = []
    for pos, num in enumerate(numbers):
        if num == wanted_num:
            found_pos.append(pos)

    vysledek = dict()

    vysledek["positions"] = found_pos
    vysledek["count"] = len(found_pos)
    return vysledek

print(linear_search(data, 2))


data_pattern = read_data("sequential.json", "dna_sequence")
def pattern_search(data_pattern, pattern):
    found_pattern = ()



def main():
    pass


if __name__ == '__main__':
    main()