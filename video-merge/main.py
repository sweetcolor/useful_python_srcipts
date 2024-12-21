import os
import pathlib
import re
import sys
import time
from video_merge_error import VideoMergeError
from constants import EXT_SUB, EXT_VIDEO, WORK_PATH


if not WORK_PATH.is_dir():
    raise VideoMergeError(f'{WORK_PATH} is not directory.')


is_clear_needed = len(sys.argv) > 1 and sys.argv[1] == '-C'


def find_time_begin(file_name: str):
    group_name = 'time_begin'
    return re.match(f'.+ (?P<{group_name}>\d\d-\d\d-\d\d) - ', file_name).group(group_name)


def convert_to_time(file_path: pathlib.Path):
    return time.mktime(time.strptime(find_time_begin(file_path.name), '%H-%M-%S'))


def convert_to_index(file_path: pathlib.Path):
    group_name = 'index'
    return int(re.match(f'(?P<{group_name}>\d\d?)-', file_path.name).group(group_name))


video_files = sorted(WORK_PATH.glob(f'*.{EXT_VIDEO}'), key=convert_to_time)
subtitle_files = sorted(WORK_PATH.glob(f'*.{EXT_SUB}'), key=convert_to_index)

for video, subtitle in zip(video_files, subtitle_files):
    output_name = video.with_suffix('.mkv')
    os.system(f'ffmpeg -i "{video}" -i "{subtitle}" -c copy -disposition:s:0 default "{output_name}"')

    if is_clear_needed:
        video.unlink()
        subtitle.unlink()
