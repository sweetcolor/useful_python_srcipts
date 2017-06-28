# remove some Windows trashes
# like Zone.Identifier, Thumbs.db and Thumbs.db:encryptable

import sys
import os
import re


class TrashFileRemover:
    def __init__(self):
        self.directory = None

    def run(self):
        self._argv_parse()
        self._check_values()
        self._remove_temp_files()

    def _remove_temp_files(self):
        for (dir_name, subdir, files) in os.walk(self.directory):
            for file in files:
                if re.search('(Zone\.Identifier)|(Thumbs)', file):
                    print('%s/%s' % (dir_name, file))
                    os.remove(os.path.join(dir_name, file))

    def _set_recursion(self, val=True):
        self.recursion = val

    def _set_directory(self, dir_):
        if os.path.isdir(dir_):
            self.directory = dir_
        else:
            print('%s: No such file or directory' % dir_)
            sys.exit(1)

    def _print_help(self):
        pass

    def _argv_switcher(self, key, val):
        argv = {
            '-h': lambda: self._print_help,
            '-d': lambda: self._set_directory(val)
        }
        return argv.get(key, lambda: None)()

    def _check_values(self):
        if not self.directory:
            print('Directory not selected!')
            self._print_help()
            sys.exit(2)
        print('Selected directory: %s' % self.directory)

    def _argv_parse(self):
        sys.argv.append('')
        argv = sys.argv
        for i in range(1, len(argv)-1):
            self._argv_switcher(argv[i], argv[i + 1])


r = TrashFileRemover()
r.run()
