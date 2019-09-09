import os
from pathlib import Path
from shutil import copyfile
TopDir="CyberSecurity-Notes"
if not os.path.exists(TopDir):
    os.makedirs(TopDir)
else:
    print(f'directory {TopDir} exist I can not proceeed !')
    exit(1)
for MyWeeks in range(1,25):
    WeekName = "Week " + str(MyWeeks)
    print(f'{WeekName}')
    for MyDays in range(1,4):
        FolderName= os.path.join(TopDir,WeekName,str(MyDays))
        # print(f'{FolderName}')
        os.makedirs(FolderName)
