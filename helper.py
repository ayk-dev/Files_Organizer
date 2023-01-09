import os
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


def get_month_year():
    month = date.today().month - 1
    year = date.today().year
    if month == 0:
        month = 12
        year -= 1
    return month, year


def get_dir_path():
    month, year = get_month_year()
    dir_name = f'{months_full[month]} {year}'
    absolute_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    dir_path = os.path.join(absolute_path, 'Documents', 'Rate cons', f'{year}', dir_name)
    return dir_path


def get_file_path():
    month, year = get_month_year()
    file_name = f'{months_short[month]}_{year}.txt'
    directory_path = get_dir_path()
    file_path = os.path.join(directory_path, file_name)
    return file_path


def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')