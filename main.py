# /c/Users/xxx/AppData/Roaming/Python/Python37/Scripts/pipenv.exe run python main.py 'path' 'pattern**' 'newfilename.txt'

import os
import sys
from shutil import copyfile
try:
    import sh
except ImportError:
    # fallback: emulate the sh API with pbs
    import pbs
    class Sh(object):
        def __getattr__(self, attr):
            return pbs.Command(attr)
    sh = Sh()

print("arg len[" + str(len(sys.argv)) + "] argv: " + str(sys.argv))
dir_to_scan = sys.argv[1]
pattern_to_find = sys.argv[2]
new_file_name = sys.argv[3]

# prepare a /working/ directory to perform all work in and create the git repo in
workingdir = dir_to_scan + '/working'
try:
    os.mkdir(workingdir)
except:
    print('workingdir already exists')


# initialize git repo in /working/
git = sh.git.bake(_cwd=workingdir)
print(git.init())

# chdir and read all filenames
os.chdir(dir_to_scan)
filenames = os.listdir()

# only read files that match the expected pattern
filenames = list(filter(lambda x: (pattern_to_find in x), filenames))

# order the files by moddate to create the history correctly
filenames.sort(key = lambda x: os.stat(x).st_mtime)

# iterate all filtered, ordered files and individually commit them
# using their original file name and modified by dates
for filename in filenames:
    info = os.stat(filename)
    print(filename, info.st_mtime)
    copyfile(filename, workingdir  + '/' + new_file_name)
    print(git.add(new_file_name))
    print(git.commit('--allow-empty', m='update to version \'' + filename + '\'', date=info.st_mtime))


print('Conversion to git repo successful')
print('see [https://github.com/tungstn/filename-vc-to-git] for information')