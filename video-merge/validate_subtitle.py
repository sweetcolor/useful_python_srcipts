import unittest
from constants import WORK_PATH, EXT_SUB
from utils import count_all_items, convert_to_index


json_file = WORK_PATH.joinpath('info.json').open()
subtitles_count: int = count_all_items(json_file)
print(subtitles_count)

correct_indexes: list = list(range(subtitles_count))


class TestSubtitle(unittest.TestCase):
    def test_indexes(self):
        indexes = sorted(map(convert_to_index, WORK_PATH.glob(f'*.{EXT_SUB}')))
        print('correct_indexes', correct_indexes)
        print('indexes', indexes)

        self.assertEqual(indexes, correct_indexes)


if __name__ == '__main__':
    unittest.main()