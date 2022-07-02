import os, shutil
from datetime import date


months_full = {
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
months_short = {
        1: 'Jan',
        2: 'Feb',
        3: 'Mar',
        4: 'Apr',
        5: 'May',
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
month = date.today().month - 1
year = date.today().year


def get_dir_path():
    dir_name = f'{months_full[month]} {year}'
    absolute_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(absolute_path, 'Documents', 'Rate cons', f'{year}', dir_name)
    return dir_path


def get_file_path():
    file_name = f'{months_short[month]}_{year}.txt'
    directory_path = get_dir_path()
    file_path = os.path.join(directory_path, file_name)
    return file_path


def create_directory(dir_path):
    os.mkdir(dir_path)


def create_content_file(file_path):
    with open(file_path, 'w') as file:
        file.write('pass')


def list_pdf_files(fs, path):
    with open(path, 'w') as file:
        for name in fs:
            args = name.rstrip('.pdf').split('-')
            file.write(' '.join(args) + '\n')


def move_files_to_new_dir(src, dest):
    destination = shutil.move(src, dest)
    return destination


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    directory = get_dir_path()

    try:
        create_directory(directory)
        txt_file_path = get_file_path()
        create_content_file(txt_file_path)
        # os.remove(file_path)

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        files = [f for f in os.listdir(desktop) if f.startswith(months_short[month])]

        list_pdf_files(files, txt_file_path)
        for file in files:
            shutil.move(os.path.join(desktop, file), os.path.join(directory, file))

    except FileExistsError:
        print(f'Program is supposed to run only once per month and has already been executed,'
              f' please check for folder {months_short[month]} {year} ')






#TODO sort the names in the .txt file by date








