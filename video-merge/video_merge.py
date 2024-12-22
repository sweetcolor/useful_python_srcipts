import os
import sys
from video_merge_error import VideoMergeError
from utils import convert_to_time, convert_to_index
from constants import EXT_SUB, EXT_VIDEO, WORK_PATH


if not WORK_PATH.is_dir():
    raise VideoMergeError(f'{WORK_PATH} is not directory.')


is_clear_needed = len(sys.argv) > 1 and sys.argv[1] == '-C'

video_files = sorted(WORK_PATH.glob(f'*.{EXT_VIDEO}'), key=convert_to_time)
subtitle_files = sorted(WORK_PATH.glob(f'*.{EXT_SUB}'), key=convert_to_index)

for video, subtitle in zip(video_files, subtitle_files):
    output_name = video.with_suffix('.mkv')
    os.system(f'ffmpeg -i "{video}" -i "{subtitle}" -c copy -disposition:s:0 default "{output_name}"')

    if is_clear_needed:
        video.unlink()
        subtitle.unlink()
