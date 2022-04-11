import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name) #spojuje dvě cesty dohromady, lomítky
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(sequence, number):
    search_res = {"positions":[], "count":0}
    for index, value in enumerate(sequence): #oindexuje sequenci
        if value == number:
            search_res["positions"].append(index)
            search_res["count"] += 1
    return search_res #vrací celý slovnik

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    results = linear_search(sequential_data, 0) #zjišťuje kde jsou nuly
    print(results)
    dna_sequence = read_data("sequential.json", "dna_sequence")
    print(dna_sequence)

    pass

def pattern_search(sequence, pattern):
    positions = set() #vytvoření množiny
    index = 0
    while index < len(sequence) - len(pattern):#pokračujeme až do konce znaků
        idx = 0
        for letter in sequence[index:index + len(pattern)]:
            if letter != pattern[idx]:
                break
            else:
                idx = idx + 1
            if idx == len(pattern):
                positions.add(index) #metoda add protože se jedná o množiny
            index = index + 1
        return positions

    idx = 1



#ukazatel - ukazuje, na jakém jsme indexu
if __name__ == '__main__':
    main()