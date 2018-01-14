import os
import sys
import re
from urllib import request as urequest
import itertools


class M3UDownloader:
    def __init__(self):
        self.m3u_path = ''
        self.output_dir_path = ''
        self.err_msg = ''
        self._get_argv()

    ###
    # Read argv and check errors
    # TODO Need some universal API for all scripts
    ###
    def _get_argv(self):
        if len(sys.argv) == 3:
            self.m3u_path = sys.argv[1]
            self.output_dir_path = sys.argv[2]
        else:

            self.err_msg += 'Must be 2 arguments\n'
            self._help()
        self._check_argv()
        self._check_err()

    def _check_argv(self):
        if not os.path.isfile(self.m3u_path):
            self.err_msg += 'm3u file path is not correct\n'
        if not os.path.isdir(self.output_dir_path):
            self.err_msg += 'output directory path is not correct\n'

    def _check_err(self):
        if self.err_msg:
            self._help(1)

    def _help(self, status=0):
        print('script.py <m3u file path> <output directory>')
        print(self.err_msg, end='')
        sys.exit(status)

    ###
    # Read and download m3u file
    ###
    def read_m3u(self):
        m3u_dir_name = os.path.splitext(os.path.basename(self.m3u_path))[0]
        self.output_dir_path = os.path.join(self.output_dir_path, m3u_dir_name)
        if not os.path.exists(self.output_dir_path):
            os.mkdir(self.output_dir_path)
        with open(self.m3u_path) as m3u:
            first_line = m3u.readline()
            if not first_line.startswith('#EXTM3U'):
                self.err_msg += 'm3u must start\'s with #EXTM3U\n'
                print(self.err_msg)
                return
            for line in itertools.zip_longest(*[m3u] * 2):
                record_marker = '#EXTINF:'
                url = None
                title = None
                if line[0].startswith(record_marker):
                    title = line[0][len(record_marker)+1:].split(',')[1].strip().replace('/', ' ')
                if re.match('\w+', line[1]):
                    url = line[1].strip()
                file_path = os.path.join(self.output_dir_path, '{}.mp3'.format(title))
                if url and title and not os.path.exists(file_path):
                    urequest.urlretrieve(url, file_path)
                    print(title)
                    print(url)
                    print()


if __name__ == '__main__':
    M3UDownloader().read_m3u()
