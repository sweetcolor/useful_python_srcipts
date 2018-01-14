import os
import sys
import glob
import shutil


def glob_files(ext):
    return set(glob.glob('*%s' % ext))


if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print('Directory param not found. Please enter directory path')
    sys.exit(1)

if not shutil.which('ffmpeg'):
    print('ffmpeg is not installed!')
    sys.exit(2)

if not os.path.isdir(path):
    print('Wrong directory path')
    sys.exit(3)

prev_dir = os.getcwd()
os.chdir(path)
print(path)
mp4_ext = '.mp4'
opus_ext = '.opus'
mp4_files = glob_files(mp4_ext)
opus_files = glob_files(opus_ext)
for mp4_file in mp4_files:
    for opus_file in opus_files:
        if mp4_file[:-len(mp4_ext)] == opus_file[:-len(opus_ext)]:
            out_name = mp4_file[:-len(mp4_ext)] + '_' + mp4_ext
            params = '-map 0:0 -map 1:0 -vcodec copy -acodec aac -strict -2'
            os.system(
                'ffmpeg -i "{video}" -i "{audio}" {params} "{out_name}"'.format(
                    video=mp4_file, audio=opus_file,
                    params=params, out_name=out_name
                ))
            if os.path.isfile(out_name) and os.stat(out_name).st_size:
                os.remove(mp4_file)
                os.remove(opus_file)
                os.rename(out_name, mp4_file)
            break
os.chdir(prev_dir)
