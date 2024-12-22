import pathlib
import re
import time


def _find_time_begin(file_name: str):
    group_name = 'time_begin'
    return re.match(f'.+ (?P<{group_name}>\d\d-\d\d-\d\d) - ', file_name).group(group_name)


def convert_to_time(file_path: pathlib.Path):
    return time.mktime(time.strptime(_find_time_begin(file_path.name), '%H-%M-%S'))


def convert_to_index(file_path: pathlib.Path):
    group_name = 'index'
    return int(re.match(f'(?P<{group_name}>\d\d?)-', file_path.name).group(group_name))


# remove forbidden characters for linux and windows path
# Linux/Unix: /
# Windows: < > : " / \ | ? *
# https://stackoverflow.com/questions/1976007/what-characters-are-forbidden-in-windows-and-linux-directory-names
def clear_name(name: str):
    return re.sub('[\/\|\\\?\<\>\:\*]', '_', name)
