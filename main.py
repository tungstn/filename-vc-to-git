import os
import sys

print("Arguments length and args:")
print(len(sys.argv))
print(str(sys.argv))

workingdir = 'working'
try:
    os.mkdir(workingdir)
except:
    print('workingdir already exists')

filenames = os.listdir()
for filename in filenames:
    info = os.stat(filename)
    print(filename, info.st_mtime)


#sys.argv[1]

try:
    import sh
except ImportError:
    # fallback: emulate the sh API with pbs
    import pbs
    class Sh(object):
        def __getattr__(self, attr):
            return pbs.Command(attr)
    sh = Sh()

git = sh.git.bake(_cwd=workingdir)
print(git.init())
print(git.status())
# checkout and track a remote branch
# print git.checkout('-b', 'somebranch')
fakefile = os.open(workingdir+'/fake.txt', os.O_RDWR|os.O_CREAT)
os.close(fakefile)

# add a file
print(git.add('.'))
# commit
print(git.commit(m='my commit message'))
# now we are one commit ahead
print(git.status() )


print('Exit Successful')