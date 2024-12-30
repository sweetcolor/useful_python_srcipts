import os
from constants import WORK_PATH


for video in WORK_PATH.glob('*.mkv'):
    output_name = video.with_stem(f'{video.stem} 1080p')
    os.system(f'ffmpeg -i "{video}" -vf scale=1920:1080 -c:a copy -c:s copy "{output_name}"')
