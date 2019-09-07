import os
from pathlib import Path

# set the rootDir where the search will start
rootDir = "/cygdrive/C/Users/212715347/Downloads/"
rootDir = "Downloads/test123"
print(Path.home())
mayBe = os.path.join(Path.home(), 'Downloads/test123')
#mayBe=os.path.abspath(rootDir)
if os.path.exists(f'{mayBe}'):
    print(f'{mayBe} exists')
else:
    print(f'{mayBe} does not exists')

# traverse rootDir and locate the files
# print(f'root dir is {mayBe}')
for dirName, subdirList, fileList in os.walk(mayBe):
    #  print('Found directory: %s' % dirName)
    if "Stu_" in dirName:
     for fname in fileList:
        print('\t%s' % fname)
