import fnmatch, os
from pathlib import Path
import pathlib
from shutil import copyfile
def pptx_copy(rootDir):
    # set the rootDir where the search will start
    # that is in home dorectory
    #rootDir = "Downloads"
    # build rootDir from rootDir with the base as home "~"
    rootDir = os.path.join(Path.home(),rootDir)
    # traverse rootDir and locate the files
    ####
    # when the path has Stu_ in it 
    ####
    # store currenet directory and build target directory based on current directory 

    curDir=os.path.curdir
    targetDir=os.path.join(curDir,"target")

    print(f'{rootDir}')
    for files in pathlib.Path(rootDir).glob("**/*.ppt?"):
        print(f'files is {files}')
    # if not os.path.exists(targetDir):
    #     os.makedirs(targetDir)
    # moveOn = True
    # for dirName, subdirList, fileList in os.walk(rootDir):
    #     if ( "Stu_" in dirName ):
    #         for fname in fileList:
    #             sourceFile = os.path.join(dirName,fname)
    #             targetFile = os.path.join(targetDir,fname)
    #             #print('\t%s' % sourceFile)
    #             #print(f'{targetDir}')
    #             if not os.path.exists(targetFile):
    #                 copyfile(sourceFile, targetFile)
    #             else:
    #                 print(f'excuse me I can not copy \n source file {sourceFile} as \n target file {targetFile} exists')
    #                 moveOn = False
    #                 break
    #         else:
    #             if ( not moveOn ):
    #                 break
    #         if ( not moveOn ):
    #                 break
pptx_copy("Downloads")
# test
