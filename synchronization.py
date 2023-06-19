""" 
Please implement a program that synchronizes two folders: source and replica. The
program should maintain a full, identical copy of source folder at replica folder.
Solve the test task by writing a program in one of these programming languages:

- Synchronization must be one-way: after the synchronization content of the
replica folder should be modified to exactly match content of the source
folder;
- Synchronization should be performed periodically.
- File creation/copying/removal operations should be logged to a file and to the
console output;
- Folder paths, synchronization interval and log file path should be provided
using the command line arguments;
- It is undesirable to use third-party libraries that implement folder
synchronization;
- It is allowed (and recommended) to use external libraries implementing other
well-known algorithms. For example, there is no point in implementing yet
another function that calculates MD5 if you need it for the task – it is
perfectly acceptable to use a third-party (or built-in) library. 
"""

#Get original path, replica path, log file path and sync interval through the command line

#Check contents of the original folder and compare to the replica folder by looping through both of them

#For every difference, register the kind of operation needed to match the subsequent folders(create/copy/remove), log it in a file and console and match both of the folders