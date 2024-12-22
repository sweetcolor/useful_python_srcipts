import json
import re
from constants import WORK_PATH
from utils import convert_to_time, clear_name


json_file = WORK_PATH.joinpath('info.json').open()
video_files = list(WORK_PATH.glob('*.mkv'))

info = json.load(json_file)

moved_files = 0

for section_index, section in enumerate(info['sections'], start=1):
    name = clear_name(section['name'])
    section_dir = WORK_PATH.joinpath(f'{section_index}. {name}')
    section_dir.mkdir(exist_ok=True)

    times = map(lambda item: item['time'].replace(':', '-'), section['items'])
    names_pattern = re.compile(f'.+({"|".join(times)}).+')

    files_to_section = sorted(filter(lambda file: names_pattern.match(file.name), video_files), key=convert_to_time)

    for file_index, video_file in enumerate(files_to_section, start=1 + moved_files):
        new_name = section_dir / f'{file_index}. {video_file.name}'
        video_file.rename(section_dir / f'{file_index}. {video_file.name}')

    moved_files += len(section['items'])
