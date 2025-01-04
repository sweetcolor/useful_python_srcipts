import pathlib
from urllib.parse import urlparse
from haralyzer import HarParser
from constants import WORK_PATH, EXT_SUB


saved_subtitles = set()

for har_file in WORK_PATH.glob('*.har'):
    har_page = HarParser.from_file(har_file).pages[0]

    for entry in har_page.entries:
        subtitle_name: pathlib.Path = pathlib.Path(urlparse(entry.url).path.split('/')[-1])

        if subtitle_name.suffix == f'.{EXT_SUB}' and not subtitle_name in saved_subtitles:
            subtitle_path: pathlib.Path = WORK_PATH / subtitle_name

            with subtitle_path.open('w') as subtitle:
                content: str = entry.response.text

                print(subtitle_path)
                subtitle.write(content)

            saved_subtitles.add(subtitle_name)
