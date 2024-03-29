# PythonTwo
Python Assignment two
# Instructions

In this exercise, you will use Python to complete four practical challenges:
* Creating 24 directories for each week of class, each containing 3 folders for each day of class
* Copying files from _**`~/Downloads`**_ into the current directory
* Adding the copy script to the _**`PATH`**_
* Add an alias for the copy script to _**`~/.bashrc`**_

---

## Class Notes Folder

Create a script called _**`create_notes_drs.py`**_. In the file, define and call a function called _**`main`**_ that does the following:

* Creates a directory called _**`CyberSecurity-Notes`**_ in the current working directory
* Within the _**`CyberSecurity-Notes`**_ directory, creates 24 sub-directories (sub-folders), called _**`Week 1`**_, _**`Week 2`**_, _**`Week 3`**_, and so on until up through _**`Week 24`**_
* Within each week directory, create 3 sub-directories, called _**`Day 1`**_, _**`Day 2`**_ , and _**`Day 3`**_
![create folders](create_notes_drs.png)

**Bonus Challenge**: Add a conditional statement to abort the script if the directory `CyberSecurity-Notes` already exists.

![stop because directory alredy exists](cant_proceed.png)
---

## Copying Student Exercises

So far you've used a few different Python modules, but for the rest of the homework, you will need to familiarize yourself with a new one. The `shutil` module is a Python module used for high-level file operations like moving and copying. Read [this beforehand](https://www.journaldev.com/20536/python-shutil-module) to get familiar with `shutil` and make sure to use the [documentation](https://docs.python.org/3.5/library/shutil.html#module-shutil) while you're working through the homework. 

<!-- '/cygdrive/c/cygwin64_2/usr/libexec/git-core/git-credential-manager.exe' get: /cygdrive/c/cygwin64_2/usr/libexec/git-core/git-credential-manager.exe: No such file or directory -->
test



Create a script called _**`copy_activities.py`**_ with a function called _**`stu_activities`**_ that does the following:
for _**`housekeeping`**_ purpose I have taken leiberty to copy the files to a folfder named _**`target`**_  that could be cleaned up after verification or maintained for testing purpose as deemed

* Finds files in _**`~/Downloads`**_ that contain the string _**`Stu_`**_
* Copies these files into the current working directory

**Note**: This isn't just a challenge to complete for the sake of it, this is a practical script you can run to move any downloaded files from class into your class notes directories.


below picture depicts that if a _**targetfile**_ exists copy process stops totally. In this case the file _**`Akamai_StateOfInternet_2017.pdf`**_ exists more than once in the source directory structure hence it breaks from the loop

![stop if the file exists](copy_activities.png)
test
---

## Copy Class Slides

Create a script called _**`copy_slides.py`**_ with a function called _**`pptx_copy`**_
Students will create a script that does the following:

* Finds files in _**`~/Downloads`**_ with the file extension _**`.pptx`**_ or _**`.ppt`**_
* Copies these files into the current working directory

**Note**: This is another practical script you can use to move downloaded slides from class into your class notes directories.

---

## Updating PATH and Add an Alias

**Note**: Consider this a _bonus_. You do _not_ need to complete this step for credit. But, these tools will come up in class later, so you're strongly encouraged to study up now!

Now these great scripts have been written, but they are only executable from their relative path - where the files are in your system. In this final step, we'll make them accessible to you anywhere in your system directory.

* First, read the [following article](http://linuxcommand.org/lc3_wss0020.php) to learn more about `.bashrc`, `PATH`, aliases, and the `export` command and answer the following questions.
    * What is the main difference betweeen `~/.bashrc` and the `~/.bash_profile`?
    * What does the `export PATH` command do?
    * What is the benefit of creating aliases?
* Create a directory called `/usr/local/bin` and move your three scripts into this directory.
* Update your `.bashrc` to add the directory `/usr/local/bin` to `PATH` with the following command:

```
export PATH=$PATH:/usr/local/bin
```

* Finally create aliases in `.bashrc` for the three scripts
    * `alias copy_activities="copy_activities.py"`
    * `alias copy_slides="copy_slides.py"`
    * `alias create_notes_drs="create_notes_drs.py"`

## Submission
Please submit `create_notes_drs.py`, `copy_slides.py`, and `copy_notes.py`.
