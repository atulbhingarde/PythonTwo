import os
from pathlib import Path
from shutil import copyfile
TopDir="CyberSecurity-Notes"

os.makedirs(TopDir)
for MyWeeks in range(1,25):
    WeekName = "Week " + str(MyWeeks)
    print(f'{WeekName}')
    for MyDays in range(1,4):
        print(f'{MyDays}')
