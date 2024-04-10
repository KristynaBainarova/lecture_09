import os

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


def main():
    pass


if __name__ == '__main__':
    main()