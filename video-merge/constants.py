import os
import pathlib


EXT_SUB = os.getenv('SUB_EXT', 'srt')
EXT_VIDEO = os.getenv('VIDEO_EXT', 'ts')

WORK_PATH: pathlib.Path = pathlib.Path(os.getenv('WORK_PATH', pathlib.Path.home().joinpath('Downloads')))
