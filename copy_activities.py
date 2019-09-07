import os
from pathlib import Path
from shutil import copyfile

# set the rootDir where the search will start
# that is in home dorectory
rootDir = "Downloads"
# build rootDir from rootDir with the base as home "~"
rootDir = os.path.join(Path.home(),rootDir)
# traverse rootDir and locate the files
####
# when the path has Stu_ in it 
####
for dirName, subdirList, fileList in os.walk(rootDir):
    if "Stu_" in dirName:
     for fname in fileList:
        sourceFile =os.path.join(dirName,fname)
        print('\t%s' % sourceFile)
        if not os.path.exists(fname):
            copyfile(sourceFile, fname)
        else:
            print(f'excuse me I can not copy file {fname} as it eists in current directory')
