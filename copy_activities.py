import os
from pathlib import Path

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
        print('\t%s' % fname)
