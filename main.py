import os
from datetime import date


months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
month = date.today().month
# TODO add -1 to month when project is finished
year = date.today().year


def get_dir_path():
    dir_name = f'{months[month]} {year}'
    absolute_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(absolute_path, 'Documents', 'Rate cons', f'{year}', dir_name)
    return dir_path


def get_file_path():
    file_name = f'{months[month]}_{year}.txt'
    directory_path = get_dir_path()
    file_path = os.path.join(directory_path, file_name)
    return file_path


def create_directory(dir_path):
    os.mkdir(dir_path)


def create_content_file(file_path):
    with open(file_path, 'w') as file:
        file.write('pass')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directory = get_dir_path()
    create_directory(directory)

    file_path = get_file_path()
    create_content_file(file_path)
    # os.remove(file_path)



