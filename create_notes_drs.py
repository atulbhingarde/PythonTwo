import os.path

# set the rootDir where the search will start
rootDir = "/cygdrive/C/Users/212715347/Downloads"
rootDir = "~/Downloads"
if os.path.exists(f'{rootDir}'):
    print(f'{rootDir} exists')
else:
    print(f'{rootDir} does not exists')

# traverse rootDir and locate the files
print(f'root dir is {rootDir}')
for dirName, subdirList, fileList in os.walk(rootDir):
     print('Found directory: %s' % dirName)
     for fname in fileList:
         print('\t%s' % fname)
