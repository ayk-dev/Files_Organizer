import os, shutil
from helper import get_file_path, get_desktop_path, month, months_short, months_full, year


def create_directory(dir_path):
    os.mkdir(dir_path)


def create_content_file(file_path):
    content_file = open(file_path, 'w')
    content_file.close()


def list_pdf_files(fs, path):
    with open(path, 'w') as file:
        for name in sorted(fs):
            args = name.rstrip('.pdf').split('-')
            file.write(' '.join(args) + '\n')


def move_files_to_new_dir(src, dest):
    destination = shutil.move(src, dest)
    return destination


def run_program(directory):
    try:
        create_directory(directory)
        txt_file_path = get_file_path()
        create_content_file(txt_file_path)

        desktop = get_desktop_path()
        files = [f for f in os.listdir(desktop) if f.startswith(months_short[month])]

        list_pdf_files(files, txt_file_path)
        for file in files:
            shutil.move(os.path.join(desktop, file), os.path.join(directory, file))

    except FileExistsError:
        print(f'Program is supposed to run only once per month and has already been executed,'
              f' please check for folder {months_short[month]} {year} ')