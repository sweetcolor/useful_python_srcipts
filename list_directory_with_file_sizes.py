# python3 list_directory_with_file_sizes.py -r <dir_name>
# TODO add total sizes for subdirectories

import os
import sys


def dir_base_name(path_):
    return os.path.basename(os.path.normpath(path_))


def rec_print_text(writable_file, text):
    print(text)
    writable_file.write(text + '\n')


def shorting_dir_path(path_, base_name):
    path_arr = path_.split(os.path.sep)
    idx = path_arr.index(base_name)
    return path_arr[idx:]


def file_sizes(file_path):
    size = os.path.getsize(file_path)
    one_kibibyte = 1024
    template = '{num:.2f} {prefix}b'
    if size < one_kibibyte:
        return template.format(num=size, prefix='')
    elif size < one_kibibyte ** 2:
        return template.format(num=round(size / one_kibibyte, 2), prefix='K')
    elif size < one_kibibyte ** 3:
        return template.format(num=round(size / one_kibibyte ** 2, 2), prefix='M')
    elif size < one_kibibyte ** 4:
        return template.format(num=round(size / one_kibibyte ** 3, 2), prefix='G')
    else:
        return template.format(num=round(size / one_kibibyte ** 4, 2), prefix='T')


def get_prefix(arr_path):
    spaces = '  '
    return spaces * (len(arr_path) - 1), spaces * len(arr_path)


arg = sys.argv[1]
recurse = False
if arg == '-r':
    recurse = True
    path = sys.argv[2]
else:
    path = arg
if os.path.isdir(path):
    start_dir_path = os.path.split(path)[1]
    with open(os.path.join(path, '%s.txt' % start_dir_path), 'w') as file_:
        print(os.getcwd())
        if recurse:
            for (dir_name, sub_share, file_share) in os.walk(path):
                shorter_dir_path = shorting_dir_path(dir_name, start_dir_path)
                dir_prefix, file_prefix = get_prefix(shorter_dir_path)
                rec_print_text(file_, dir_prefix + '[' + os.path.join(*shorter_dir_path) + ']')
                for f_name in file_share:
                    if not f_name.startswith('.'):
                        rec_print_text(file_, '{0}{1}  --  {2}'.format(file_prefix, f_name,
                                                                       file_sizes(os.path.join(dir_name, f_name))))

        else:
            for item in os.listdir(path):
                print(item)
                file_.write(item + '\n')
else:
    print('%s is not directory' % path)
